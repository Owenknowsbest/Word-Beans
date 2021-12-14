import socketserver


class Server(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print("Handle!")

        data = self.request.recv(1024)
        print(data)
        self.request.send(data)


if __name__ == "__main__":
    address = ("", 27015)
    server = socketserver.TCPServer(address, Server)
    try:
        server.serve_forever()
    except:
        pass
