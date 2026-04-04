import socket
import threading
from getStreamUrl import get_stream_url
import time
import sys

class Client(socket.socket):
    def __init__(self , player , ip):
        self.player = player
        self.stream_url = ""
        self.isConnected = False
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        try:

            self.connect((ip , 5050))
            print("[SUCCESS] Connection Established")
            self.isConnected = True
        except Exception as e:
            print("[ERROR] Please check if the ip is correct of the server is running properly")
            sys.exit()

        if self.isConnected:
            threading.Thread(target=self.recv_messages , daemon=True).start()

    def recv_messages(self):
        while self.isConnected: 
            try:
                bytes = self.recv(1024)

                if not bytes:
                    print("[ERROR] Server disconnected")
                    break

                data = bytes.decode().split(":")
                
    
                if data[0] == 'pause':
                    self.player.pause = not self.player.pause

                elif data[0] == "load":
                    loadSongName = data[1]
                    url = get_stream_url(loadSongName)
                    self.stream_url = url
                    self.send_event(f"ready:{loadSongName}")

                elif data[0] == "playSongOnTimestamp":
                    timestamp = float(data[2])
                    delay = timestamp - time.time()
                    if delay > 0:
                        time.sleep(delay)
                    
                    print(f"[NOW PLAYING] {loadSongName}")
                    self.player.play(self.stream_url)

            except ConnectionResetError:
                print("[ERROR] Server Disconnected")
                self.isConnected = False
                break


            except Exception as e:
                print(e)
        

    def send_event(self , event):
        self.send(str.encode(event))

