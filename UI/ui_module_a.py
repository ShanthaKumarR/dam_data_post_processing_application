from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(578, 361)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DP_SingleFileRB = QRadioButton(self.groupBox)
        self.DP_SingleFileRB.setObjectName(u"DP_SingleFileRB")
        self.DP_SingleFileRB.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.DP_SingleFileRB)

        self.DP_MultiFileRB = QRadioButton(self.groupBox)
        self.DP_MultiFileRB.setObjectName(u"DP_MultiFileRB")
        self.DP_MultiFileRB.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.DP_MultiFileRB)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.DP_SetupFileLab = QLabel(self.groupBox)
        self.DP_SetupFileLab.setObjectName(u"DP_SetupFileLab")

        self.gridLayout.addWidget(self.DP_SetupFileLab, 0, 0, 1, 1)

        self.DP_SetupFileLE = QLineEdit(self.groupBox)
        self.DP_SetupFileLE.setObjectName(u"DP_SetupFileLE")
        self.DP_SetupFileLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_SetupFileLE, 0, 1, 1, 1)

        self.DP_SetupFilePB = QPushButton(self.groupBox)
        self.DP_SetupFilePB.setObjectName(u"DP_SetupFilePB")
        self.DP_SetupFilePB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_SetupFilePB, 0, 2, 1, 1)

        self.DP_InstrumentconfigFileLB = QLabel(self.groupBox)
        self.DP_InstrumentconfigFileLB.setObjectName(u"DP_InstrumentconfigFileLB")

        self.gridLayout.addWidget(self.DP_InstrumentconfigFileLB, 1, 0, 1, 1)

        self.DP_InstrumentconfigFileLE = QLineEdit(self.groupBox)
        self.DP_InstrumentconfigFileLE.setObjectName(u"DP_InstrumentconfigFileLE")
        self.DP_InstrumentconfigFileLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_InstrumentconfigFileLE, 1, 1, 1, 1)

        self.DP_InstrumentConfigFilePB = QPushButton(self.groupBox)
        self.DP_InstrumentConfigFilePB.setObjectName(u"DP_InstrumentConfigFilePB")
        self.DP_InstrumentConfigFilePB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_InstrumentConfigFilePB, 1, 2, 1, 1)

        self.DP_InputDirLB = QLabel(self.groupBox)
        self.DP_InputDirLB.setObjectName(u"DP_InputDirLB")

        self.gridLayout.addWidget(self.DP_InputDirLB, 2, 0, 1, 1)

        self.DP_InputDirLE = QLineEdit(self.groupBox)
        self.DP_InputDirLE.setObjectName(u"DP_InputDirLE")
        self.DP_InputDirLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_InputDirLE, 2, 1, 1, 1)

        self.DP_InputDirPB = QPushButton(self.groupBox)
        self.DP_InputDirPB.setObjectName(u"DP_InputDirPB")
        self.DP_InputDirPB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_InputDirPB, 2, 2, 1, 1)

        self.DP_OutputDirLB = QLabel(self.groupBox)
        self.DP_OutputDirLB.setObjectName(u"DP_OutputDirLB")

        self.gridLayout.addWidget(self.DP_OutputDirLB, 3, 0, 1, 1)

        self.DP_OutputDirLE = QLineEdit(self.groupBox)
        self.DP_OutputDirLE.setObjectName(u"DP_OutputDirLE")
        self.DP_OutputDirLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_OutputDirLE, 3, 1, 1, 1)

        self.DP_OutputDirPB = QPushButton(self.groupBox)
        self.DP_OutputDirPB.setObjectName(u"DP_OutputDirPB")
        self.DP_OutputDirPB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_OutputDirPB, 3, 2, 1, 1)

        self.DP_InputFileNameLB = QLabel(self.groupBox)
        self.DP_InputFileNameLB.setObjectName(u"DP_InputFileNameLB")

        self.gridLayout.addWidget(self.DP_InputFileNameLB, 4, 0, 1, 1)

        self.DP_InputFileNameLE = QLineEdit(self.groupBox)
        self.DP_InputFileNameLE.setObjectName(u"DP_InputFileNameLE")
        self.DP_InputFileNameLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_InputFileNameLE, 4, 1, 1, 1)

        self.DP_InputFileNamePB = QPushButton(self.groupBox)
        self.DP_InputFileNamePB.setObjectName(u"DP_InputFileNamePB")
        self.DP_InputFileNamePB.setMinimumSize(QSize(75, 25))

        self.gridLayout.addWidget(self.DP_InputFileNamePB, 4, 2, 1, 1)

        self.DP_NameAppendLabel = QLabel(self.groupBox)
        self.DP_NameAppendLabel.setObjectName(u"DP_NameAppendLabel")

        self.gridLayout.addWidget(self.DP_NameAppendLabel, 5, 0, 1, 1)

        self.DP_NameAppendLE = QLineEdit(self.groupBox)
        self.DP_NameAppendLE.setObjectName(u"DP_NameAppendLE")
        self.DP_NameAppendLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_NameAppendLE, 5, 1, 1, 1)

        self.DP_OutputFileName = QLabel(self.groupBox)
        self.DP_OutputFileName.setObjectName(u"DP_OutputFileName")

        self.gridLayout.addWidget(self.DP_OutputFileName, 6, 0, 1, 1)

        self.DP_OutputFileNameLE = QLineEdit(self.groupBox)
        self.DP_OutputFileNameLE.setObjectName(u"DP_OutputFileNameLE")
        self.DP_OutputFileNameLE.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.DP_OutputFileNameLE, 6, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.DP_CancelPB = QPushButton(self.groupBox)
        self.DP_CancelPB.setObjectName(u"DP_CancelPB")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DP_CancelPB.sizePolicy().hasHeightForWidth())
        self.DP_CancelPB.setSizePolicy(sizePolicy1)
        self.DP_CancelPB.setMinimumSize(QSize(0, 0))
        self.DP_CancelPB.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.DP_CancelPB, 0, Qt.AlignRight)

        self.DP_OkayPB = QPushButton(self.groupBox)
        self.DP_OkayPB.setObjectName(u"DP_OkayPB")
        sizePolicy1.setHeightForWidth(self.DP_OkayPB.sizePolicy().hasHeightForWidth())
        self.DP_OkayPB.setSizePolicy(sizePolicy1)
        self.DP_OkayPB.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.DP_OkayPB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.DP_SingleFileRB.setText(QCoreApplication.translate("Form", u"singleFile", None))
        self.DP_MultiFileRB.setText(QCoreApplication.translate("Form", u"Multiple file", None))
        self.DP_SetupFileLab.setText(QCoreApplication.translate("Form", u"Program set up file ", None))
        self.DP_SetupFilePB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.DP_InstrumentconfigFileLB.setText(QCoreApplication.translate("Form", u"Instrument config file", None))
        self.DP_InstrumentConfigFilePB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.DP_InputDirLB.setText(QCoreApplication.translate("Form", u"Input directory", None))
        self.DP_InputDirPB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.DP_OutputDirLB.setText(QCoreApplication.translate("Form", u"Output directory", None))
        self.DP_OutputDirPB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.DP_InputFileNameLB.setText(QCoreApplication.translate("Form", u"Input File", None))
        self.DP_InputFileNamePB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.DP_NameAppendLabel.setText(QCoreApplication.translate("Form", u"Name Append", None))
        self.DP_OutputFileName.setText(QCoreApplication.translate("Form", u"Output File Name ", None))
        self.DP_CancelPB.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.DP_OkayPB.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi





