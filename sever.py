import socket
from _thread import *
from player import Player
# from nesto1 import *
import pickle


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)
server = IPAddr
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # s.recvfrom(port)
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")


# player1 = GameObject("dog.png", 480, 700, 50, 50)
# player2 = GameObject("cat (1).png", 380, 700, 50, 50)



#players = [PlayerCharacter("cat (1).png", 480, 700, 50, 50), PlayerCharacter("cat (1).png", 380, 700, 50, 50)]
#players = [Player(480, 700, 50, 50), Player( 380, 700, 50, 50)]
p1 = Player(340, 700, 50, 50)#, (255, 0, 0))
p2 = Player(480, 700, 50, 50)#, (0, 0, 255))

players = [p1, p2]
#enemies = [NonPlayerCharacter("dog.png", 80, 600, 50, 50), NonPlayerCharacter("dog.png", 80, 400, 50, 50), NonPlayerCharacter("dog.png", 20, 200, 50, 50)]


def threaded_client(conn, player):

    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]

                else:
                    reply = players[1]


                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))


        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
