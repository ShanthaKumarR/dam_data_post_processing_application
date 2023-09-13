from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox, QDialog, QLineEdit, QPushButton
from seasave_data_post_processing.path_xml import Create_path_xml
from threading import Thread
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
import os
from xml.dom import minidom
import json
import logging
from log import empty_field_alert

try:
    if os.path.isdir('log'):
        pass
    else:
        os.mkdir('log')        
except:
     pass


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('log\\data_post_processing.log')
file_handler.setFormatter(formatter)
LOGGER.addHandler(file_handler)


#important note: onle single file or a file full of folder can be converted at once 
# this is because only these actions are supported by the batch file process



class DataPostProcessingController(QObject):
    DOWN    = 1
    UP      = -1

    def __init__(self, model_table, controls, data_post_processing_model_obj, data_post_processing_backend_obj, dpc_template_CB, DP_SEBbatchLE):
        QObject.__init__(self)
        self.ui_controls = controls(self)
        self.module_table = model_table
        self.model = QStandardItemModel(parent = self)
        self.module_table.setModel(self.model)        
        self.fileName = list()
        self.path_xml= Create_path_xml()
        self.module_table.doubleClicked.connect(self.on_Click)
        self.data_post_processing_model_obj = data_post_processing_model_obj
        self.data_post_processing_backend_obj = data_post_processing_backend_obj
        self.dpc_template_CB = dpc_template_CB
        self.DP_SEBbatchLE = DP_SEBbatchLE
        self.set_suggestion()
        self.isExeLocationFile_exist()
        self.load_previous_exe_location()
        self.on_start_run()
    def on_close(self):
        try:
            os.mkdir('model_history')
            self.save_template('model_history\\pp_temp.json')
        except FileExistsError:
            self.save_template('model_history\\pp_temp.json')

    def on_start_run(self):
        try:
                with open('model_history\\pp_temp.json', 'r') as model_name:
                    my_temp_data = json.load(model_name)
                    #self.model.setRowCount(0)
                    #self.model.setColumnCount(0)
                    return self.load_table_for_tepmplate(([my_temp_data[keys]['model_name'] for keys in my_temp_data], [my_temp_data[keys]['parameters'] for keys in my_temp_data]))
        except:
            '''template is empty'''
            self.model.setRowCount(0)

            self.model.setColumnCount(0)
    def moveCurrentRow(self, direction=DOWN):
            if direction not in (self.DOWN, self.UP):
                return       
            model = self.model
            selModel = self.module_table.selectionModel()
            selected = selModel.selectedRows()
            if not selected:
                return
            items = []
            indexes = sorted(selected, key=lambda x: x.row(), reverse=(direction==self.DOWN))
            for idx in indexes:
                items.append(model.itemFromIndex(idx))
                rowNum = idx.row()
                newRow = rowNum+direction
                if not (0 <= newRow < model.rowCount()):
                    continue
                rowItems = model.takeRow(rowNum)
                model.insertRow(newRow, rowItems)
                file_in_old_possition = self.fileName[rowNum]
                file_moving_to_new_position = self.fileName[newRow]
                self.fileName[rowNum] = file_moving_to_new_position
                self.fileName[newRow] = file_in_old_possition
            selModel.clear()

            for item in items:
                selModel.select(item.index(), selModel.Select|selModel.Rows)
                

    def removeModel(self):
        model = self.model
        indices = self.module_table.selectionModel().selectedRows() 
        try:
            for index in sorted(indices):
                model.removeRow(index.row()) 
                self.fileName.pop(index.row())
        except IndexError:
            'please select single model at once'
            empty_field_alert('please delete single model at a time')
            LOGGER.info('please delete single model at a time')

    
    def on_Click(self):
            index=(self.module_table.selectionModel().currentIndex())
            value=index.sibling(index.row(),index.column()).data() 
            filePath = 'processing_modules_cookies'+'/'+ self.fileName[index.row()] 
            model_dict = {'AlignCTDW':self.data_post_processing_model_obj.showAlignCTDWindow, 'BinAvgW':self.data_post_processing_model_obj.showBinAverage,\
                 'BuoyancyW':self.data_post_processing_model_obj.showBuoyancyWindow, 'CellTMW':self.data_post_processing_model_obj.showCellThermalMassWindow, \
                     'DeriveW':self.data_post_processing_model_obj.showDriveWindow, 'DeriveTEOS_10W':self.data_post_processing_model_obj.showDeriveTEOS10Window,\
                         'FilterW':self.data_post_processing_model_obj.showFilterWindow, 'LoopEditW':self.data_post_processing_model_obj.showLoopEditWindow, \
                              'W_FilterW':self.data_post_processing_model_obj.showWindowFilterWindow, 'WildEditW':self.data_post_processing_model_obj.showWildEditWindow,\
                                  'DatCnvW':self.data_post_processing_model_obj.showDatcnvWindow, 'BottleSumW':self.data_post_processing_model_obj.showBottleSummaryWindow, \
                                      'MarkScanW':self.data_post_processing_model_obj.showMarkScanWindow}

            [model_dict[key](filePath, value) for key in model_dict if value == key]

    def prepare_batch_arg(self):
        try:
            if os.path.isdir('files'):
                with open('files\\arg_file.txt', 'w') as line:
                    pass
            else:
                 os.mkdir('files')
                 with open('files\\arg_file.txt', 'w') as line:
                        pass
        except:
            LOGGER.info('Not possible to create file to append batch argument')
        
        try:
            self.data_post_processing_backend_obj.set_file_path(self.fileName, self.get_selected_models())
            self.data_post_processing_thread()
        except FileNotFoundError:
            empty_field_alert('file not found')

    def data_post_processing_thread(self):
        if os.path.isfile(self.DP_SEBbatchLE.text()+'\\SBEBatch.exe'):
            self.process_thread = Thread(target=self.data_post_processing_backend_obj.process_data, args =( self.get_selected_models(), self.DP_SEBbatchLE.text()), daemon= True)
            self.process_thread.start()
        else:
            empty_field_alert('SBEbatch executable not found in the given location (possibly file renamed or moved or deleted or corrupted)')
            LOGGER.info('SBEbatch executable not found in the given location (possibly file renamed or moved or deleted or corrupted)')

    def getBatchSetupFilePath(self):
        tempSetupFilePath = self.DP_SEBbatchLE.text()
        batchSetupFilePath = QFileDialog.getExistingDirectory( parent = None, caption='SEB data processing executable')
        if not batchSetupFilePath:
            self.DP_SEBbatchLE.setText(tempSetupFilePath)
        else:
            self.DP_SEBbatchLE.setText(batchSetupFilePath)
        

    def get_selected_models(self):
        row =  self.model.rowCount()
        row = [self.model.item(row, 0) for row in range(row)]
        return [item.text() for item in row]


    def save_template(self, template_file_path):
        tag_name_list = ['sigleOrMultipleFile', 'setupFilePath', 'instrumentconfigPath', 'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend', 'outputFileName']
        data = {}
        
        for file, model, inx in zip(self.fileName, self.get_selected_models(), range(len(self.fileName))):
            with open('processing_modules_cookies\\'+file, 'r') as f:
                domObj = minidom.parse(f)
                model_tag = domObj.getElementsByTagName(model)               
                parammeters = {}
                for pathTag in tag_name_list:                     
                    for tag in model_tag:                       
                        try:                           
                            value = tag.getElementsByTagName(pathTag)[0].childNodes[0].nodeValue     
                            parammeters[pathTag] = value                    
                        except:
                            pass
        
                data[inx]= {'model_name': model, 'parameters':parammeters}
         
        with open(template_file_path, 'w') as jf:
            json.dump(data, jf, indent=4)

    def evnt(self):
        self.alert = QMessageBox()
        self.alert.setWindowTitle('Alert')
        self.alert.setText('Option to save the value!')
        self.alert.setInformativeText('Do you want save these model values as template?')
        self.alert.addButton('yes', QMessageBox.YesRole )
        self.alert.addButton('No', QMessageBox.NoRole)
        ret = self.alert.exec()
        if ret == 0:
            self.getPath()
        elif ret == 1:
            pass

    def getPath(self):       
        self.path = QDialog()
        self.path.resize(450, 100)
        self.path.setWindowTitle("Template Name")
        self.enterTemplateName = QLineEdit(self.path)
        self.enterTemplateName.setPlaceholderText('Enter Template Name')
        self.enterTemplateName.setGeometry(QtCore.QRect(20, 50, 200, 20))       
        self.enterPathButton = QPushButton('ok', self.path)
        self.enterPathButton.setGeometry(QtCore.QRect(230, 50, 200, 20))
        self.enterPathButton.clicked.connect(lambda: self.checkForDuplicateFile())
        self.path.exec_()

    def checkForDuplicateFile(self, template_dir = 'temp'):
        template_name = self.enterTemplateName.text()

        templates = os.listdir(template_dir)
        
        if not template_name+'.json' in templates and len(template_name)>0:
            self.dpc_template_CB.addItem(template_name)
            self.save_template(template_dir+'\\'+template_name+'.json')


        elif template_name+'.json' in templates:
            self.fileOverWriteAlert = QMessageBox()
            self.fileOverWriteAlert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.fileOverWriteAlert.setText('Template '+ '"'+template_name+'"' + 'alredy exist'+ '\n' + 
            'Do you want to overwrite the existing file ?')
            ret = self.fileOverWriteAlert.exec()

            if ret == QMessageBox.Yes:
                os.remove('temp\\'+template_name+'.json')
                self.save_template(template_dir+'\\'+template_name+'.json')
                self.path.close()
            elif ret == QMessageBox.No:
                pass

        
        
    def get_sugesstion(self, File_name):
        for file in os.listdir(File_name):
            if os.path.isfile(os.path.join(File_name, file)):
                yield file


    def set_suggestion(self):
        try:
            if os.path.isdir('temp'):
                if len(os.listdir('temp')) == 0:
                    with open('temp\\--No_template_selected--.txt', 'w') as file:
                        pass
                else:
                    self.add_saved_templates()
            else:
                os.mkdir('temp')
                with open('temp\\--No_template_selected--.txt', 'w') as file:
                    pass
                self.add_saved_templates()
        except:
            pass

            
        
    def delete_template(self):
        if self.dpc_template_CB.currentText() != '--No_template_selected--':
            self.alert = QMessageBox()
            self.alert.setWindowTitle('Alert')
            self.alert.setText('You are trying to delete the template '+self.dpc_template_CB.currentText())
            self.alert.setInformativeText('Do you want delete the template?')
            self.alert.addButton('yes', QMessageBox.YesRole )
            self.alert.addButton('No', QMessageBox.NoRole)
            ret = self.alert.exec()
            if ret == 0:
                os.remove('temp\\'+self.dpc_template_CB.currentText()+'.json')
                ret = self.dpc_template_CB.findText(self.dpc_template_CB.currentText())
                self.dpc_template_CB.removeItem(ret)
                self.dpc_template_CB.setCurrentIndex(0)
            elif ret == 1:
                pass
    
    def add_saved_templates(self, directory = 'temp\\'):
        suggestion = os.listdir(directory)
        suggestion=[x.split('.')[0] for x in suggestion]
        [self.dpc_template_CB.addItem(file_name) for file_name in suggestion]
                    
    def get_info_from_template(self): 
        try:
            if not self.dpc_template_CB.currentText() == '--No_template_selected--':
                with open('temp\\'+self.dpc_template_CB.currentText()+'.json', 'r') as model_name:
                    my_temp_data = json.load(model_name)
                    self.model.setRowCount(0)
                    self.model.setColumnCount(0)
                    return ([my_temp_data[keys]['model_name'] for keys in my_temp_data], [my_temp_data[keys]['parameters'] for keys in my_temp_data])
        except:
            '''template is empty'''
            self.model.setRowCount(0)
            self.model.setColumnCount(0)
            

    

    def load_table_for_tepmplate(self, modules):
        self.fileName.clear()
        try:
            for inx, saved_value in enumerate(zip(modules[0], modules[1])):
                self.add_standard_item(saved_value[0])
                self.assign_value_from_template_to_module_file(self.fileName[inx], saved_value[1], saved_value[0])
           
        except TypeError:
            self.model.setRowCount(0)
            self.model.setColumnCount(0)
           

    def add_standard_item(self, module_name:str)->None:
        item = QStandardItem(module_name)
        self.model.appendRow(item)
        self.create_file_for_module(module_name, str(self.model.indexFromItem(item).row()))
        
    def create_file_for_module(self, module_name:str, row:str)->None:
        if module_name  in ['DatCnvW', 'BottleSumW', 'MarkScanW']:
            self.path_xml.ModuleTags(root_name= 'data_processing_modules', tag_name=['Raw_data_processing'],  data_processing_modules=[module_name],
            file_path= 'processing_modules_cookies'+'/'+module_name+row+'.xml')
            self.fileName.append(module_name+row+'.xml')
        else:
            self.path_xml.ModuleTags(root_name= 'data_processing_modules', tag_name=['data_processing'], data_processing_modules =[module_name], \
                file_path= 'processing_modules_cookies'+'/'+module_name+row+'.xml')
            self.fileName.append(module_name+row+'.xml')
    
    

    def assign_value_from_template_to_module_file(self, file_Path:str, parameter:dict, module_name:str)-> None:
        try:
            with open( 'processing_modules_cookies'+'/'+file_Path, 'r', encoding="utf-8")as f:
                domObj = minidom.parse(f)
                dataConversion = domObj.getElementsByTagName(module_name)[0]   
                for key in parameter:
                    if parameter[key] == '':
                        dataConversion.getElementsByTagName(key)[0].childNodes[0].nodeValue = 'No_path'
                    else:
                        dataConversion.getElementsByTagName(key)[0].childNodes[0].nodeValue = parameter[key]
            with open( 'processing_modules_cookies'+'/'+file_Path, 'w', encoding="utf-8")as f:
                domObj.writexml(f)
                
        except FileNotFoundError:
           pass
                
    def load_previous_exe_location(self, folder ='exe_file', file_name = 'exe.json', key='SBExe_folder'):
        try:
            
            with open(folder+'//'+file_name, 'r') as file:
                path_dict = json.load(file)
                self.DP_SEBbatchLE.setText(path_dict[key])
        except:
            pass
    
    def isExeLocationFile_exist(self, folder ='exe_file', file_name = 'exe.json', key='SBExe_folder'):
        try:
            if os.path.isdir(folder):
                if os.path.isfile(folder+'//'+file_name):
                    pass
                else:
                    with open(folder+'//'+file_name, 'w') as file:
                        path_dict = {key: 'Nil'}
                        json.dump(path_dict, file, indent =4)
            else:
                os.mkdir(folder)
                with open(folder+'//'+file_name, 'w') as file:
                    path_dict = {key: 'Nil'}
                    json.dump(path_dict, file, indent =4)
        except:
            pass
    
    def SBExe_location(self, folder ='exe_file', file_name = 'exe.json', key='SBExe_folder'):
        try:
            with open(folder+'//'+file_name, 'r') as file:
                path_dict = json.load(file)
                path_dict[key] = self.DP_SEBbatchLE.text()

                with open(folder+'//'+file_name, 'w') as file:
                    json.dump(path_dict, file, indent =4)
        except FileNotFoundError:
            pass

    def on_close_run(self, close_method):
        self.SBExe_location()
        close_method()