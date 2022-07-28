from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from UI import icons



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 855)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setLineWidth(1)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")
        self.settings.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/images/images/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon)

        self.horizontalLayout.addWidget(self.settings)

        self.min_button = QPushButton(self.widget)
        self.min_button.setObjectName(u"min_button")
        self.min_button.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.min_button)

        self.max_button = QPushButton(self.widget)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.max_button)

        self.close_button = QPushButton(self.widget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout_5.addWidget(self.widget, 0, Qt.AlignRight)


        self.horizontalLayout_4.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.header)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.Data_processing_temp_label = QLabel(self.frame_11)
        self.Data_processing_temp_label.setObjectName(u"Data_processing_temp_label")
        font1 = QFont()
        font1.setPointSize(13)
        self.Data_processing_temp_label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.Data_processing_temp_label)

        self.DP_model_temp_CB = QComboBox(self.frame_11)
        self.DP_model_temp_CB.setObjectName(u"DP_model_temp_CB")

        self.horizontalLayout_10.addWidget(self.DP_model_temp_CB)

        self.data_processing_template_delete_PB = QPushButton(self.frame_11)
        self.data_processing_template_delete_PB.setObjectName(u"data_processing_template_delete_PB")

        self.horizontalLayout_10.addWidget(self.data_processing_template_delete_PB)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_32 = QFrame(self.frame)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_32)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(200, 16777215))
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_35)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(9, 9, 9, -1)
        self.DP_DatCnvPB = QPushButton(self.frame_35)
        self.DP_DatCnvPB.setObjectName(u"DP_DatCnvPB")
        self.DP_DatCnvPB.setMinimumSize(QSize(185, 0))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.DP_DatCnvPB.setFont(font2)
        self.DP_DatCnvPB.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_DatCnvPB, 0, Qt.AlignLeft)

        self.DP_BottleSummaryBtn = QPushButton(self.frame_35)
        self.DP_BottleSummaryBtn.setObjectName(u"DP_BottleSummaryBtn")
        self.DP_BottleSummaryBtn.setMinimumSize(QSize(185, 0))
        self.DP_BottleSummaryBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_BottleSummaryBtn.setFont(font2)
        self.DP_BottleSummaryBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_BottleSummaryBtn, 0, Qt.AlignLeft)

        self.DP_MarkScanBtn = QPushButton(self.frame_35)
        self.DP_MarkScanBtn.setObjectName(u"DP_MarkScanBtn")
        self.DP_MarkScanBtn.setMinimumSize(QSize(185, 0))
        self.DP_MarkScanBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_MarkScanBtn.setFont(font2)
        self.DP_MarkScanBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_MarkScanBtn, 0, Qt.AlignLeft)

        self.DP_BuoyancySlBtn = QPushButton(self.frame_35)
        self.DP_BuoyancySlBtn.setObjectName(u"DP_BuoyancySlBtn")
        self.DP_BuoyancySlBtn.setMinimumSize(QSize(185, 0))
        self.DP_BuoyancySlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_BuoyancySlBtn.setFont(font2)
        self.DP_BuoyancySlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_BuoyancySlBtn, 0, Qt.AlignLeft)

        self.DP_BinAverageSlBtn = QPushButton(self.frame_35)
        self.DP_BinAverageSlBtn.setObjectName(u"DP_BinAverageSlBtn")
        self.DP_BinAverageSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_BinAverageSlBtn.setFont(font2)
        self.DP_BinAverageSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_BinAverageSlBtn, 0, Qt.AlignLeft)

        self.DP_WindowFilterSlBtn = QPushButton(self.frame_35)
        self.DP_WindowFilterSlBtn.setObjectName(u"DP_WindowFilterSlBtn")
        self.DP_WindowFilterSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_WindowFilterSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_WindowFilterSlBtn.setFont(font2)
        self.DP_WindowFilterSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_WindowFilterSlBtn, 0, Qt.AlignLeft)

        self.DP_AlignctdSlBtn = QPushButton(self.frame_35)
        self.DP_AlignctdSlBtn.setObjectName(u"DP_AlignctdSlBtn")
        self.DP_AlignctdSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_AlignctdSlBtn.setMaximumSize(QSize(250, 16777215))
        self.DP_AlignctdSlBtn.setFont(font2)
        self.DP_AlignctdSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_AlignctdSlBtn, 0, Qt.AlignLeft)

        self.DP_LoopEditSlBtn = QPushButton(self.frame_35)
        self.DP_LoopEditSlBtn.setObjectName(u"DP_LoopEditSlBtn")
        self.DP_LoopEditSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_LoopEditSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_LoopEditSlBtn.setFont(font2)
        self.DP_LoopEditSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_LoopEditSlBtn, 0, Qt.AlignLeft)

        self.DP_WildEditSlBtn = QPushButton(self.frame_35)
        self.DP_WildEditSlBtn.setObjectName(u"DP_WildEditSlBtn")
        self.DP_WildEditSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_WildEditSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_WildEditSlBtn.setFont(font2)
        self.DP_WildEditSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_WildEditSlBtn, 0, Qt.AlignLeft)

        self.DP_FilterSlBtn = QPushButton(self.frame_35)
        self.DP_FilterSlBtn.setObjectName(u"DP_FilterSlBtn")
        self.DP_FilterSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_FilterSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_FilterSlBtn.setFont(font2)
        self.DP_FilterSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_FilterSlBtn, 0, Qt.AlignLeft)

        self.DP_CellThermalMassSlBtn = QPushButton(self.frame_35)
        self.DP_CellThermalMassSlBtn.setObjectName(u"DP_CellThermalMassSlBtn")
        self.DP_CellThermalMassSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_CellThermalMassSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_CellThermalMassSlBtn.setFont(font2)
        self.DP_CellThermalMassSlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_CellThermalMassSlBtn, 0, Qt.AlignLeft)

        self.DP_DeriveTEO10SlBtn = QPushButton(self.frame_35)
        self.DP_DeriveTEO10SlBtn.setObjectName(u"DP_DeriveTEO10SlBtn")
        self.DP_DeriveTEO10SlBtn.setMinimumSize(QSize(185, 0))
        self.DP_DeriveTEO10SlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_DeriveTEO10SlBtn.setFont(font2)
        self.DP_DeriveTEO10SlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_DeriveTEO10SlBtn, 0, Qt.AlignLeft)

        self.DP_DeriveEOS80SlBtn = QPushButton(self.frame_35)
        self.DP_DeriveEOS80SlBtn.setObjectName(u"DP_DeriveEOS80SlBtn")
        self.DP_DeriveEOS80SlBtn.setMinimumSize(QSize(185, 0))
        self.DP_DeriveEOS80SlBtn.setMaximumSize(QSize(185, 16777215))
        self.DP_DeriveEOS80SlBtn.setFont(font2)
        self.DP_DeriveEOS80SlBtn.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.DP_DeriveEOS80SlBtn, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_35)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_40 = QFrame(self.frame_32)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.DP_TableView = QTableView(self.frame_40)
        self.DP_TableView.setObjectName(u"DP_TableView")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DP_TableView.sizePolicy().hasHeightForWidth())
        self.DP_TableView.setSizePolicy(sizePolicy)
        self.DP_TableView.setMinimumSize(QSize(0, 500))

        self.verticalLayout_3.addWidget(self.DP_TableView)


        self.verticalLayout_4.addWidget(self.frame_40)

        self.frame_44 = QFrame(self.frame_32)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.DP_moveUpBtn = QPushButton(self.frame_44)
        self.DP_moveUpBtn.setObjectName(u"DP_moveUpBtn")
        self.DP_moveUpBtn.setFont(font2)
        self.DP_moveUpBtn.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.DP_moveUpBtn)

        self.DP_moveDownBtn = QPushButton(self.frame_44)
        self.DP_moveDownBtn.setObjectName(u"DP_moveDownBtn")
        self.DP_moveDownBtn.setMaximumSize(QSize(16777215, 35))
        self.DP_moveDownBtn.setFont(font2)
        self.DP_moveDownBtn.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.DP_moveDownBtn)

        self.DP_deleteModel = QPushButton(self.frame_44)
        self.DP_deleteModel.setObjectName(u"DP_deleteModel")
        self.DP_deleteModel.setFont(font2)
        self.DP_deleteModel.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.DP_deleteModel)

        self.DP_save_model = QPushButton(self.frame_44)
        self.DP_save_model.setObjectName(u"DP_save_model")
        self.DP_save_model.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.DP_save_model)


        self.verticalLayout_4.addWidget(self.frame_44)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.frame_32)

        self.frame_41 = QFrame(self.frame)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.DP_SEBbatchLB = QLabel(self.frame_41)
        self.DP_SEBbatchLB.setObjectName(u"DP_SEBbatchLB")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.DP_SEBbatchLB.setFont(font3)

        self.horizontalLayout_2.addWidget(self.DP_SEBbatchLB)

        self.DP_SEBbatchLE = QLineEdit(self.frame_41)
        self.DP_SEBbatchLE.setObjectName(u"DP_SEBbatchLE")
        self.DP_SEBbatchLE.setMinimumSize(QSize(0, 0))
        self.DP_SEBbatchLE.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.DP_SEBbatchLE)

        self.DP_SEBbatchBrowsePB = QPushButton(self.frame_41)
        self.DP_SEBbatchBrowsePB.setObjectName(u"DP_SEBbatchBrowsePB")
        self.DP_SEBbatchBrowsePB.setMinimumSize(QSize(0, 0))
        self.DP_SEBbatchBrowsePB.setFont(font2)
        self.DP_SEBbatchBrowsePB.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.DP_SEBbatchBrowsePB)

        self.DP_ConvertDataBtn = QPushButton(self.frame_41)
        self.DP_ConvertDataBtn.setObjectName(u"DP_ConvertDataBtn")
        self.DP_ConvertDataBtn.setMinimumSize(QSize(0, 0))
        self.DP_ConvertDataBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_ConvertDataBtn.setFont(font2)
        self.DP_ConvertDataBtn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.DP_ConvertDataBtn)


        self.verticalLayout_2.addWidget(self.frame_41)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Post Processing", None))
        self.settings.setText("")
        self.min_button.setText("")
        self.max_button.setText("")
        self.close_button.setText("")
        self.Data_processing_temp_label.setText(QCoreApplication.translate("MainWindow", u"Data Processing template", None))
        self.data_processing_template_delete_PB.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.DP_DatCnvPB.setText(QCoreApplication.translate("MainWindow", u"DatCnv", None))
        self.DP_BottleSummaryBtn.setText(QCoreApplication.translate("MainWindow", u"Bottle Summary", None))
        self.DP_MarkScanBtn.setText(QCoreApplication.translate("MainWindow", u"Mark Scan", None))
        self.DP_BuoyancySlBtn.setText(QCoreApplication.translate("MainWindow", u"Buoyancy", None))
        self.DP_BinAverageSlBtn.setText(QCoreApplication.translate("MainWindow", u"Bin Average", None))
        self.DP_WindowFilterSlBtn.setText(QCoreApplication.translate("MainWindow", u"Window Filter", None))
        self.DP_AlignctdSlBtn.setText(QCoreApplication.translate("MainWindow", u"Align CTD", None))
        self.DP_LoopEditSlBtn.setText(QCoreApplication.translate("MainWindow", u"Loop Edit", None))
        self.DP_WildEditSlBtn.setText(QCoreApplication.translate("MainWindow", u"Wild Edit", None))
        self.DP_FilterSlBtn.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.DP_CellThermalMassSlBtn.setText(QCoreApplication.translate("MainWindow", u"Cell Thermal Mass", None))
        self.DP_DeriveTEO10SlBtn.setText(QCoreApplication.translate("MainWindow", u"Derive TEOS-10", None))
        self.DP_DeriveEOS80SlBtn.setText(QCoreApplication.translate("MainWindow", u"Derive - EOS-80 ", None))
        self.DP_moveUpBtn.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.DP_moveDownBtn.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.DP_deleteModel.setText(QCoreApplication.translate("MainWindow", u"Delete Model", None))
        self.DP_save_model.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.DP_SEBbatchLB.setText(QCoreApplication.translate("MainWindow", u"SEBbatch setup file(.exe)", None))
        self.DP_SEBbatchBrowsePB.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.DP_ConvertDataBtn.setText(QCoreApplication.translate("MainWindow", u"Process Data", None))
    # retranslateUi





