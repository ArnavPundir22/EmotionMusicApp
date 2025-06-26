import sys
from PyQt5.QtWidgets import QApplication
from gui import EmotionMusicGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmotionMusicGUI()
    window.show()
    sys.exit(app.exec_())
