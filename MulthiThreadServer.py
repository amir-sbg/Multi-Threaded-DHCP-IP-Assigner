import socket, threading


class Server:

    def __init__(self):
        self.IP_pool = []
        self.blockedMACs = []
        self.__serversIP = "127.0.0.1"
        self.__serversPort = 8080

    def runServer(self):
        server = socket.socket(family=socket.AF_INET,type= socket.SOCK_DGRAM)
        # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.__serversIP, self.__serversPort))

        while True:
            server.listen(1)
            clientsock, clientAddress = server.accept()
            newthread = ServerSideClientHandler(clientAddress, clientsock)
            newthread.start()


class ServerSideClientHandler(threading.Thread):

    def __init__(self, clientAddress, clientsocket):
        self.clientAddress = clientAddress
        self.clientsocket = clientsocket
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New client connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", self.clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            if True:
                print("Server : receiving DISCOVERY from client ...")
                DHCP_DISCOVERY = self.csocket.recv(2048)
                DHCP_DISCOVERY = DHCP_DISCOVERY.decode()
                print("Client DISCOVERY :", DHCP_DISCOVERY,end="\n")
                print("Server : sending OFFER ...")
                self.csocket.send(self.DHCP_OFFER_Sender())
                print("Server : receiving REQUEST from client ...")
                DHCP_REQUEST = self.csocket.recv(2048)
                DHCP_REQUEST = DHCP_REQUEST.decode()
                print("Client REQUEST :", DHCP_DISCOVERY, end="\n")
                print("Server : sending ACK ...")
                self.csocket.send(self.DHCP_ACK_Sender())
            else:
                if msg == 'bye':
                    break
                print("from client", msg)

        print("Client at ", self.clientAddress, " disconnected...")

    def DHCP_ACK_Sender(self):
        pass

    def DHCP_OFFER_Sender(self):
        pass
