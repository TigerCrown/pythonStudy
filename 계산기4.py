import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 레이아웃 설정
        layout = QVBoxLayout()

        # 결과 표시창
        self.result_display = QLineEdit(self)
        self.result_display.setFixedHeight(50)
        self.result_display.setFont(QFont('Arial', 18))
        layout.addWidget(self.result_display)

        # 버튼 생성 및 스타일 설정
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.setFixedHeight(60)
            button.setFont(QFont('Arial', 14))
            button.setStyleSheet('QPushButton {background-color: #f0f0f0; border: 1px solid #ccc;}'
                                 'QPushButton:pressed {background-color: #d5d5d5;}')
            button.clicked.connect(self.on_button_click)
            layout.addWidget(button)

        # 윈도우 설정
        self.setLayout(layout)
        self.setWindowTitle('계산기')
        self.setGeometry(300, 300, 300, 400)

        self.show()

    def on_button_click(self):
        sender = self.sender()
        current_text = self.result_display.text()

        if sender.text() == 'C':
            self.result_display.clear()
        elif sender.text() == '=':
            try:
                result = str(eval(current_text))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText('Error')
        else:
            self.result_display.setText(current_text + sender.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    sys.exit(app.exec_())