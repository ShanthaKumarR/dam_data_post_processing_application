from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"widget")
        self.resize(900, 553)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.DP_TitleLB = QLabel(self.frame_4)
        self.DP_TitleLB.setObjectName(u"DP_TitleLB")

        self.verticalLayout_3.addWidget(self.DP_TitleLB)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DP_SingleFileRB = QRadioButton(self.frame_5)
        self.DP_SingleFileRB.setObjectName(u"DP_SingleFileRB")
        self.DP_SingleFileRB.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.DP_SingleFileRB)

        self.DP_MultiFileRB = QRadioButton(self.frame_5)
        self.DP_MultiFileRB.setObjectName(u"DP_MultiFileRB")
        self.DP_MultiFileRB.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.DP_MultiFileRB)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.DP_SetupFileLab = QLabel(self.frame_5)
        self.DP_SetupFileLab.setObjectName(u"DP_SetupFileLab")

        self.gridLayout.addWidget(self.DP_SetupFileLab, 0, 0, 1, 1)

        self.DP_SetupFileLE = QLineEdit(self.frame_5)
        self.DP_SetupFileLE.setObjectName(u"DP_SetupFileLE")
        self.DP_SetupFileLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_SetupFileLE, 0, 1, 1, 1)

        self.DP_SetupFilePB = QPushButton(self.frame_5)
        self.DP_SetupFilePB.setObjectName(u"DP_SetupFilePB")
        self.DP_SetupFilePB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_SetupFilePB, 0, 2, 1, 1)

        self.DP_InstrumentconfigFileLB = QLabel(self.frame_5)
        self.DP_InstrumentconfigFileLB.setObjectName(u"DP_InstrumentconfigFileLB")

        self.gridLayout.addWidget(self.DP_InstrumentconfigFileLB, 1, 0, 1, 1)

        self.DP_InstrumentconfigFileLE = QLineEdit(self.frame_5)
        self.DP_InstrumentconfigFileLE.setObjectName(u"DP_InstrumentconfigFileLE")
        self.DP_InstrumentconfigFileLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_InstrumentconfigFileLE, 1, 1, 1, 1)

        self.DP_InstrumentConfigFilePB = QPushButton(self.frame_5)
        self.DP_InstrumentConfigFilePB.setObjectName(u"DP_InstrumentConfigFilePB")
        self.DP_InstrumentConfigFilePB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_InstrumentConfigFilePB, 1, 2, 1, 1)

        self.DP_InputDirLB = QLabel(self.frame_5)
        self.DP_InputDirLB.setObjectName(u"DP_InputDirLB")

        self.gridLayout.addWidget(self.DP_InputDirLB, 2, 0, 1, 1)

        self.DP_InputDirLE = QLineEdit(self.frame_5)
        self.DP_InputDirLE.setObjectName(u"DP_InputDirLE")
        self.DP_InputDirLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_InputDirLE, 2, 1, 1, 1)

        self.DP_InputDirPB = QPushButton(self.frame_5)
        self.DP_InputDirPB.setObjectName(u"DP_InputDirPB")
        self.DP_InputDirPB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_InputDirPB, 2, 2, 1, 1)

        self.DP_OutputDirLB = QLabel(self.frame_5)
        self.DP_OutputDirLB.setObjectName(u"DP_OutputDirLB")

        self.gridLayout.addWidget(self.DP_OutputDirLB, 3, 0, 1, 1)

        self.DP_OutputDirLE = QLineEdit(self.frame_5)
        self.DP_OutputDirLE.setObjectName(u"DP_OutputDirLE")
        self.DP_OutputDirLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_OutputDirLE, 3, 1, 1, 1)

        self.DP_OutputDirPB = QPushButton(self.frame_5)
        self.DP_OutputDirPB.setObjectName(u"DP_OutputDirPB")
        self.DP_OutputDirPB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_OutputDirPB, 3, 2, 1, 1)

        self.DP_InputFileNameLB = QLabel(self.frame_5)
        self.DP_InputFileNameLB.setObjectName(u"DP_InputFileNameLB")

        self.gridLayout.addWidget(self.DP_InputFileNameLB, 4, 0, 1, 1)

        self.DP_InputFileNameLE = QLineEdit(self.frame_5)
        self.DP_InputFileNameLE.setObjectName(u"DP_InputFileNameLE")
        self.DP_InputFileNameLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_InputFileNameLE, 4, 1, 1, 1)

        self.DP_InputFileNamePB = QPushButton(self.frame_5)
        self.DP_InputFileNamePB.setObjectName(u"DP_InputFileNamePB")
        self.DP_InputFileNamePB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_InputFileNamePB, 4, 2, 1, 1)

        self.DP_NameAppendLabel = QLabel(self.frame_5)
        self.DP_NameAppendLabel.setObjectName(u"DP_NameAppendLabel")

        self.gridLayout.addWidget(self.DP_NameAppendLabel, 5, 0, 1, 1)

        self.DP_NameAppendLE = QLineEdit(self.frame_5)
        self.DP_NameAppendLE.setObjectName(u"DP_NameAppendLE")
        self.DP_NameAppendLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_NameAppendLE, 5, 1, 1, 1)

        self.DP_OutputFileName = QLabel(self.frame_5)
        self.DP_OutputFileName.setObjectName(u"DP_OutputFileName")

        self.gridLayout.addWidget(self.DP_OutputFileName, 6, 0, 1, 1)

        self.DP_OutputFileNameLE = QLineEdit(self.frame_5)
        self.DP_OutputFileNameLE.setObjectName(u"DP_OutputFileNameLE")
        self.DP_OutputFileNameLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_OutputFileNameLE, 6, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.DP_CancelPB = QPushButton(self.frame_3)
        self.DP_CancelPB.setObjectName(u"DP_CancelPB")
        self.DP_CancelPB.setMinimumSize(QSize(75, 25))
        self.DP_CancelPB.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.DP_CancelPB)

        self.DP_OkayPB = QPushButton(self.frame_3)
        self.DP_OkayPB.setObjectName(u"DP_OkayPB")
        self.DP_OkayPB.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_2.addWidget(self.DP_OkayPB)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)
        #self.ros_file = None

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.DP_TitleLB.setText(QCoreApplication.translate("widget", u"Template A", None))
        self.DP_SingleFileRB.setText(QCoreApplication.translate("widget", u"singleFile", None))
        self.DP_MultiFileRB.setText(QCoreApplication.translate("widget", u"Multiple file", None))
        self.DP_SetupFileLab.setText(QCoreApplication.translate("widget", u"Program set up file ", None))
        self.DP_SetupFilePB.setText(QCoreApplication.translate("widget", u"Browse", None))
        self.DP_InstrumentconfigFileLB.setText(QCoreApplication.translate("widget", u"Instrument config file", None))
        self.DP_InstrumentConfigFilePB.setText(QCoreApplication.translate("widget", u"Browse", None))
        self.DP_InputDirLB.setText(QCoreApplication.translate("widget", u"Input directory", None))
        self.DP_InputDirPB.setText(QCoreApplication.translate("widget", u"Browse", None))
        self.DP_OutputDirLB.setText(QCoreApplication.translate("widget", u"Output directory", None))
        self.DP_OutputDirPB.setText(QCoreApplication.translate("widget", u"Browse", None))
        self.DP_InputFileNameLB.setText(QCoreApplication.translate("widget", u"Input File", None))
        self.DP_InputFileNamePB.setText(QCoreApplication.translate("widget", u"Browse", None))
        self.DP_NameAppendLabel.setText(QCoreApplication.translate("widget", u"Name Append", None))
        self.DP_OutputFileName.setText(QCoreApplication.translate("widget", u"Output File Name ", None))
        self.DP_CancelPB.setText(QCoreApplication.translate("widget", u"Cancel", None))
        self.DP_OkayPB.setText(QCoreApplication.translate("widget", u"OK", None))
    # retranslateUi

