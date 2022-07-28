from UI.ui_main import Ui_MainWindow
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtCore, QtGui
from qt_material import apply_stylesheet
import os

class View(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.my_style = """

        QMainWindow{backgroound: #262D37;}
        
        """
        #self.app.setStyleSheet(self.my_style)
        QMainWindow.__init__(self)
        #Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.header.setStyleSheet('background-color: #448aff')
        self.ui.header.installEventFilter(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.prevGeo = self.geometry()
        self.moved = False
        extra = {'density_scale': '0',}
        
        apply_stylesheet(self.app, 'dark_blue.xml', invert_secondary=True, extra=extra)
        stylesheet = self.app.styleSheet()
        with open('UI\\new_stylesheet.css') as file:
            self.app.setStyleSheet(stylesheet + file.read().format(**os.environ))
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

    def eventFilter(self, obj, event) -> bool:
        
        if obj == self.ui.header:
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
       
    def start_app(self):
        self.show()
        sys.exit(self.app.exec_())

    def MaximizeWindow(self):
        if self.isMaximized():
            self.showNormal()
           
        else:
            self.showMaximized()
           

    def normalWindow(self):
        self.showNormal()

    def MinimusedWindow(self):
        self.showMinimized()
           