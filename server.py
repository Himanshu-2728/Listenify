import socket
import threading
import time

class Host(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET , socket.SOCK_STREAM)
        self.add = socket.gethostbyname(socket.gethostname())
        self.clients = []
        self.port = 5050
        self.bind((self.add , self.port))
        self.listen()
        self.ready_clients = set()

    @property
    def numClients(self):
        return len(self.clients)

    def handle_client_events(self , conn , addr):
        while True:
            try:

                msg = conn.recv(1024).decode()
                if msg != "":
                    if "playreq" in msg:
                        self.ready_clients.clear()
                        songName = msg.split(":")[1]
                        for client in self.clients:
                            client.send(f"load:{songName}".encode())
                        print(f"load:{songName} sent to all clients")

                    elif "ready" in msg:
                        self.ready_clients.add(conn)
                        readySongName = msg.split(":")[1]
                        timestamp = time.time() + 2
                        if len(self.ready_clients) == self.numClients:
                            for client in self.clients:
                                client.send(f"playSongOnTimestamp:{readySongName}:{timestamp}".encode("utf-8"))

                    elif "p" in msg:
                        for client in self.clients:
                            client.send("pause".encode("utf-8"))

            except ConnectionResetError:
                self.clients = [x for x in self.clients if x!= conn]
                print(f"[DISCONNECTION] {addr} disconnected")     
                break    



    def accept_clients(self):
        while True:
            conn , addr = self.accept()
            print(f"[NEW CONNECTION] {addr} connected")
            self.clients.append(conn)
            threading.Thread(target=self.handle_client_events , args=(conn, addr) , daemon=True).start()


    def get_ip(self):
        return self.add

    def start(self):
        threading.Thread(target=self.accept_clients , daemon= True).start()    
        print("[STATUS] Server is now accepting client connections")