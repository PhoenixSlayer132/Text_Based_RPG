import random

# Dict #
user = None
opponent = None

# Misc #
searching = True

# Methods #
startBat = None

# Creation System #
basePlayerLvl = 1
basePlayerHP = 20
basePlayerDF = random.randint(3, 5)
basePlayerSPD = random.randint(3, 5)
basePlayerATK = random.randint(3, 7)

# Monster Stats #
## Entry
monstELvl = 1
monstEHP = random.randint(15, 30)
monstEDF = random.randint(1, 3)
monstESPD = random.randint(1, 5)
monstEATK = random.randint(1, 5)
## Beginner
monstBLvl = random.randint(1, 3)
monstBHP = random.randint(15, 30) * monstBLvl
monstBDF = random.randint(3, 7) * monstBLvl
monstBSPD = random.randint(3, 7) * monstBLvl
monstBATK = random.randint(3, 7) * monstBLvl
## Intermediate
monstILvl = random.randint(4, 6)
monstIHP = random.randint(20, 35) * monstILvl
monstIDF = random.randint(5, 9) * monstILvl
monstISPD = random.randint(5, 9) * monstILvl
monstIATK = random.randint(5, 9) * monstILvl

# Leveling System #
levelMeter = 0.0
playerLVL = 1
playerHP = 0
playerDF = 0
playerSPD = 0
playerATK = 0

def lvlStats():
    global playerHP, playerDF, playerSPD, playerATK

    playerHP = basePlayerHP * playerLVL
    playerDF = basePlayerDF * playerLVL
    playerSPD = basePlayerSPD * playerLVL
    playerATK = basePlayerATK * playerLVL

    user.lvl = playerLVL
    user.hp = playerHP
    user.df = playerDF
    user.spd = playerSPD
    user.atk = playerATK