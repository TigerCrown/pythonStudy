import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QIcon

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 레이아웃 설정
        layout = QVBoxLayout()

        # 결과 표시창
        self.result_display = QLineEdit(self)
        self.result_display.setFixedHeight(100)
        self.result_display.setFont(QFont('Arial', 24))
        self.result_display.setAlignment(Qt.AlignRight)
        layout.addWidget(self.result_display)

        # 버튼 생성 및 스타일 설정
        button_texts = [
            ('C', 'gray'),
            ('7', 'gray'),
            ('8', 'gray'),
            ('9', 'gray'),
            ('/', 'orange'),
            ('4', 'gray'),
            ('5', 'gray'),
            ('6', 'gray'),
            ('*', 'orange'),
            ('1', 'gray'),
            ('2', 'gray'),
            ('3', 'gray'),
            ('-', 'orange'),
            ('0', 'gray'),
            ('.', 'gray'),
            ('=', 'orange'),
            ('+', 'orange'),
        ]

        for button_text, color in button_texts:
            button = QPushButton(button_text, self)
            button.setFixedHeight(80)
            button.setFont(QFont('Arial', 20))
            button.setStyleSheet(f'background-color: {color}; border: none; color: white;')
            button.clicked.connect(self.on_button_click)
            layout.addWidget(button)

        # 윈도우 설정
        self.setLayout(layout)
        self.setWindowTitle('계산기')
        self.setGeometry(300, 300, 300, 500)
        self.setWindowIcon(QIcon('calculator_icon.png'))  # 아이콘 파일 경로에 맞게 수정

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