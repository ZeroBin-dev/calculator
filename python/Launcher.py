import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtGui import QIcon
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, 'component'))

# 계산 서비스 import
from Calc import Calc

class Calculator(QWidget):

    # 생성자
    def __init__(self):
        super().__init__()
        self.initUI()

    # QT 초기화
    def initUI(self):
        self.setWindowTitle('파이썬 계산기')
        self.setGeometry(300, 300, 400, 400)
        
        # 아이콘 설정
        icon_path = os.path.join(os.path.dirname(__file__), 'image', 'favicon.png')
        self.setWindowIcon(QIcon(icon_path))

        # 레이아웃 생성
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        # 텍스트 상자 생성
        self.result_display = QLineEdit(self)
        self.result_display.setFixedHeight(50)
        grid_layout.addWidget(self.result_display, 0, 0, 1, 4)

        # 버튼 생성
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]

        row, col = 1, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)

            button.clicked.connect(self.button_clicked)
            grid_layout.addWidget(button, row, col)
            
            # 컬럼이 4개가 되면 다음줄로 넘어가기
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid_layout)
        self.setLayout(layout)

        self.show()

    def button_clicked(self):
        clicked_button = self.sender()
        current_text = self.result_display.text()
        
        if clicked_button.text() == '=':
            try:
                # eval 함수를 통해 수식을 계산
                result = eval(current_text)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText('Error')
        else:
            new_text = current_text + clicked_button.text()
            self.result_display.setText(new_text)

# main 함수
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    
    # 계산(이건안씀)
    calc = Calc()
    print(calc.add(1, 2));


    sys.exit(app.exec())
