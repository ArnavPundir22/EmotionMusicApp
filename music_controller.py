# music_controller.py
import os
import random
from pygame import mixer

mixer.init()

BASE_MUSIC_DIR = os.path.join(os.getcwd(), "music")

emotion_to_folder = {
    'happy': 'happy',
    'sad': 'sad',
    'angry': 'angry',
    'fear': 'fear',
    'surprise': 'surprise',
    'neutral': 'neutral',
    'disgust': 'disgust'
}

current_playlist = []
current_index = -1
is_paused = False

def load_playlist(emotion):
    global current_playlist, current_index
    folder = emotion_to_folder.get(emotion.lower(), 'neutral')
    path = os.path.join(BASE_MUSIC_DIR, folder)

    if not os.path.exists(path):
        print(f"[Music] Folder not found: {path}")
        current_playlist = []
        return

    songs = [os.path.join(path, file) for file in os.listdir(path)
             if file.lower().endswith(('.mp3', '.wav', '.ogg','.mpeg'))]

    random.shuffle(songs)
    current_playlist = songs
    current_index = 0

def play_current_song():
    if current_playlist and 0 <= current_index < len(current_playlist):
        try:
            mixer.music.load(current_playlist[current_index])
            mixer.music.play()
            print(f"[Music] Playing: {os.path.basename(current_playlist[current_index])}")
        except Exception as e:
            print(f"[Music Error]: {e}")

def get_current_playlist_names():
    return [os.path.basename(path) for path in current_playlist]

def play_song_by_index(index):
    global current_index
    if 0 <= index < len(current_playlist):
        current_index = index
        play_current_song()


def play_music_for_emotion(emotion):
    load_playlist(emotion)
    play_current_song()

def pause_music():
    global is_paused
    if mixer.music.get_busy():
        mixer.music.pause()
        is_paused = True

def resume_music():
    global is_paused
    if is_paused:
        mixer.music.unpause()
        is_paused = False

def stop_music():
    mixer.music.stop()

def next_song():
    global current_index
    if current_playlist:
        current_index = (current_index + 1) % len(current_playlist)
        play_current_song()

def previous_song():
    global current_index
    if current_playlist:
        current_index = (current_index - 1) % len(current_playlist)
        play_current_song()
