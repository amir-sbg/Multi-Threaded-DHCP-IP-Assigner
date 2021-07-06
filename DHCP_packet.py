class DHCP_packet:
    def __init__(self, OperationCode8,
                 HardwareType8,
                 HardwareAddressLength8,
                 Hops8,
                 TransactionIdentifier32,
                 seconds16,
                 flags16,
                 ciaddr_ClientIP32,
                 yiaddr_YourIP32,
                 siaddr_ServerIP32,
                 giaddr_GatewayIP32,
                 chaddr_ClienHardwaretIP32,
                 sname_ServerName32,
                 bname_BootFileName32,
                 mcookie_MagicCookie8,
                 Options24):
        self.__OperationCode8 = OperationCode8
        self.__HardwareType8 = HardwareType8
        self.__HardwareAddressLength8 = HardwareAddressLength8
        self.__Hops8 = Hops8

        self.__TransactionIdentifier32 = TransactionIdentifier32

        self.__seconds16 = seconds16
        self.__flags16 = flags16

        self.__ciaddr_ClientIP32 = ciaddr_ClientIP32
        self.__yiaddr_YourIP32 = yiaddr_YourIP32
        self.__siaddr_ServerIP32 = siaddr_ServerIP32
        self.__giaddr_GatewayIP32 = giaddr_GatewayIP32
        self.__chaddr_ClienHardwaretIP32 = chaddr_ClienHardwaretIP32
        self.__sname_ServerName32 = sname_ServerName32
        self.__bname_BootFileName32 = bname_BootFileName32

        self.__mcookie_MagicCookie8 = mcookie_MagicCookie8
        self.__Options24 = Options24

    def DHCP_messageEncoder(self):
        return ("{:08b}".format(self.__OperationCode8) + \
                "{:08b}".format(self.__HardwareType8) + \
                "{:08b}".format(self.__HardwareAddressLength8) + \
                "{:08b}".format(self.__Hops8) + \
                "{:32b}".format(self.__TransactionIdentifier32) + \
                "{:16b}".format(self.__seconds16) + \
                "{:16b}".format(self.__flags16) + \
                "{:32b}".format(self.__ciaddr_ClientIP32) + \
                "{:32b}".format(self.__yiaddr_YourIP32) + \
                "{:32b}".format(self.__siaddr_ServerIP32) + \
                "{:32b}".format(self.__giaddr_GatewayIP32) + \
                "{:32b}".format(self.__chaddr_ClienHardwaretIP32) + \
                "{:32b}".format(self.__sname_ServerName32) + \
                "{:32b}".format(self.__bname_BootFileName32) + \
                "{:8b}".format(self.__mcookie_MagicCookie8) + \
                "{:24b}".format(self.__Options24)).replace(" ", "0")

    def DHCP_messageDecoder(self, message):
        self.__OperationCode8 = int(message[0:8], 2)
        self.__HardwareType8 = int(message[8:16], 2)
        self.__HardwareAddressLength8 = int(message[16:24], 2)
        self.__Hops8 = int(message[24:32], 2)

        self.__TransactionIdentifier32 = int(message[32:64], 2)

        self.__seconds16 = int(message[64:80], 2)
        self.__flags16 = int(message[80:96], 2)

        self.__ciaddr_ClientIP32 = int(message[96:128], 2)
        self.__yiaddr_YourIP32 = int(message[128:160], 2)
        self.__siaddr_ServerIP32 = int(message[160:192], 2)
        self.__giaddr_GatewayIP32 = int(message[192:224], 2)
        self.__chaddr_ClienHardwaretIP32 = int(message[224:256], 2)
        self.__sname_ServerName32 = int(message[256:288], 2)
        self.__bname_BootFileName32 = int(message[288:320], 2)

        self.__mcookie_MagicCookie8 = int(message[320:328], 2)
        self.__Options24 = int(message[328:352], 2)

    # query_params = "{:04x}".format(int( str(QR) + str(OPCODE).zfill(4) + str(AA) + str(TC) + str(RD) + str(RA) + str(Z).zfill(3) + str(RCODE).zfill(4), 2))
    def printer(self):
        print(self.__OperationCode8)
        print(self.__HardwareType8)
        print(self.__HardwareAddressLength8)
        print(self.__Hops8)
        print(self.__TransactionIdentifier32)
        print(self.__seconds16)

        print(self.__flags16)
        print(self.__ciaddr_ClientIP32)
        print(self.__yiaddr_YourIP32)
        print(self.__siaddr_ServerIP32)
        print(self.__giaddr_GatewayIP32)
        print(self.__chaddr_ClienHardwaretIP32)
        print(self.__sname_ServerName32)
        print(self.__bname_BootFileName32)
        print(self.__mcookie_MagicCookie8)
        print(self.__Options24)

    def ipEncoder(self, ip):
        ipL = ip.split(".")
        ipEncoded = ""
        for i in ipL:
            print("{:08b}".format(int(i)))
            ipEncoded = ipEncoded + "{:08b}".format(int(i))
        return ipEncoded

    def ipDecoder(self, intIP):
        ipDecoded = ""
        for i in range(0, 4):
            ipDecoded = ipDecoded + str(int(intIP[i * 8:(i + 1) * 8], 2)) + "."
        return ipDecoded[0:-1]
    # x = "{:03b}".format(3)


# y = 0xc0a80164
#
# print(type(x))
# print(x)
#
# print(type(y))
# print(y)


#
# print(type(str(4).zfill(10)))
# print((str(4).zfill(10)))

# import socket
# import struct
#
# def ip2int(addr):
#     return struct.unpack("!I", socket.inet_aton(addr))[0]
#
# def int2ip(addr):
#     return socket.inet_ntoa(struct.pack("!I", addr))
#
# print(int2ip(0xc0a80164)) # 192.168.1.100
# print(ip2int('10.0.0.1')) # 167772161


# x=DHCP_packet(1,2,3,4  ,5,6,1,7,8,9,11,8,2,3,10,2)
# g=DHCP_packet(6,7,5,4,5,6,6,6,5,6,6,5,4,3,3,45)
# y=x.DHCP_messageEncoder()
# print(y)
# x.DHCP_messageDecoder(y)
# g.printer()
# g.DHCP_messageDecoder(y)
# print()
# # x.printer()
# g.printer()
x = ipEncoder("193.222.224.2")
print(len(x))
print(ipDecoder(x))
# print(x.split("."))
