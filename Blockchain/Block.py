from hashlib import sha256
from datetime import datetime

class Block:
    def __init__(self, data):
        self.timestamp = datetime.now();
        self.data = data
        self.prevBlockHash = ''
        self.hash = self.calculateHash()

    def calculateHash(self):
        blockInfo = str(self.timestamp) + self.data + str(self.prevBlockHash)
        return sha256(blockInfo.encode('utf-8')).hexdigest()

