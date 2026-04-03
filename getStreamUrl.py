import subprocess
from searchsong import get_id

def get_stream_url(query):

    id = get_id(query)
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