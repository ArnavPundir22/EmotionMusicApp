# main,py
import sys
from PyQt5.QtWidgets import QApplication
from gui import EmotionMusicGUI

if __name__ == "__main__":
    playbacktry:
        app = QApplication(sys.argv)
        window = EmotionMusicGUI()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"[App Error]: {e}")
