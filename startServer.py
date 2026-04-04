from server import Host

running = True
while running:
    try:
        server = Host()
        server.start()
        ip = server.get_ip()
        print(f"Enter this ip in the client to connect [Make sure both the computers are connected to same wifi]\n{ip}")
        choice = input(">>")
        if choice == 'q':
            running = False
        
    except KeyboardInterrupt:
        running = False