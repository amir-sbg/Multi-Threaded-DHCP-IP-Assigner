import socket, random


class Client:
    def __init__(self):
        self.__serverIP, self.__port = "127.0.0.1", 8080
        self.__timeoutTimer = 80
        self.__discoverTimer = 80
        self.__backoff_cutoff = 120
        self.__initial_interval = 10
        self.__previousInterval = 0

    def runClient(self):
        clientSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        while True:
            if True:
                print("Client : sending DISCOVERY ...")
                clientSock.sendto(self.DHCP_DISCOVERY_Sender(), (self.__serverIP, self.__port))

                print("Client : receiving OFFER from server ...")
                DHCP_Offer = clientSock.recv(2048)
                print("Server OFFER :", DHCP_Offer.decode(), end="\n")

                print("Client : sending REQUEST ...")
                clientSock.sendto(self.DHCP_REQUEST_Sender(), (self.__serverIP, self.__port))

                print("Client : receiving ACK from server ...")
                DHCP_Ack = clientSock.recv(2048)
                print("\u2592\u2592\u2592\u2592\u2592")
                print("Server ACK :", DHCP_Ack.decode(), end="\n")

                if DHCP_Ack == 'bye':
                    break
            else:
                pass
        clientSock.close()

    def DHCP_REQUEST_Sender(self):
        return ""

    def DHCP_DISCOVERY_Sender(self):
        return ""

    def previousIntervalCalculator(self):
        newTimeInterval = self.__previousInterval * 2 * (random.random.uniform(0, 1))
        if newTimeInterval < self.__backoff_cutoff:
            self.__previousInterval = newTimeInterval
        else:
            self.__previousInterval = self.__backoff_cutoff
