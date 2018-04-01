from Blockchain import Blockchain
from Block import Block
from datetime import datetime

chain = Blockchain()

chain.addBlockToChain(Block("second block"))
chain.addBlockToChain(Block("third block"))
chain.addBlockToChain(Block("fourth block"))

chain.print()
print(chain.validate())

chain.blocks[2].data = "corrupt data"

chain.print()
print(chain.validate())
