# EmotionMusicApp 🎵😊😢

EmotionMusicApp is an AI-powered music player that detects your emotion in real-time using your webcam and plays songs that match your mood. Built using Python, PyQt5 for the GUI, and DeepFace for emotion recognition, the app creates a personalized music experience based on how you feel.

## Features

- 🎭 Emotion detection using DeepFace and webcam input  
- 🎶 Automatic music playback based on detected emotion  
- 🖥️ Intuitive PyQt5-based GUI with Play, Pause, Next, and Previous controls  
- 📁 Supports organizing songs into folders by emotion (e.g., happy, sad, angry, etc.)

## Supported Emotions

- Happy  
- Sad  
- Angry  
- Neutral  
- Fear  
- Surprise  

## Folder Structure

To use EmotionMusicApp effectively, **copy your favorite songs into the respective emotion folders** inside the `songs/` directory.

Example folder structure:
```
EmotionMusicApp/
│
├── songs/
│   ├── happy/
│   ├── sad/
│   ├── angry/
│   ├── neutral/
│   ├── fear/
│   ├── surprise/
│   
```

Each folder should contain `.mp3` or `.wav` files appropriate for that emotion.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArnavPundir22/EmotionMusicApp.git
   cd EmotionMusicApp
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python gui.py
   ```

## Requirements

- Python 3.8+
- OpenCV
- DeepFace
- PyQt5
- Pygame (for audio playback)

You can install them manually if `requirements.txt` is not provided:
```bash
pip install opencv-python deepface PyQt5 pygame
```

## Notes

- Make sure your system has a webcam.
- The app may take a few seconds to detect the emotion.
- All music must be placed in the corresponding emotion folder **before using the app**.

## Creator

This project is created by - **Arnav Pundir**.

---

Enjoy music that understands your mood! 🎧🧠
