from ui import *
from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 27015))
sock.sendall(b"this would be the word that get's appended but there would not be any spaces because then it "
             b"would not be a word")
data = sock.recv(1024)
print("I GOT A BINGO! ", repr(data))
sock.close()
app = MainWindow()
app.run()
