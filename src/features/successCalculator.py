
from ..utils.constants import \
    BASIC, CRITICAL, EXTREME, IMPOSSIBLE, WHATAHERO, DIESIZE



def sortRolls(rolls):
    sortedRolls = {n:0 for n in range(1, DIESIZE + 1)}

    for roll in rolls:
        sortedRolls[roll] += 1

    return sortedRolls


def countSuccess(sortedRolls):
    successes = {n:0 for n in range(7)}

    for numberOfFace in sortedRolls.values():

        if numberOfFace > 6:
            successes[6] += 1
        else:
            successes[numberOfFace] += 1

    return successes



def calculateSuccess(rolls):

    sortedRolls = sortRolls(rolls)
    successes = countSuccess(sortedRolls)

    return {BASIC:successes[2], CRITICAL:successes[3],\
        EXTREME:successes[4],  IMPOSSIBLE:successes[5], \
            WHATAHERO:successes[6]}




def calculateRiskySuccess(rolls, riskedSuccess):

    successes = calculateSuccess(rolls)

    successes[riskedSuccess] -= 1
    if successes[riskedSuccess] < 0: successes[riskedSuccess] = 0

    return successes




def calculateAllOrNothing(newRolls, oldRolls):

    oldSortedRolls = sortRolls(oldRolls)
    newSortedRolls = sortRolls(newRolls)

    for face in newSortedRolls.keys():
        if newSortedRolls[face] == oldSortedRolls[face]:
            newSortedRolls[face] = 0

    successes = countSuccess(newSortedRolls)

    return {BASIC: successes[2], CRITICAL: successes[3], \
        EXTREME: successes[4],  IMPOSSIBLE: successes[5], \
            WHATAHERO: successes[6]}
