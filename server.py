import socket
import threading

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("10.133.136.37", 5000))
# server.listen()

# clients = []

# def recv_client_messages(conn):
#     while True:
#         msg = conn.recv(1024).decode('utf-8')
#         for i in [x for x in clients if x != conn]:
#             i.send(msg.encode())

# def accept_client(server):
#     print("Thread started")
#     while True:
#         conn, addr = server.accept()
#         print("Someone just connected")
#         clients.append(conn)
#         threading.Thread(target=recv_client_messages , args=(conn , ) , daemon=True).start()

# threading.Thread(target=accept_client , args= (server ,),  daemon=True ).start()

class Host(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET , socket.SOCK_STREAM)
        self.add = socket.gethostbyname(socket.gethostname())
        self.clients = []
        self.port = 5050
        self.bind((self.add , self.port))
        self.listen()

    def handle_client_events(self , conn):
        while True:
            msg = conn.recv(1024)
            for client in [x for x in self.clients if x != conn]:
                client.send(msg)

    def accept_clients(self):
        while True:
            conn , addr = self.accept()
            print(addr , " connected")
            self.clients.append(conn)
            threading.Thread(target=self.handle_client_events , args=(conn,) , daemon=True).start()


    def get_connection_url(self):
        return self.add + ":" + str(self.port)

    def start(self):
        threading.Thread(target=self.accept_clients , daemon= True).start()    