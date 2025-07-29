import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(100, 100, 500, 500)

        # Radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)


        self.initUI()  # call setup

    def initUI(self):
        # Set geometry for each radio button
        self.radio1.setGeometry(20, 20, 300, 40)
        self.radio2.setGeometry(20, 70, 300, 40)
        self.radio3.setGeometry(20, 120, 300, 40)
        self.radio4.setGeometry(20, 170, 300, 40)
        self.radio5.setGeometry(20, 220, 300, 40)

        # Set styling
        self.setStyleSheet("""
            QRadioButton {
                font-size: 24px;
                font-family: Arial;
                padding: 5px;
            }
        """)

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is checkecd")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # Valid for PyQt5

if __name__ == "__main__":
    main()
