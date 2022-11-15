from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('edytor.ui', self)
        self.show()

        self.setWindowTitle("Notepad Clone")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.close)
        self.actionChange_Font.triggered.connect(self.change_font)

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))

    def change_font(self):
        font, _ = QFontDialog.getFont()
        if _:
            self.plainTextEditor.setFont(font)

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files(*.py)",
                                                  options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files(*)",
                                                  options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your file?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)  # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)  # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)  # 2

        answer = dialog.exec_()
        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()
