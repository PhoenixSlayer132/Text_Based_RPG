import random

# Dict #
user = None
opponent = None

# Misc #
searching = True
playerDefending = False
monsterDefending = False
playerInit = False
monsterInit = False

# Methods #
startBat = None

# Creation System #
basePlayerLvl = 1
basePlayerHP = 20
basePlayerDF = random.randint(3, 5)
basePlayerSPD = random.randint(3, 5)
basePlayerATK = random.randint(3, 7)

# Leveling System #
levelMeter = 0.0
playerLVL = 1

def lvlStats():
    user.lvl = playerLVL
    user.hp = basePlayerHP * playerLVL
    user.df = basePlayerDF * playerLVL
    user.spd = basePlayerSPD * playerLVL
    user.atk = basePlayerATK * playerLVL

# Monster Stats #
## Entry
monstELvl = 1
monstEHP = random.randint(15, 30)
monstEDF = random.randint(1, 2)
monstESPD = random.randint(1, 5)
monstEATK = random.randint(1, 5)

## Beginner
monstBLvl = random.randint(1, 3)
monstBHP = random.randint(15, 30) * monstBLvl
monstBDF = random.randint(1, 5) * monstBLvl
monstBSPD = random.randint(3, 7) * monstBLvl
monstBATK = random.randint(3, 7) * monstBLvl

## Intermediate
monstILvl = random.randint(4, 6)
monstIHP = random.randint(20, 35) * monstILvl
monstIDF = random.randint(3, 7) * monstILvl
monstISPD = random.randint(5, 9) * monstILvl
monstIATK = random.randint(5, 9) * monstILvl

## Boss Monsters ##
bossMonstLvl = random.randint(4, 6)
bossMonstHP = random.randint(20, 35) * playerLVL
bossMonstDF = random.randint(3, 7) * playerLVL
bossMonstSPD = random.randint(5, 9) * playerLVL
bossMonstATK = random.randint(5, 9) * playerLVL

# Monster Stats Randomizers #

def randomizeE():
    global monstEHP, monstEDF, monstESPD, monstEATK
    monstEHP = random.randint(15, 30)
    monstEDF = random.randint(1, 2)
    monstESPD = random.randint(1, 5)
    monstEATK = random.randint(1, 5)

def randomizeB():
    global monstBLvl, monstBHP, monstBDF, monstBSPD, monstBATK
    monstBLvl = random.randint(1, 3)
    monstBHP = random.randint(15, 30) * monstBLvl
    monstBDF = random.randint(1, 5) * monstBLvl
    monstBSPD = random.randint(3, 7) * monstBLvl
    monstBATK = random.randint(3, 7) * monstBLvl

def randomizeI():
    global monstILvl, monstIHP, monstIDF, monstISPD, monstIATK
    monstILvl = random.randint(4, 6)
    monstIHP = random.randint(20, 35) * monstILvl
    monstIDF = random.randint(3, 7) * monstILvl
    monstISPD = random.randint(5, 9) * monstILvl
    monstIATK = random.randint(5, 9) * monstILvl
