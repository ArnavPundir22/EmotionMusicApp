
# 🎵 Emotion Music Recommender - EmotionMusicApp

An AI-powered desktop application that **detects your emotion using webcam** or allows **manual emotion selection**, and plays music tailored to your mood.  
You can also **add your favorite songs** to each emotion category.

---

## 💡 Features

- 🎭 Real-time emotion detection via webcam (DeepFace)
- 👤 Manual emotion selection (bypass detection)
- 📂 Add music to any emotion category
- 🎧 Emotion-specific playlists (happy, sad, angry, etc.)
- ⏯️ Media controls: Play, Pause, Next, Previous
- 🖥️ PyQt5 GUI with dark mode

---


## 🛠 Technologies Used

- **Python**
- **OpenCV** (webcam & image processing)
- **DeepFace**  `emotion_detector.py` model
- **PyQt5** (for GUI)
- **Pygame** or **Mixer** for audio playback

---

## 📁 Folder Structure

```
EmotionMusicApp/
│
├── emotion_detector.py      # Handles emotion prediction from webcam frame
├── music_controller.py      # Handles audio controls per emotion
├── EmotionMusicGUI.py       # Main GUI application                
├── songs/
│   ├── happy/
│   ├── sad/
│   ├── angry/
│   ├── surprise/
│   ├── fear/
│   ├── neutral/
└── README.md
```

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/EmotionMusicApp.git
cd EmotionMusicApp
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not created, use:
```bash
pip install PyQt5 opencv-python pygame deepface
```

3. **Run the app**
```bash
python EmotionMusicGUI.py
```

---

## 🎼 How to Add Songs

- ✅ Click **"➕ Add Song to Category"** to browse and copy a song into the appropriate emotion folder.
- 📂 Songs are stored in `songs/<emotion>/`.

---

## 🎯 Manual Emotion Selection

- You can click **"🎯 Select Emotion Manually"** to skip webcam detection and directly choose your mood.
- This instantly plays music for the selected emotion.

---

## 🧠 Emotion Categories Supported

- Happy 🥳  
- Sad ☹️  
- Angry 🤬  
- Surprise 😮  
- Fear 😱  
- Neutral 😒  

---

## ⚠️ Notes

- Webcam required for automatic detection.
- Emotion detection is done every 10 seconds to reduce overhead.
- Make sure music files are `.mp3` or `.wav`.

---

## Developer

- This is created by **Arnav Pundir**
