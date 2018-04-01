from Block import Block

class Blockchain:
    def __init__(self):
        self.blocks = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block("genesisBlock")

    def addBlockToChain(self, Block):
        Block.prevBlockHash = self.blocks[-1].hash
        Block.hash = Block.calculateHash()
        self.blocks.append(Block)

    def validate(self):
        i = 1
        while i < len(self.blocks):
            currentBlock = self.blocks[i]
            prevBlock = self.blocks[i-1]

            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.prevBlockHash != prevBlock.hash:
                return False
            i += 1
        return True

    def print(self):
        i = 0
        while i < len(self.blocks):
            Block = self.blocks[i]
            print("BLOCK " + str(i) + ": ")
            print("    hash: " + Block.hash)
            print("    prevHash: " + Block.prevBlockHash)
            print("    data: " + Block.data)
            i += 1
