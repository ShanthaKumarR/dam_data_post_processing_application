from UI.ui_main import Ui_Form
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QPushButton, QVBoxLayout
import sys
from PyQt5 import QtCore, QtGui
from qt_material import apply_stylesheet
import os
from PyQt5.QtGui import  QIcon
from qt_material import apply_stylesheet, QtStyleTools, list_themes

color_dict = {'dark_amber':'#ffd740', 'dark_blue':'#448aff', 'dark_cyan':'#4dd0e1', 'dark_lightgreen':'#8bc34a', 'dark_pink': '#ff4081', 'dark_purple':'#ab47bc', 'dark_red':'#ff1744',\
        'dark_teal':'#1de9b6', 'dark_yellow':'#ffff00', 'light_blue':'#2979ff', 'light_amber':'#ffc400', 'light_blue_500':'#03a9f4','light_cyan':'#00e5ff', 'light_cyan_500':'#00bcd4','light_lightgreen':'#64dd17', \
        'light_lightgreen_500':'#8bc34a', 'light_orange':'#ff3d00','light_pink':'#ff4081', 'light_pink_500':'#e91e63','light_purple':'#e040fb', 'light_purple_500':'#9c27b0', 'light_red':'#ff1744',\
        'light_red_500':'#f44336', 'light_teal':'#1de9b6', 'light_teal_500':'#009688', 'light_yellow':'#ffea00'}

class View(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.label.installEventFilter(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.prevGeo = self.geometry()
        self.moved = False
        self.theme = 'dark_blue.xml'
        self.set_app_style_sheet(header_color = '#448aff', color = self.theme)
        self.ui.frame.installEventFilter(self)
        
    def ui_controls(self, controller):
        self.ui.DP_DatCnvPB.clicked.connect(lambda: controller.add_standard_item('DatCnvW'))
        self.ui.DP_AlignctdSlBtn.clicked.connect(lambda: controller.add_standard_item('AlignCTDW'))
        self.ui.DP_BinAverageSlBtn.clicked.connect(lambda: controller.add_standard_item('BinAvgW'))
        self.ui.DP_BuoyancySlBtn.clicked.connect(lambda: controller.add_standard_item('BuoyancyW'))
        self.ui.DP_CellThermalMassSlBtn.clicked.connect(lambda: controller.add_standard_item('CellTMW'))
        self.ui.DP_DeriveEOS80SlBtn.clicked.connect(lambda: controller.add_standard_item('DeriveW'))
        self.ui.DP_DeriveTEO10SlBtn.clicked.connect(lambda: controller.add_standard_item('DeriveTEOS_10W'))
        self.ui.DP_FilterSlBtn.clicked.connect(lambda: controller.add_standard_item('FilterW'))
        self.ui.DP_LoopEditSlBtn.clicked.connect(lambda: controller.add_standard_item('LoopEditW'))
        self.ui.DP_WildEditSlBtn.clicked.connect(lambda: controller.add_standard_item('WildEditW'))
        self.ui.DP_WindowFilterSlBtn.clicked.connect(lambda: controller.add_standard_item('W_FilterW'))
        self.ui.DP_MarkScanBtn.clicked.connect(lambda: controller.add_standard_item('MarkScanW'))
        self.ui.DP_moveUpBtn.clicked.connect(partial(controller.moveCurrentRow, controller.UP))
        self.ui.DP_moveDownBtn.clicked.connect(partial(controller.moveCurrentRow, controller.DOWN))
        self.ui.DP_deleteModel.clicked.connect(partial(controller.removeModel))
        self.ui.DP_BottleSummaryBtn.clicked.connect(lambda: controller.add_standard_item('BottleSumW'))
        
        self.ui.DP_save_model.clicked.connect(controller.evnt)
        self.ui.DP_model_temp_CB.currentIndexChanged.connect(lambda:controller.load_table_for_tepmplate(controller.get_info_from_template()))
        self.ui.data_processing_template_delete_PB.clicked.connect(controller.delete_template)
        self.ui.DP_SEBbatchBrowsePB.clicked.connect(controller.getBatchSetupFilePath)
        self.ui.DP_ConvertDataBtn.clicked.connect(controller.prepare_batch_arg)
        self.ui.close_button.clicked.connect(lambda:controller.on_close_run(self.close))
        self.ui.max_button.clicked.connect(self.MaximizeWindow)
        self.ui.min_button.clicked.connect(self.MinimusedWindow)
        self.ui.settings.clicked.connect(self.theme_option)
    
       
    def start_app(self):
        self.show()
        sys.exit(self.app.exec_())

    def MaximizeWindow(self):
        if self.isMaximized():
            self.ui.max_button.setIcon(QIcon(u":/images/images/icon_maximize.png"))
            self.showNormal()
           
        else:
            self.showMaximized()
            self.ui.max_button.setIcon(QIcon(u":/images/images/icon_restore.png"))
           

    def normalWindow(self):
        self.showNormal()

    def MinimusedWindow(self):
        self.showMinimized()
        
    
    def eventFilter(self, obj, event) -> bool:
        
        if obj == self.ui.frame:
            if self.ui.close_button.underMouse():
                    return True
            if self.ui.max_button.underMouse():
                        return True
            if self.ui.min_button.underMouse():
                    return True
            if self.ui.settings.underMouse():
                    return True
            else:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                     if event.globalPos().y() < 10 and self.moved:
                        self.prevGeo = self.geometry()
                        self.showMaximized()
                        return True

                if event.type() == QtCore.QEvent.MouseButtonDblClick:
                    self.setWindowState(self.windowState() ^ QtCore.Qt.WindowFullScreen)
                    return True
                if event.type() == QtCore.QEvent.MouseButtonPress:
                        self.oldPosition = event.globalPos()
                if event.type() == QtCore.QEvent.MouseMove:
                    delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                    self.oldPosition = event.globalPos()
                    self.moved = True
                else:
                    return True
            
        return True


    def theme_option(self):
        self.theme = QDialog()
        Vbox_layout = QVBoxLayout(self.theme)
        Themes = list_themes()
        self.Theme_buttons = [QPushButton(self.theme) for _ in range(len(Themes))]
        [btn.setText(name.split('.')[0]) for btn, name in zip(self.Theme_buttons, Themes)]
        [btn.setObjectName(name.split('.')[0]) for btn, name in zip(self.Theme_buttons, Themes)]
        self.theme_button_color(self.Theme_buttons)
        [Vbox_layout.addWidget(btn)   for btn in self.Theme_buttons]
        [button.clicked.connect(lambda:self.theme_button_clicke_action()) for button in self.Theme_buttons]
        self.theme.exec_()
    
    def theme_button_clicke_action(self):
        self.theme = self.sender().objectName()+'.xml'
        self.selected_theme = color_dict[self.theme.split('.')[0]]
        self.set_app_style_sheet(self.selected_theme, self.theme)
       
    def theme_button_color(self, theme_buttons):
        try:
            [btn.setStyleSheet("background-color: "+ color_dict[btn.objectName()]) for btn in theme_buttons]
        except:
            pass

    def set_app_style_sheet(self, header_color, color):
        self.ui.label.setStyleSheet('background-color:'+header_color)
        extra = {'density_scale': '0',}
        apply_stylesheet(self, color, invert_secondary=True, extra=extra)