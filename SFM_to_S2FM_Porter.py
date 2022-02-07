import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from converter_ui import Ui_MainWindow
import convert_s1_to_s2

with open("save.txt", "r") as file:
            data = file.readlines()
            data[0] = data[0][0:-1]
            if len(data) < 2:
                data.append("")
                data.append("")
# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.setFixedSize(544, 165)
        self.Convert_btn.clicked.connect(self.start_converting)
        self.Save_btn.clicked.connect(self.save_data)
        self.SFM_Folder.setText(data[0])
        self.S2FM_Folder.setText(data[1])
        self.Firend_Endlire.setText("<a href=\"https://vk.com/public207807597/\">GUI made by Firend_Endlire</a>")
        self.Firend_Endlire.setOpenExternalLinks(True)
        self.REDxEYE.setText("<a href=\"https://github.com/REDxEYE/Source2Converter/\">Original converter made by REDxEYE</a>")
        self.REDxEYE.setOpenExternalLinks(True)
        self.setWindowIcon(QtGui.QIcon('Icon.png'))

    def start_converting(self):
        sfm_folder = str(self.SFM_Folder.text())
        s2fm_folder = str(self.S2FM_Folder.text())
        if s2fm_folder == "":
            s2fm_folder = sfm_folder + "_converted"
        command = f'python convert_s1_to_s2.py -m {sfm_folder} -a {s2fm_folder}' 
        if self.check_compile.isChecked():
            command += " -c"
        if self.check_sandbox.isChecked():
            command += " -s"
        if self.check_debug.isChecked():
            command += " -d"
        os.system(command)
    
    def save_data(self):
        with open("save.txt", "w") as file:
            now = str(self.SFM_Folder.text() + "\n")
            file.write(now)
            now = str(self.S2FM_Folder.text())
            file.write(now)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setWindowIcon(QtGui.QIcon('Icon.png'))
    ex.show()
    sys.exit(app.exec_())
    
