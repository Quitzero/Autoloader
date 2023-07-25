import sys
from PySide6 import QtWidgets

from UI.mainUI import Ui_MainWindow
from UI.settingsUI import Ui_Dialog


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.settings_button.triggered.connect(self.button_clicked)

    def button_clicked(self, s):
        print("click", s)

        dlg = SettingsInterface(self)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


class SettingsInterface(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
