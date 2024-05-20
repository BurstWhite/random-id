from PySide6.QtWidgets import QApplication
from lib.window import RandomNumberApp
import sys

App = QApplication([])

if __name__ == '__main__':
    window = RandomNumberApp()
    window.show()
    sys.exit(App.exec())