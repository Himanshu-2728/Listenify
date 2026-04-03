import socket
import threading
from getStreamUrl import get_stream_url

class Client(socket.socket):
    def __init__(self , player):
        self.player = player
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        try:

            self.connect((socket.gethostbyname(socket.gethostname()) , 5050))
        
        except Exception as e:
            print(e)

        threading.Thread(target=self.recv_messages).start()

    def recv_messages(self):
        while True: 
            try:
                data = self.recv(1024).decode().split(":")
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if(data[0] == "next"):
                    next_song = data[1]
                    print("next song event recieved:" + next_song)
                    url = get_stream_url(next_song)
                    self.player.stop()
                    print(f"Now playing {next_song}")
                    self.player.play(url)
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if(data[0] == "play"):
                    url = get_stream_url(data[1])
                    self.player.play(url)
                if not data:
                    print("client disconnected")

            except Exception as e:
                print(e)

    def send_event(self , event):
        self.send(str.encode(event))

