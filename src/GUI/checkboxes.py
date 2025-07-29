import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)  # x, y, width, height
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("front-size: 30px;"
                                    "font-family:Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)


    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("you like food")
        else:
            print("you do not like food.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # This is valid in PyQt5

if __name__ == "__main__":
    main()
