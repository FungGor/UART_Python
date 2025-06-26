class FrameCommunicationProtocol():
    def __init__(self):
        self.frameID = 0xFF
        self.txPayloadLength = 0
        self.rxPayloadLength = 0
        self.txPayload = bytearray()
        self.rxPayload = bytearray()
    
    def getFrameID(self, txMsgID):
        self.frameID = txMsgID & 0x1F  # Mask to get the last 4 bits
        return self.frameID
    
    def getrxPayloadLength(self, rxMsgFirstIndex):
        self.rxPayloadLength = rxMsgFirstIndex[1]
        return self.rxPayloadLength
    
    def getRxPayLoad(self, rxMsg):
        self.rxPayload = rxMsg[2:2 + self.rxPayloadLength]
        return self.rxPayload
    
    def getTxPayloadLength(self, size):
        self.txPayloadLength = size
        return self.txPayloadLength
    
    def getTxPayLoad(self, txMsg):
        self.txPayload = txMsg[2:2 + self.txPayloadLength]
        return self.txPayload