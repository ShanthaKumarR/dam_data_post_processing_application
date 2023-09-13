from PyQt5.QtWidgets import QMessageBox

def log_writer(msg):
    with open('log\\log.txt', 'a') as log_file:
        log_file.write(msg+'\n')



def empty_field_alert(msg = 'Empty field alert'):
    alert_dialog_box = QMessageBox()
    alert_dialog_box.setWindowTitle('Empty field alert')
    alert_dialog_box.setIcon(QMessageBox.Warning)
    alert_dialog_box.setText(msg)
    alert_dialog_box.exec_()

class NoSetupFile(Exception):
    pass