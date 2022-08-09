from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from UI import icons




class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(987, 862)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(Form)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settings = QPushButton(self.frame)
        self.settings.setObjectName(u"settings")
        self.settings.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/images/images/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon)

        self.horizontalLayout.addWidget(self.settings)

        self.min_button = QPushButton(self.frame)
        self.min_button.setObjectName(u"min_button")
        self.min_button.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.min_button)

        self.max_button = QPushButton(self.frame)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.max_button)

        self.close_button = QPushButton(self.frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.close_button)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)


        self.verticalLayout_9.addWidget(self.frame)

        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 0, 9, 9)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.DP_DatCnvPB = QPushButton(self.groupBox)
        self.DP_DatCnvPB.setObjectName(u"DP_DatCnvPB")
        self.DP_DatCnvPB.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.DP_DatCnvPB.setFont(font1)
        self.DP_DatCnvPB.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_DatCnvPB)

        self.DP_BottleSummaryBtn = QPushButton(self.groupBox)
        self.DP_BottleSummaryBtn.setObjectName(u"DP_BottleSummaryBtn")
        self.DP_BottleSummaryBtn.setMinimumSize(QSize(0, 0))
        self.DP_BottleSummaryBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_BottleSummaryBtn.setFont(font1)
        self.DP_BottleSummaryBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_BottleSummaryBtn)

        self.DP_MarkScanBtn = QPushButton(self.groupBox)
        self.DP_MarkScanBtn.setObjectName(u"DP_MarkScanBtn")
        self.DP_MarkScanBtn.setMinimumSize(QSize(0, 0))
        self.DP_MarkScanBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_MarkScanBtn.setFont(font1)
        self.DP_MarkScanBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_MarkScanBtn)

        self.DP_BuoyancySlBtn = QPushButton(self.groupBox)
        self.DP_BuoyancySlBtn.setObjectName(u"DP_BuoyancySlBtn")
        self.DP_BuoyancySlBtn.setMinimumSize(QSize(0, 0))
        self.DP_BuoyancySlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_BuoyancySlBtn.setFont(font1)
        self.DP_BuoyancySlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_BuoyancySlBtn)

        self.DP_BinAverageSlBtn = QPushButton(self.groupBox)
        self.DP_BinAverageSlBtn.setObjectName(u"DP_BinAverageSlBtn")
        self.DP_BinAverageSlBtn.setMinimumSize(QSize(0, 0))
        self.DP_BinAverageSlBtn.setFont(font1)
        self.DP_BinAverageSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_BinAverageSlBtn)

        self.DP_WindowFilterSlBtn = QPushButton(self.groupBox)
        self.DP_WindowFilterSlBtn.setObjectName(u"DP_WindowFilterSlBtn")
        self.DP_WindowFilterSlBtn.setMinimumSize(QSize(0, 0))
        self.DP_WindowFilterSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_WindowFilterSlBtn.setFont(font1)
        self.DP_WindowFilterSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_WindowFilterSlBtn)

        self.DP_AlignctdSlBtn = QPushButton(self.groupBox)
        self.DP_AlignctdSlBtn.setObjectName(u"DP_AlignctdSlBtn")
        self.DP_AlignctdSlBtn.setMinimumSize(QSize(185, 0))
        self.DP_AlignctdSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_AlignctdSlBtn.setFont(font1)
        self.DP_AlignctdSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_AlignctdSlBtn)

        self.DP_LoopEditSlBtn = QPushButton(self.groupBox)
        self.DP_LoopEditSlBtn.setObjectName(u"DP_LoopEditSlBtn")
        self.DP_LoopEditSlBtn.setMinimumSize(QSize(0, 0))
        self.DP_LoopEditSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_LoopEditSlBtn.setFont(font1)
        self.DP_LoopEditSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_LoopEditSlBtn)

        self.DP_WildEditSlBtn = QPushButton(self.groupBox)
        self.DP_WildEditSlBtn.setObjectName(u"DP_WildEditSlBtn")
        self.DP_WildEditSlBtn.setMinimumSize(QSize(0, 0))
        self.DP_WildEditSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_WildEditSlBtn.setFont(font1)
        self.DP_WildEditSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_WildEditSlBtn)

        self.DP_FilterSlBtn = QPushButton(self.groupBox)
        self.DP_FilterSlBtn.setObjectName(u"DP_FilterSlBtn")
        self.DP_FilterSlBtn.setMinimumSize(QSize(0, 0))
        self.DP_FilterSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_FilterSlBtn.setFont(font1)
        self.DP_FilterSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_FilterSlBtn)

        self.DP_CellThermalMassSlBtn = QPushButton(self.groupBox)
        self.DP_CellThermalMassSlBtn.setObjectName(u"DP_CellThermalMassSlBtn")
        self.DP_CellThermalMassSlBtn.setMinimumSize(QSize(0, 0))
        self.DP_CellThermalMassSlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_CellThermalMassSlBtn.setFont(font1)
        self.DP_CellThermalMassSlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_CellThermalMassSlBtn)

        self.DP_DeriveTEO10SlBtn = QPushButton(self.groupBox)
        self.DP_DeriveTEO10SlBtn.setObjectName(u"DP_DeriveTEO10SlBtn")
        self.DP_DeriveTEO10SlBtn.setMinimumSize(QSize(0, 0))
        self.DP_DeriveTEO10SlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_DeriveTEO10SlBtn.setFont(font1)
        self.DP_DeriveTEO10SlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_DeriveTEO10SlBtn)

        self.DP_DeriveEOS80SlBtn = QPushButton(self.groupBox)
        self.DP_DeriveEOS80SlBtn.setObjectName(u"DP_DeriveEOS80SlBtn")
        self.DP_DeriveEOS80SlBtn.setMinimumSize(QSize(0, 0))
        self.DP_DeriveEOS80SlBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_DeriveEOS80SlBtn.setFont(font1)
        self.DP_DeriveEOS80SlBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DP_DeriveEOS80SlBtn)


        self.verticalLayout_7.addLayout(self.verticalLayout)


        self.horizontalLayout_9.addWidget(self.groupBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Data_processing_temp_label = QLabel(self.groupBox_5)
        self.Data_processing_temp_label.setObjectName(u"Data_processing_temp_label")
        font2 = QFont()
        font2.setPointSize(8)
        self.Data_processing_temp_label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.Data_processing_temp_label)

        self.DP_model_temp_CB = QComboBox(self.groupBox_5)
        self.DP_model_temp_CB.setObjectName(u"DP_model_temp_CB")

        self.horizontalLayout_4.addWidget(self.DP_model_temp_CB)

        self.data_processing_template_delete_PB = QPushButton(self.groupBox_5)
        self.data_processing_template_delete_PB.setObjectName(u"data_processing_template_delete_PB")

        self.horizontalLayout_4.addWidget(self.data_processing_template_delete_PB)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 9)
        self.DP_TableView = QTableView(self.groupBox_2)
        self.DP_TableView.setObjectName(u"DP_TableView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.DP_TableView.sizePolicy().hasHeightForWidth())
        self.DP_TableView.setSizePolicy(sizePolicy3)
        self.DP_TableView.setMinimumSize(QSize(0, 500))
        self.DP_TableView.horizontalHeader().setVisible(False)
        self.DP_TableView.verticalHeader().setVisible(False)
        self.DP_TableView.verticalHeader().setHighlightSections(False)

        self.verticalLayout_5.addWidget(self.DP_TableView)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.DP_moveUpBtn = QPushButton(self.groupBox_3)
        self.DP_moveUpBtn.setObjectName(u"DP_moveUpBtn")
        self.DP_moveUpBtn.setFont(font1)
        self.DP_moveUpBtn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.DP_moveUpBtn)

        self.DP_moveDownBtn = QPushButton(self.groupBox_3)
        self.DP_moveDownBtn.setObjectName(u"DP_moveDownBtn")
        self.DP_moveDownBtn.setMaximumSize(QSize(16777215, 35))
        self.DP_moveDownBtn.setFont(font1)
        self.DP_moveDownBtn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.DP_moveDownBtn)

        self.DP_deleteModel = QPushButton(self.groupBox_3)
        self.DP_deleteModel.setObjectName(u"DP_deleteModel")
        self.DP_deleteModel.setFont(font1)
        self.DP_deleteModel.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.DP_deleteModel)

        self.DP_save_model = QPushButton(self.groupBox_3)
        self.DP_save_model.setObjectName(u"DP_save_model")
        self.DP_save_model.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.DP_save_model)


        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.groupBox_4 = QGroupBox(self.groupBox_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.DP_SEBbatchLB = QLabel(self.groupBox_4)
        self.DP_SEBbatchLB.setObjectName(u"DP_SEBbatchLB")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.DP_SEBbatchLB.setFont(font3)

        self.horizontalLayout_5.addWidget(self.DP_SEBbatchLB)

        self.DP_SEBbatchLE = QLineEdit(self.groupBox_4)
        self.DP_SEBbatchLE.setObjectName(u"DP_SEBbatchLE")
        self.DP_SEBbatchLE.setMinimumSize(QSize(0, 0))
        self.DP_SEBbatchLE.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.DP_SEBbatchLE)

        self.DP_SEBbatchBrowsePB = QPushButton(self.groupBox_4)
        self.DP_SEBbatchBrowsePB.setObjectName(u"DP_SEBbatchBrowsePB")
        self.DP_SEBbatchBrowsePB.setMinimumSize(QSize(0, 0))
        self.DP_SEBbatchBrowsePB.setFont(font1)
        self.DP_SEBbatchBrowsePB.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.DP_SEBbatchBrowsePB)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.DP_ConvertDataBtn = QPushButton(self.groupBox_4)
        self.DP_ConvertDataBtn.setObjectName(u"DP_ConvertDataBtn")
        self.DP_ConvertDataBtn.setMinimumSize(QSize(0, 0))
        self.DP_ConvertDataBtn.setMaximumSize(QSize(16777215, 16777215))
        self.DP_ConvertDataBtn.setFont(font1)
        self.DP_ConvertDataBtn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.DP_ConvertDataBtn)


        self.verticalLayout_6.addWidget(self.groupBox_4)


        self.verticalLayout_9.addWidget(self.groupBox_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setMaximumSize(QSize(16, 16))
        self.widget.setStyleSheet(u"background-image: url(:/images/images/cil-size-grip.png);")

        self.horizontalLayout_7.addWidget(self.widget)
        QSizeGrip(self.widget)

        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.settings.setToolTip('App settings')
       
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data Post Processing", None))
        self.settings.setText("")
        self.min_button.setText("")
        self.max_button.setText("")
        self.close_button.setText("")
        self.groupBox_6.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Modules", None))
        self.DP_DatCnvPB.setText(QCoreApplication.translate("Form", u"DatCnv", None))
        self.DP_BottleSummaryBtn.setText(QCoreApplication.translate("Form", u"Bottle Summary", None))
        self.DP_MarkScanBtn.setText(QCoreApplication.translate("Form", u"Mark Scan", None))
        self.DP_BuoyancySlBtn.setText(QCoreApplication.translate("Form", u"Buoyancy", None))
        self.DP_BinAverageSlBtn.setText(QCoreApplication.translate("Form", u"Bin Average", None))
        self.DP_WindowFilterSlBtn.setText(QCoreApplication.translate("Form", u"Window Filter", None))
        self.DP_AlignctdSlBtn.setText(QCoreApplication.translate("Form", u"Align CTD", None))
        self.DP_LoopEditSlBtn.setText(QCoreApplication.translate("Form", u"Loop Edit", None))
        self.DP_WildEditSlBtn.setText(QCoreApplication.translate("Form", u"Wild Edit", None))
        self.DP_FilterSlBtn.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.DP_CellThermalMassSlBtn.setText(QCoreApplication.translate("Form", u"Cell Thermal Mass", None))
        self.DP_DeriveTEO10SlBtn.setText(QCoreApplication.translate("Form", u"Derive TEOS-10", None))
        self.DP_DeriveEOS80SlBtn.setText(QCoreApplication.translate("Form", u"Derive - EOS-80 ", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Saved sequence", None))
        self.Data_processing_temp_label.setText(QCoreApplication.translate("Form", u"Data Processing template", None))
        self.data_processing_template_delete_PB.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Controls", None))
        self.DP_moveUpBtn.setText(QCoreApplication.translate("Form", u"Move Up", None))
        self.DP_moveDownBtn.setText(QCoreApplication.translate("Form", u"Move Down", None))
        self.DP_deleteModel.setText(QCoreApplication.translate("Form", u"Delete Model", None))
        self.DP_save_model.setText(QCoreApplication.translate("Form", u"Save", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.DP_SEBbatchLB.setText(QCoreApplication.translate("Form", u"SEBbatch setup file folder", None))
        self.DP_SEBbatchBrowsePB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.DP_ConvertDataBtn.setText(QCoreApplication.translate("Form", u"Process Data", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DAM-IOW-Data Post Processing-V1.00", None))
    # retranslateUi







