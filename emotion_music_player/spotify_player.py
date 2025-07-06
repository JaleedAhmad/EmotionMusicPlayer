import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

# Load environment variables
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-playback-state,user-modify-playback-state"
))

# Emotion to search query mapping
emotion_to_genre = {
    "Happy": "happy pop",
    "Sad": "sad songs",
    "Angry": "rock rage",
    "Neutral": "chill lofi",
    "Surprise": "party hits",
    "Fear": "soothing calm music",
    "Disgust": "ambient instrumental"
}

def play_emotion_track(emotion):
    query = emotion_to_genre.get(emotion, "lofi")
    results = sp.search(q=query, limit=1, type="track")

    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']

        print(f"\n🎵 Detected Emotion: {emotion}")
        print(f"🔊 Now Playing: {name} - {artist}")
        print(f"🌐 Opening in browser: {url}\n")

        webbrowser.open(url)
    else:
        print(f"No Spotify track found for emotion: {emotion}")
