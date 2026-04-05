import subprocess
from searchsong import search_youtube_music , extract_songs
from yt_dlp import YoutubeDL

def get_stream_url(query):

    data = search_youtube_music(query)
    id = extract_songs(data)[0]['videoId']
    url =  f"https://www.youtube.com/watch?v={id}"


    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info["url"]

    return audio_url

# print(get_stream_url("wildflower"))