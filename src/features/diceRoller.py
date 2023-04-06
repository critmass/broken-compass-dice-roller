from random import randrange
from ..utils.constants import DIESIZE, COIN
from .successCalculator import sortRolls

MAXROLL = DIESIZE+1
MINROLL = 1



def roll(diceToRoll):
    diceRolled = [randrange(MINROLL, MAXROLL) for die in range(diceToRoll)]

    return diceRolled



def reroll(oldDiceRolled):
    diceRolled = oldDiceRolled.copy()
    indexOfRerolls = []

    faces = sortRolls(diceRolled)

    for face in faces.keys():

        if faces[face] == 1:
            i = diceRolled.index(face)

            indexOfRerolls.append(i)

    for i in indexOfRerolls:
        diceRolled[i] = randrange(MINROLL, MAXROLL)

    return diceRolled


def flip(): return COIN[randrange(2)]