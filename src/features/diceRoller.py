from random import randrange
from ..utils.constants import DIESIZE, COIN

MAXROLL = DIESIZE+1
MINROLL = 1

def roll(diceToRoll):

    diceRolled = [randrange(MINROLL, MAXROLL) for die in range(diceToRoll)]

    return diceRolled


def reroll(oldDiceRolled):
    diceRolled = oldDiceRolled.copy()
    faces = {}
    for die in diceRolled:
        faces[die] += 1
    for face in faces:
        if faces[face] == 1:
            i = diceRolled.index(faces[face])
            diceRolled[i] = randrange(MINROLL, MAXROLL)
    return diceRolled


def flip():
    return COIN[randrange(0,2)]