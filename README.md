# 🎶 Emotion-Based Music Player

This project detects a user's facial emotion in real time using a webcam and plays music that matches the detected emotion — either from **YouTube** or **Spotify**.

## 📸 How It Works

1. Captures real-time video using your webcam.
2. Detects facial emotions using a CNN-based deep learning model (`emotion_model.h5`).
3. Maps detected emotions to relevant music genres.
4. Plays music using:
   - ✅ **YouTube** audio via `yt_dlp` and `ffplay`.
   - 🔄 (Optional) **Spotify** via the Spotify Web API and `spotipy`.

## 🧠 Emotions Detected

- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

## 🧰 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- yt-dlp + ffplay (for YouTube streaming)
- Spotipy + Spotify API (optional)
- Haar Cascade Classifier (for face detection)

## 📂 Project Structure

```
emotion-music-player/
├── emotion_model.h5             # Pre-trained emotion detection model
├── emotion_music_player.py      # Main emotion detection + YouTube playback script
├── spotify_player.py            # Plays emotion-based songs via Spotify
├── youtube_player.py            # Plays emotion-based songs via YouTube
├── requirements.txt
└── README.md
```

## 💿 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/emotion-music-player.git
   cd emotion-music-player
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) For Spotify support:**
   Create a `.env` file and add:
   ```
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

4. **Install ffmpeg (for `ffplay`) if using YouTube audio:**
   - Ubuntu: `sudo apt install ffmpeg`
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/)

## ▶️ Usage

### Run with YouTube Playback
```bash
python emotion_music_player.py
```

### Switch to Spotify Playback (optional)
Uncomment the `play_emotion_track(emotion)` line in `emotion_music_player.py` and comment out `play_youtube_audio(emotion)`.

> Note: You can only use either YouTube or Spotify for music at a time.

## 📌 Notes

- Only one face is handled at a time per frame.
- Music is selected based on dominant detected emotion.
- Spotify playback opens the song in your browser and requires an active Spotify device/session.

## 🚀 Future Enhancements

- Add GUI for user interaction.
- Support for multiple faces or group-based emotion.
- Advanced emotion tracking over time for dynamic playlisting.

## 👨‍💻 Author

**Jaleed Ahmad**

## 📜 License

MIT License – feel free to use, modify, and distribute.
