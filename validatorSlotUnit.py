from StakeHashUtils import StakeHashUtils

class ValidatorSlotUnit():
    def __init__(self,publicKey,iteration,lastBlockHash):
        self.publicKey = str(publicKey)
        self.iteration = iteration
        self.lastBlockHash = str(lastBlockHash)
    
    def validatorSlotHash(self):
        hashData = self.publicKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = StakeHashUtils.hash(hashData).hexdigest()
        return hashData