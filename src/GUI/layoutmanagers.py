import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(100, 100, 500, 500)
        self.initUI()  # Call it here

    def initUI(self):  # Should be defined as a separate method
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create labels
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        # Set background colors
        label1.setStyleSheet("background-color: red; color: white; padding: 10px;")
        label2.setStyleSheet("background-color: yellow; padding: 10px;")
        label3.setStyleSheet("background-color: green; color: white; padding: 10px;")
        label4.setStyleSheet("background-color: blue; color: white; padding: 10px;")
        label5.setStyleSheet("background-color: purple; color: white; padding: 10px;")

        # Layout (Horizontal box)
        hbox = QVBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
