#gui.py
import sys
import cv2
import os
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from emotion_detector import detect_emotion
from music_controller import play_music_for_emotion
from pygame import mixer

os.environ["QT_QPA_PLATFORM"] = "wayland"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class EmotionMusicGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Emotion Music Recommender")
        self.setGeometry(100, 100, 640, 480)

        self.image_label = QLabel()
        self.emotion_label = QLabel("Detected Emotion: None")

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.emotion_label)
        self.setLayout(layout)

        self.setStyleSheet("""
            QLabel { font-size: 16px; }
        """)

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.emotion_label.setText("Error: Unable to access webcam")
            return

        mixer.init()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # ~33 fps

        self.frame_count = 0
        self.last_emotion = None

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        # Show webcam frame
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(img))

        self.emoji_map = {
            "happy": "😄",
            "sad": "😢",
            "angry": "😠",
            "surprise": "😲",
            "fear": "😱",
            "neutral": "😐",
            "disgust": "🤢"
        }


        # Only detect emotion every 30 frames (~1 second if 30fps)
        self.frame_count += 1
        if self.frame_count % 30 == 0:
            emotion = detect_emotion(frame)
            if emotion and emotion != self.last_emotion:
                self.last_emotion = emotion
                self.emotion_label.setText(f"Detected Emotion: {emotion} {self.emoji_map.get(emotion, '')}")

                play_music_for_emotion(emotion)

    def closeEvent(self, event):
        self.cap.release()
        mixer.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmotionMusicGUI()
    window.show()
    sys.exit(app.exec_())
