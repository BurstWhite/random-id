import sys
import random
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class RandomNumberApp(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("学号抽取器")

        # 创建一个垂直布局
        self.layout = QVBoxLayout()

        # 创建一个标签用于显示随机数
        self.label = QLabel("按下按钮以抽取学号")
        self.layout.addWidget(self.label)

        # 创建一个按钮用于生成随机数
        self.button = QPushButton("抽取")
        self.button.clicked.connect(self.generate_random_number)
        self.layout.addWidget(self.button)

        # 设置布局
        self.setLayout(self.layout)

    def generate_random_number(self):
        # 生成一个随机数
        random_number = random.randint(1, 55)
        # 更新标签内容
        self.label.setText(f"抽到学号: {random_number}")