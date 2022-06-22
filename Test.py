from ProofOfStake import ProofOfStake
from validatorSlotUnit import ValidatorSlotUnit


if __name__ == '__main__':

    slotUnitObject = ValidatorSlotUnit('harry',1,'lasthash')
    print(slotUnitObject.validatorSlotHash())
    
    ''' posObject = ProofOfStake()
    posObject.addTokensToStake('harry', 10)
    posObject.addTokensToStake('john', 100)
    print(posObject.getStakedTokens('harry'))
    print(posObject.getStakedTokens('john'))
    print(posObject.getStakedTokens('parker')) '''

    

    