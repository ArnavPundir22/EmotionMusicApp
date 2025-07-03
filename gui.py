import sys
import time
import cv2
import os
import shutil
from PyQt5.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QWidget,
    QPushButton, QHBoxLayout, QListWidget, QCheckBox,
    QFileDialog, QInputDialog
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from emotion_detector import detect_emotion
import music_controller as mc


os.environ["QT_QPA_PLATFORM"] = "wayland"  # Optional for Linux/Wayland


class EmotionMusicGUI(QWidget):
    emoji_map = {
        "happy": "🥳",
        "sad": "☹️",
        "angry": "🤬",
        "surprise": "😮",
        "fear": "😱",
        "neutral": "😒",
        "disgust": "🤫"
    }

    last_detection_time = 0
    detection_interval = 10  # seconds

    def __init__(self):
        super().__init__()
        # Set Dark Theme
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: white;
                font-size: 14px;
            }
            QLabel {
                color: white;
            }
            QListWidget {
                background-color: #222;
                color: white;
            }
            QCheckBox, QPushButton {
                background-color: #333;
                color: white;
                padding: 5px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

        self.setWindowTitle("Emotion Music Recommender")
        self.setGeometry(500, 100, 600, 700)

        self.image_label = QLabel()
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: green; font-size: 14px;")
        self.emotion_label = QLabel("Detected Emotion: None")

        # Playlist view
        self.song_list = QListWidget()
        self.song_list.itemClicked.connect(self.song_selected)

        # Emotion Detection Toggle
        self.emotion_toggle = QCheckBox("Enable Emotion Detection")
        self.emotion_toggle.setChecked(True)

        # Add Song Button
        self.add_song_button = QPushButton("➕ Add Song to Category")
        self.add_song_button.clicked.connect(self.add_song_to_category)

        # Manual Emotion Select Button
        self.manual_emotion_button = QPushButton("🎯 Select Emotion Manually")
        self.manual_emotion_button.clicked.connect(self.select_emotion_manually)

        # Control Buttons
        self.play_pause_button = QPushButton("⏯️ Play/Pause")
        self.next_button = QPushButton("⏭️ Next")
        self.prev_button = QPushButton("⏮️ Previous")

        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        self.next_button.clicked.connect(mc.next_song)
        self.prev_button.clicked.connect(mc.previous_song)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.prev_button)
        control_layout.addWidget(self.play_pause_button)
        control_layout.addWidget(self.next_button)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.emotion_label)
        layout.addWidget(self.song_list)
        layout.addWidget(self.emotion_toggle)
        layout.addWidget(self.manual_emotion_button)
        layout.addWidget(self.add_song_button)
        layout.addLayout(control_layout)
        self.setLayout(layout)

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.emotion_label.setText("Error: Unable to access webcam")
            return

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # ~33 fps

        self.last_emotion = None

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.flip(frame, 1)  # Mirror the frame

        # Show webcam frame
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(img))

        if self.emotion_toggle.isChecked():
            current_time = time.time()
            if current_time - self.last_detection_time >= self.detection_interval:
                self.last_detection_time = current_time

                self.status_label.setText("Detecting Emotion...")
                emotion = detect_emotion(frame)
                self.status_label.setText("")

                if emotion and emotion != self.last_emotion:
                    self.last_emotion = emotion
                    self.emotion_label.setText(
                        f"Detected Emotion: {emotion.capitalize()} {self.emoji_map.get(emotion, '')}"
                    )
                    mc.stop_music()
                    mc.play_music_for_emotion(emotion)
                    self.load_song_list()

    def toggle_play_pause(self):
        if mc.is_paused:
            mc.resume_music()
        else:
            mc.pause_music()

    def song_selected(self, item):
        index = self.song_list.row(item)
        mc.play_song_by_index(index)

    def load_song_list(self):
        self.song_list.clear()
        songs = mc.get_current_playlist_names()
        self.song_list.addItems(songs)

    def add_song_to_category(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a music file", "", "Audio Files (*.mp3 *.wav)")
        if file_path:
            emotions = list(self.emoji_map.keys())
            emotion, ok = QInputDialog.getItem(self, "Select Emotion Category", "Emotion:", emotions, 0, False)
            if ok and emotion:
                dest_folder = os.path.join("songs", emotion)
                os.makedirs(dest_folder, exist_ok=True)
                try:
                    shutil.copy(file_path, dest_folder)
                    self.status_label.setText(f"✅ Song added to '{emotion}' category.")
                    if emotion == self.last_emotion:
                        self.load_song_list()
                except Exception as e:
                    self.status_label.setText(f"❌ Error adding song: {e}")

    def select_emotion_manually(self):
        emotions = list(self.emoji_map.keys())
        emotion, ok = QInputDialog.getItem(self, "Select Your Emotion", "Emotion:", emotions, 0, False)
        if ok and emotion:
            self.last_emotion = emotion
            self.emotion_label.setText(
                f"Manually Selected Emotion: {emotion.capitalize()} {self.emoji_map.get(emotion, '')}"
            )
            mc.stop_music()
            mc.play_music_for_emotion(emotion)
            self.load_song_list()

    def closeEvent(self, event):
        self.cap.release()
        mc.stop_music()
        mc.mixer.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmotionMusicGUI()
    window.show()
    sys.exit(app.exec_())
