import subprocess
from searchsong import search_youtube_music , extract_songs

def get_stream_url(query):

    data = search_youtube_music(query)
    id = extract_songs(data)[0]['videoId']
    url =  f"https://www.youtube.com/watch?v={id}"


    output = subprocess.check_output(
        [
            "yt-dlp",
            "--js-runtimes" , "node",
            "-f" , "bestaudio",
            "-g",
            "--no-playlist",
            url
        ]
    )

    return output.decode()