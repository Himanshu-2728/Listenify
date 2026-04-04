import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]


import mpv
from getStreamUrl import get_stream_url
from server import Host
from client import Client

player = mpv.MPV(video = False)
try:
    print("Enter host ip:")
    ip = input("-->")
    client = Client(player , ip )
    print('''Commands:
        !play -> enter -> type song name ## Use this command to play any song
        !p    -> Pause or resume playback
        !q    -> exit
    ''')
except KeyboardInterrupt:
    pass
running = True
while running:
    try:
        choice = input("")

        if choice == "!q":
            running = False

        elif choice == "!play":
            songName = input("Enter song name: ")
            client.send_event(f"playreq:{songName}")

        elif choice == '!p':
            client.send_event("p")
    
    except KeyboardInterrupt:
        running = False

    except OSError:
        break


    