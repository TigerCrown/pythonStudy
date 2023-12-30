import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 레이아웃 설정
        layout = QVBoxLayout()

        # 결과 표시창
        self.result_display = QLineEdit(self)
        layout.addWidget(self.result_display)

        # 버튼 생성 및 연결
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        grid_row, grid_col = 4, 4
        grid_index = 0
        grid = []
        for i in range(grid_row):
            row = []
            for j in range(grid_col):
                button = QPushButton(buttons[grid_index], self)
                button.clicked.connect(self.on_button_click)
                row.append(button)
                grid_index += 1
            grid.append(row)

        # 버튼을 레이아웃에 추가
        for row in grid:
            button_row = QVBoxLayout()
            for button in row:
                button_row.addWidget(button)
            layout.addLayout(button_row)

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