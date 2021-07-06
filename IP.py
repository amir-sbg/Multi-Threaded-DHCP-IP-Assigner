class IP:
    def __init__(self, isFree=False, ownersMacAddress=None, laeseTime=None):
        self.__IPAddress = None
        self.__isFree = isFree
        self.__ownersMacAddress = ownersMacAddress
        self.__laeseTime = laeseTime

    def leaseTimeRenewtion(self, now):
        self.__laeseTime = now

    def makeFree(self):
        self.__ownersMacAddress = None
        self.__isFree = True

    def use(self, ownersMacAddress):
        self.__isFree = False
        self.__ownersMacAddress = ownersMacAddress

    def isFree(self):
        return self.__isFree

    def changeLeaseTime(self, leaseTime):
        self.__laeseTime = leaseTime
