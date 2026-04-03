import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]


import mpv
from getStreamUrl import get_stream_url
from server import Host
from client import Client

player = mpv.MPV(video = False)

print("Do you want to host (1) or do you want to connect (2): ")
choice = int(input())
running = True
if choice == 1:
    host = Host()
    host.start()
    # query = input("Enter any song name: ")
    # stream_url = get_stream_url(query)
    # player.play(stream_url)
    while running:
        inp = input(">>")

        if inp == 'p':  # pause/resume
            player.pause = not player.pause

        elif inp == 's':  # stop
            player.stop()

        elif inp == 'q':  # quit
            player.quit()
            running = False

        elif inp == 'r':  # restart
            player.seek(0, reference='absolute')

        elif inp == 'f':  # forward 10s
            player.seek(10)

        elif inp == 'b':  # backward 10s
            player.seek(-10)

        elif inp == '+':  # volume up
            player.volume += 5

        elif inp == '-':  # volume down
            player.volume -= 5

        elif inp == 'n': 
            query = input("Enter next song name: ")
            stream_url = get_stream_url(query)
            player.stop()
            print("Playing next song")
            player.play(stream_url)

elif choice == 2:
    client = Client(player)
    # client.start()

    query = input("Enter any song name: ")
    client.send_event(f'play:{query}')
    stream_url = get_stream_url(query)
    player.play(stream_url)

    while running:
        inp = input(">>")

        if inp == 'p':  # pause/resume
            player.pause = not player.pause
            client.send_event(f"pause")

        elif inp == 's':  # stop
            player.stop()
            client.send_event(f"stop")

        elif inp == 'q':  # quit
            player.quit()
            running = False
            client.send_event(f"quit")

        elif inp == 'r':  # restart
            player.seek(0, reference='absolute')
            client.send_event(f"restart")

        elif inp == 'f':  # forward 10s
            player.seek(10)
            client.send_event(f"seek+")

        elif inp == 'b':  # backward 10s
            player.seek(-10)
            client.send_event("seek-")

        elif inp == '+':  # volume up
            player.volume += 5

        elif inp == '-':  # volume down
            player.volume -= 5

        elif inp == 'n': 
            query = input("Enter next song name: ")
            stream_url = get_stream_url(query)
            player.stop()
            print("Playing next song")
            player.play(stream_url)
            client.send_event(f"next:{query}")