import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication Setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="64ef1f4d49054b3f9ddfd0d687b65826",
    client_secret="79641bb1ed7e4692aeda5a7bc21d7403",
    redirect_uri="http://localhost:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

# Map emotions to mood keywords for Spotify search
emotion_to_query = {
    'happy': 'feel good',
    'sad': 'sad chill',
    'angry': 'rage workout',
    'fear': 'ambient focus',
    'surprise': 'indie vibes',
    'neutral': 'chill hits',
    'disgust': 'deep calm'
}

def play_music_for_emotion(emotion):
    try:
        query = emotion_to_query.get(emotion.lower(), 'chill vibes')
        results = sp.search(q=query, type='playlist', limit=1)

        if results['playlists']['items']:
            playlist_uri = results['playlists']['items'][0]['uri']
            sp.start_playback(context_uri=playlist_uri)
            print(f"[Spotify] Playing playlist for '{emotion}' mood.")
        else:
            print(f"[Spotify] No playlist found for '{emotion}'.")

    except Exception as e:
        print(f"[Spotify Error]: {e}")
