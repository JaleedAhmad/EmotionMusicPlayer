import yt_dlp
import subprocess

emotion_to_query = {
    "Happy": "feel good happy songs",
    "Sad": "sad lo-fi music",
    "Angry": "rock metal rage music",
    "Neutral": "calm background instrumental",
    "Fear": "soothing piano music",
    "Disgust": "lofi chill",
    "Surprise": "party hits"
}

def play_youtube_audio(emotion):
    query = emotion_to_query.get(emotion, "lofi beats")
    print(f"🔍 Searching YouTube for: {query}")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': False,
        'default_search': 'ytsearch1',
        'noplaylist': True,
        'extract_flat': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)

            if 'entries' in info:
                info = info['entries'][0]  # in case of ytsearch

            url = info['url']
            print(f"🎧 Streaming: {info['title']}")
            print(f"▶️ From: {url}")

            subprocess.Popen([
                'ffplay',
                '-nodisp',
                '-autoexit',
                url
            ])
    except Exception as e:
        print(f"❌ Error: {e}")
