from xml.dom import minidom 
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox, QCheckBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from xml.dom import minidom 
from UI.ui_module_a import Ui_widget
from UI.ui_module_B import Ui_Form

class DataPostProcessing:
    @staticmethod
    def getSystemFilePath(setupFileLE, obj):
        tempSetupFilePath = setupFileLE.text()
        SetupFilePath, _ = QFileDialog.getOpenFileName(obj, 'System file', 'F:\\', "system file (*.psa)")
        if not SetupFilePath:
            setupFileLE.setText(tempSetupFilePath)
        else:
            setupFileLE.setText(SetupFilePath)    
    @staticmethod
    def getInputConfigFilePath(InsconfigFileLE, obj):
        tempInputConfigPath = InsconfigFileLE.text()
        InputConfigPath, _ = QFileDialog.getOpenFileNames(obj, 'System file', 'F:\\', "(*.xmlcon *.con)")
        
        if not InputConfigPath:
            InsconfigFileLE.setText(tempInputConfigPath)
        else:
            InsconfigFileLE.setText(InputConfigPath[0])
    @staticmethod
    def getInputDirPath(InputdirLE, obj):
        tempInputDirPath = InputdirLE.text()
        InputDirPath= QFileDialog.getExistingDirectory(obj, 'Input Directory Path')
        if not InputDirPath:
            InputdirLE.setText(tempInputDirPath)
        else:
            InputdirLE.setText(InputDirPath)
    @staticmethod
    def getOutPutDirpath(OutputdirLE, obj):
        tempOutputDirPath = OutputdirLE.text()
        OutputDirPath = QFileDialog.getExistingDirectory(obj, 'Output Directory Path')
        if not OutputDirPath:
            OutputdirLE.setText(tempOutputDirPath)
        else:
            OutputdirLE.setText(OutputDirPath)
   
    @staticmethod
    def getInputFileName(moduleName, InputFileNameLE, obj):
        tempInputFilePath = InputFileNameLE.text()
        if moduleName == 'DatCnvW':
            InputFileName, _ = QFileDialog.getOpenFileNames(obj, 'System file', 'F:\\', "system file (*.hex *.dat)")   
        else:
            InputFileName, _ = QFileDialog.getOpenFileNames(obj, 'System file', 'F:\\', "system file (*.cnv)")  
        if not InputFileName:
            InputFileNameLE.setText(tempInputFilePath)
        else:
            file = InputFileName[0].split('/')[-1]
            InputFileNameLE.setText(file)
            



    
class ModelWindow(QWidget):
    def __init__(self, uiFormPath):
        super().__init__()
        #self.__uiForm 
        self.resize(750, 600)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self = loadUi(uiFormPath, self)
 


class DataPostProcessingModels(DataPostProcessing):
    def __init__(self):
        DataPostProcessing.__init__(self)              

    def showDatcnvWindow(self, filePath, model_Name):  
        self.modelWindowDat = Ui_widget() 
        self.modelWindowDat.ros_file = QCheckBox(self.modelWindowDat.frame_5)
        self.modelWindowDat.ros_file.setText('Include ros file')
        self.modelWindowDat.horizontalLayout.addWidget(self.modelWindowDat.ros_file)
        

        self.dataPostProcessingModuleIntiA(filePath, self.modelWindowDat, model_Name)             
        self.modelWindowDat.show()

    def showWindowFilterWindow(self, filePath, model_Name):  
        self.modelWindowWindowFilter =  Ui_Form() 
        self.modelWindowWindowFilter.DP_TitleLB.setText('Window Filter')
        self.dataPostProcessingModuleIntiB(filePath, self.modelWindowWindowFilter, model_Name)  
        self.modelWindowWindowFilter.show()

    def showBuoyancyWindow(self, filePath, model_Name):  
        self.modelWindowBuoyancy = Ui_Form() 
        self.modelWindowBuoyancy.DP_TitleLB.setText('Buoyancy')
        self.dataPostProcessingModuleIntiB(filePath, self.modelWindowBuoyancy, model_Name)  
        self.modelWindowBuoyancy.show()
        
    def showMarkScanWindow(self, filePath, model_Name):
        self.modelWindowMarkScan =  Ui_widget() 
        self.modelWindowMarkScan.DP_TitleLB.setText('Mark Scan')
        self.dataPostProcessingModuleIntiB(filePath, self.modelWindowMarkScan, model_Name)
        self.modelWindowMarkScan.show()

    def showFilterWindow(self, filePath, model_Name):   
        self.modelWindowFilter =  Ui_Form() 
        self.modelWindowFilter.DP_TitleLB.setText('Filter')
        self.dataPostProcessingModuleIntiB(filePath, self.modelWindowFilter, model_Name)  
        self.modelWindowFilter.show()

        
    def showAlignCTDWindow(self, filePath, model_Name):   
        self.modelWindowAlign =  Ui_Form()     
        self.modelWindowAlign.DP_TitleLB.setText('Align CTD') 
        self.dataPostProcessingModuleIntiB(filePath, self.modelWindowAlign, model_Name)     
        self.modelWindowAlign.show()

        
    def showLoopEditWindow(self, filePath, model_Name):   
        self.modelWindowLoopEdit =  Ui_Form()    
        self.modelWindowLoopEdit.DP_TitleLB.setText('Loop Edit')
        self.dataPostProcessingModuleIntiB(filePath, self.modelWindowLoopEdit, model_Name)
        self.modelWindowLoopEdit.show()

    def showCellThermalMassWindow(self, filePath, model_Name):
        self.cellThermalMassWindow =  Ui_Form() 
        self.cellThermalMassWindow.DP_TitleLB.setText('Cell Thermal Mass')
        self.dataPostProcessingModuleIntiB(filePath,  self.cellThermalMassWindow, model_Name)
        self.cellThermalMassWindow.show()
       
    def showDriveWindow(self, filePath, model_Name):
        print('I am here in dive window')
        self.driveWindow =  Ui_Form() 
        self.driveWindow.DP_TitleLB.setText('Derive')
        self.dataPostProcessingModuleIntiB(filePath, self.driveWindow, model_Name)
        self.driveWindow.show()


    def showBinAverage(self, filePath, model_Name):
        self.binAverage =  Ui_Form() 
        self.binAverage.DP_TitleLB.setText('Bin Average')
        self.dataPostProcessingModuleIntiB(filePath, self.binAverage, model_Name)
        self.binAverage.show()


    def showBottleSummaryWindow(self, filePath, model_Name):
        self.bottleSummarywindow =  Ui_widget() 
        self.dataPostProcessingModuleIntiA(filePath, self.bottleSummarywindow, model_Name)
        self.bottleSummarywindow.show()
     

    def showDeriveTEOS10Window(self, filePath, model_Name):
        self.driveTEOS10window =  Ui_Form() 
        self.driveTEOS10window.DP_TitleLB.setText('Derive TESO-10')
        self.dataPostProcessingModuleIntiB(filePath, self.driveTEOS10window, model_Name)
        self.driveTEOS10window.show()
     

    def showWildEditWindow(self, filePath, model_Name):
        self.WildEditwindow =  Ui_Form() 
        self.WildEditwindow.DP_TitleLB.setText('Wild Edit')
        self.dataPostProcessingModuleIntiB(filePath, self.WildEditwindow, model_Name)
        self.WildEditwindow.show()

    def dataPostProcessingModuleIntiB(self, filePath, instanceObject, module_name):
        
        instanceObject.DP_SetupFilePB.clicked.connect(lambda: DataPostProcessing.getSystemFilePath(setupFileLE = instanceObject.DP_SetupFileLE, obj = instanceObject))
        instanceObject.DP_InputDirPB.clicked.connect(lambda: DataPostProcessing.getInputDirPath(InputdirLE = instanceObject.DP_InputDirLE, obj = instanceObject ))
        instanceObject.DP_OutputDirPB.clicked.connect(lambda: DataPostProcessing.getOutPutDirpath(OutputdirLE= instanceObject.DP_OutputDirLE, obj= instanceObject))
        instanceObject.DP_InputFileNamePB.clicked.connect(lambda: self.getInputFileName(module_name, InputFileNameLE =instanceObject.DP_InputFileNameLE, obj = instanceObject)) 
        
        instanceObject.DP_InputFileNameLE.textChanged.connect(lambda:self.savePathTagsA(module_name, filePath, parentObj = instanceObject, pathtag = 'inputFIles', value =instanceObject.DP_InputFileNameLE.text()) )
        instanceObject.DP_SetupFileLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = None, pathtag = 'setupFilePath', value =instanceObject.DP_SetupFileLE.text()))       
        instanceObject.DP_InputDirLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath,  parentObj = None, pathtag = 'inputDirectory', value =instanceObject.DP_InputDirLE.text()))
        instanceObject.DP_OutputDirLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath,  parentObj = None, pathtag = 'outPutDir', value =instanceObject.DP_OutputDirLE.text()))
        instanceObject.DP_NameAppendLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = instanceObject, pathtag = 'nameAppend', value =instanceObject.DP_NameAppendLE.text()))
        #instanceObject.DP_SingleFileRB.clicked.connect(lambda: self.savePathTagsA(moduleName,filePath,  parentObj = None, pathtag = 'sigleOrMultipleFile', value ='single'))
        #instanceObject.DP_MultiFileRB.clicked.connect(lambda: self.savePathTagsA(moduleName, filePath,  parentObj = None, pathtag = 'sigleOrMultipleFile', value ='multi'))
        
        instanceObject.DP_SingleFileRB.clicked.connect(lambda: self.singleFile(module_name, filePath , parentObj = instanceObject, pathtag = 'sigleOrMultipleFile', value ='single'))        
        instanceObject.DP_MultiFileRB.clicked.connect(lambda: self.multipleFile(module_name, filePath, parentObj = instanceObject, pathtag = 'sigleOrMultipleFile', value ='multi'))
        instanceObject.DP_OkayPB.clicked.connect(lambda: instanceObject.close())
        instanceObject.DP_CancelPB.clicked.connect(lambda: instanceObject.close())
        self.DP_loadCookiesB(filePath, instanceObject, module_name)

    def dataPostProcessingModuleIntiA(self, filePath, instanceObject, module_name):
        
        instanceObject.DP_InstrumentConfigFilePB.clicked.connect(lambda: DataPostProcessing.getInputConfigFilePath(instanceObject.DP_InstrumentconfigFileLE, obj = instanceObject))
        instanceObject.DP_SetupFilePB.clicked.connect(lambda: DataPostProcessing.getSystemFilePath(setupFileLE = instanceObject.DP_SetupFileLE, obj = instanceObject))
        instanceObject.DP_InputDirPB.clicked.connect(lambda: DataPostProcessing.getInputDirPath(InputdirLE = instanceObject.DP_InputDirLE, obj = instanceObject ))
        instanceObject.DP_OutputDirPB.clicked.connect(lambda: DataPostProcessing.getOutPutDirpath(OutputdirLE= instanceObject.DP_OutputDirLE, obj=instanceObject ))
        instanceObject.DP_InputFileNamePB.clicked.connect(lambda: self.getInputFileName(module_name, InputFileNameLE = instanceObject.DP_InputFileNameLE, obj=instanceObject))
        instanceObject.DP_InputFileNameLE.textChanged.connect(lambda:self.savePathTagsA(module_name, filePath, parentObj = instanceObject, pathtag = 'inputFIles', value =instanceObject.DP_InputFileNameLE.text()) )
        instanceObject.DP_InstrumentconfigFileLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = None, pathtag = 'instrumentconfigPath', value =instanceObject.DP_InstrumentconfigFileLE.text()))
        instanceObject.DP_SetupFileLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = None, pathtag = 'setupFilePath', value =instanceObject.DP_SetupFileLE.text()))       
        instanceObject.DP_InputDirLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = None, pathtag = 'inputDirectory', value =instanceObject.DP_InputDirLE.text()))
        instanceObject.DP_OutputDirLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = None, pathtag = 'outPutDir', value =instanceObject.DP_OutputDirLE.text()))
        instanceObject.DP_OutputFileNameLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = None, pathtag = 'outputFileName', value =instanceObject.DP_OutputFileNameLE.text()))
        instanceObject.DP_NameAppendLE.textChanged.connect(lambda: self.savePathTagsA(module_name, filePath, parentObj = instanceObject, pathtag = 'nameAppend', value =instanceObject.DP_NameAppendLE.text()))

        instanceObject.DP_SingleFileRB.clicked.connect(lambda: self.singleFile(module_name, filePath , parentObj = instanceObject, pathtag = 'sigleOrMultipleFile', value ='single'))        
        instanceObject.DP_MultiFileRB.clicked.connect(lambda: self.multipleFile(module_name, filePath, parentObj = instanceObject, pathtag = 'sigleOrMultipleFile', value ='multi'))
        
        
        instanceObject.DP_CancelPB.clicked.connect(lambda: instanceObject.close())
        if module_name== 'DatCnvW':
            instanceObject.ros_file.clicked.connect(lambda: self.savePathTags_Datcnvw(module_name, filePath, parentObj = None, pathtag = 'ros', value =instanceObject.ros_file.isChecked()))
            self.load_values_to_gui(filePath, module_name, instanceObject)
            instanceObject.DP_OkayPB.clicked.connect(lambda:self.on_ok_pressed(instanceObject.ros_file, instanceObject.DP_SetupFileLE.text()))
            instanceObject.DP_OkayPB.clicked.connect(lambda:self.ros_file_notification(instanceObject.ros_file))
            instanceObject.DP_OkayPB.clicked.connect(lambda: instanceObject.close())
            
        else:
            instanceObject.DP_OkayPB.clicked.connect(lambda: instanceObject.close())
            self.DP_loadCookiesA(filePath, instanceObject, module_name)


    def DP_loadCookiesA(self, filePath, instanceObject, moduleName):
        
        try:
            with open(filePath, 'r', encoding="utf-8")as f:
                tagNameList = ['sigleOrMultipleFile', 'setupFilePath', 'instrumentconfigPath', 'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend', 'outputFileName']
                domObj = minidom.parse(f)
                moduleTag = domObj.getElementsByTagName(moduleName)   
                value = [tag.getElementsByTagName(pathTag)[0].childNodes[0].nodeValue for pathTag in tagNameList for tag in moduleTag]
            
                instanceObject.DP_SetupFileLE.setText(value[1])
                instanceObject.DP_InstrumentconfigFileLE.setText(value[2])
                instanceObject.DP_InputDirLE.setText(value[3])
                instanceObject.DP_InputFileNameLE.setText(value[4])
                instanceObject.DP_OutputDirLE.setText(value[5])
                instanceObject.DP_OutputFileNameLE.setText(value[7])
                instanceObject.DP_NameAppendLE.setText(value[6])
                if value[0] == 'single':
                    instanceObject.DP_SingleFileRB.setChecked(True)
                    
                elif value[0] == 'multi':
                    instanceObject.DP_MultiFileRB.setChecked(True)
                    instanceObject.DP_OutputFileNameLE.setDisabled(True)
                    instanceObject.DP_NameAppendLE.setDisabled(True)
                else:
                    instanceObject.DP_SingleFileRB.setChecked(False)
                    instanceObject.DP_MultiFileRB.setChecked(False)
        except FileNotFoundError:
            print('DP_loadCookiesS : pathInfo.xml file is missing')
        

    def DP_loadCookiesB(self, filePath, instanceObject, moduleName):
        tagNameList = ['sigleOrMultipleFile', 'setupFilePath',  'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend']      
        try:
            with open(filePath, 'r', encoding="utf-8")as f:
                domObj = minidom.parse(f)
                moduleTag = domObj.getElementsByTagName(moduleName)               
                value = [tag.getElementsByTagName(pathTag)[0].childNodes[0].nodeValue for pathTag in tagNameList for tag in moduleTag]
                #files = [file.split('/')[-1] for file in value[3]]
                instanceObject.DP_SetupFileLE.setText(value[1])
                instanceObject.DP_InputDirLE.setText(value[2])
                instanceObject.DP_InputFileNameLE.setText(value[3])
                instanceObject.DP_OutputDirLE.setText(value[4])
                instanceObject.DP_NameAppendLE.setText(value[5])
                if value[0] == 'single':
                    instanceObject.DP_SingleFileRB.setChecked(True)
                elif value[0] == 'multi':
                    instanceObject.DP_MultiFileRB.setChecked(True)
                    instanceObject.DP_OutputFileNameLE.setDisabled(True)
                    instanceObject.DP_NameAppendLE.setDisabled(True)
                else:
                    instanceObject.DP_SingleFileRB.setChecked(False)
                    instanceObject.DP_MultiFileRB.setChecked(False)
        except FileNotFoundError:
            print('The pathInof.xml file is missing')
    


    def savePathTagsA(self, moduleName, filePath, parentObj,  pathtag, value):
        if pathtag == 'inputFIles' and parentObj.DP_InputFileNameLE.text() != 'Nil': parentObj.DP_OutputFileNameLE.setText(parentObj.DP_InputFileNameLE.text().split('.')[0]+'.cnv')
        elif pathtag == 'nameAppend' and parentObj.DP_InputFileNameLE.text() != 'Nil': parentObj.DP_OutputFileNameLE.setText(parentObj.DP_InputFileNameLE.text().split('.')[0]+parentObj.DP_NameAppendLE.text()+'.cnv')            
        try:
            with open(filePath, 'r', encoding="utf-8")as f:
                domObj = minidom.parse(f)
                dataConversion = domObj.getElementsByTagName(moduleName)[0]   
                value = 'No_path' if value == ''   else value   
                dataConversion.getElementsByTagName(pathtag)[0].childNodes[0].nodeValue = value
            with open(filePath, 'w', encoding="utf-8")as f:
                domObj.writexml(f)
                
        except FileNotFoundError:
            print('There are no file named dataPostProcessing.xml is found')

    def outputDataFormat(self, instanceObject):
        if instanceObject.DP_CNV_RB.isChecked():
             with open(instanceObject.DP_SetupFileLE.text(),'r') as f:
                self.xmldoc = minidom.parse(f)        
                self.Data = self.xmldoc.getElementsByTagName('Data_Conversion')[0]
                print(len(self.Data))
        elif instanceObject.DP_ROS_RB.isChecked():
            print('ROS')
        elif instanceObject.DP_CNVROS_RB.isChecked():
            print('CNVROS')

    
    def multipleFile(self, moduleName, filePath, parentObj,  pathtag, value):
        self.savePathTagsA(moduleName, filePath, parentObj,  pathtag, value)
        parentObj.DP_InputFileNameLE.setText("Nil")
        parentObj.DP_OutputFileNameLE.setEnabled(False)
        parentObj.DP_InputFileNameLE.setEnabled(False)
        parentObj.DP_InputFileNamePB.setDisabled(True)

    def singleFile(self, moduleName, filePath, parentObj,  pathtag, value):
        self.savePathTagsA(moduleName, filePath, parentObj,  pathtag, value)
        parentObj.DP_OutputFileNameLE.setEnabled(True)
        parentObj.DP_InputFileNameLE.setEnabled(True)
        parentObj.DP_InputFileNamePB.setDisabled(False)


    def getInputFileName(self, moduleName, InputFileNameLE, obj):
        if not obj.DP_SingleFileRB.isChecked():
            alert = QMessageBox()
            alert.setWindowTitle('Alert')
            alert.setInformativeText('Please select Single File')
            alert.setIcon(QMessageBox.Warning)
            _ = alert.exec()
        else:
            DataPostProcessing.getInputFileName(moduleName, InputFileNameLE, obj )
    
    def load_values_to_gui(self, filePath, moduleName, instanceObject):
        try:
            with open(filePath, 'r', encoding="utf-8")as f:
                tagNameList = ['sigleOrMultipleFile', 'setupFilePath', 'instrumentconfigPath', 'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend', 'outputFileName', 'ros']
                domObj = minidom.parse(f)
                moduleTag = domObj.getElementsByTagName(moduleName)   
                value = [tag.getElementsByTagName(pathTag)[0].childNodes[0].nodeValue for pathTag in tagNameList for tag in moduleTag]
    
                instanceObject.DP_SetupFileLE.setText(value[1])
                instanceObject.DP_InstrumentconfigFileLE.setText(value[2])
                instanceObject.DP_InputDirLE.setText(value[3])
                instanceObject.DP_InputFileNameLE.setText(value[4])
                instanceObject.DP_OutputDirLE.setText(value[5])
                instanceObject.DP_OutputFileNameLE.setText(value[7])
                instanceObject.DP_NameAppendLE.setText(value[6])
                if value[0] == 'single':
                    instanceObject.DP_SingleFileRB.setChecked(True)
                    
                elif value[0] == 'multi':
                    instanceObject.DP_MultiFileRB.setChecked(True)
                    instanceObject.DP_OutputFileNameLE.setDisabled(True)
                    instanceObject.DP_NameAppendLE.setDisabled(True)
                else:
                    instanceObject.DP_SingleFileRB.setChecked(False)
                    instanceObject.DP_MultiFileRB.setChecked(False)
                if value[8] == 'True':
                   
                    instanceObject.ros_file.setChecked(True)
                else:
                    instanceObject.ros_file.setChecked(False)
        except FileNotFoundError:
            print('DP_loadCookiesS : pathInfo.xml file is missing')

    def savePathTags_Datcnvw(self, moduleName, filePath, parentObj,  pathtag, value):
        
        if pathtag == 'inputFIles' and parentObj.DP_InputFileNameLE.text() != 'Nil': parentObj.DP_OutputFileNameLE.setText(parentObj.DP_InputFileNameLE.text().split('.')[0]+'.cnv')
        elif pathtag == 'nameAppend' and parentObj.DP_InputFileNameLE.text() != 'Nil': parentObj.DP_OutputFileNameLE.setText(parentObj.DP_InputFileNameLE.text().split('.')[0]+parentObj.DP_NameAppendLE.text()+'.cnv')            
        try:
            with open(filePath, 'r', encoding="utf-8")as f:
                domObj = minidom.parse(f)
                dataConversion = domObj.getElementsByTagName(moduleName)[0]   
                value = 'No_path' if value == ''   else value   
                dataConversion.getElementsByTagName(pathtag)[0].childNodes[0].nodeValue = value
            with open(filePath, 'w', encoding="utf-8")as f:
                domObj.writexml(f)
                
        except FileNotFoundError:
            print('There are no file named dataPostProcessing.xml is found')

    def on_ok_pressed(self, ros_file, setup_file_path):
        try:
            with open(setup_file_path, 'r')as f:
                if ros_file.isChecked():
                    value= '2'
                else:
                    value = '0'
                domObj = minidom.parse(f)
                domObj.getElementsByTagName('CreateFile')[0].attributes['value'] = value

                with open(setup_file_path, 'w') as nf:
                    domObj.writexml(nf)
            
        except:
            pass

    def ros_file_notification(self, ros_file):
        if ros_file.isChecked():
            alert = QMessageBox()
            alert.setWindowTitle('Alert')
            alert.setInformativeText('You have choosed to created both data file (*.cnv) and bottle file (.ros). \
                Hence, please make sure that *.bl, *.hex, *.hr are located in the same directory')
            alert.setIcon(QMessageBox.Warning)
            _ = alert.exec()




'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataPostProcessingModels()
    window.showDatcnvWindow()
    window.showFilterWindow()
    #window.show()
    sys.exit(app.exec_())'''