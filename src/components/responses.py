from ..features.successCalculator import *
from ..features.diceRoller import *
from ..utils.constants import SUCCESSTYPES, WHATAHERO, JOINER

def rollResponse(diceToRoll):
    if diceToRoll < 2 or diceToRoll > 9:
        return "Roll is out of range"

    diceRolled = roll(diceToRoll)
    successes = calculateSuccess(diceRolled)

    if successes.get(WHATAHERO) > 0:
        response = f"{diceRolled} Oh! What a hero!"

    elif sum(successes.values()) > 0:
        successList = [f"{key}: {successes[key]}" for key in SUCCESSTYPES]

        response = f"{diceRolled} { JOINER.join(successList)}"

    else: response = f"{diceRolled} Oh no! No successes!"

    return response

def rerollResponse(oldRoll):

    newRoll = reroll(oldRoll)
    successes = calculateSuccess(newRoll)

    response = f"{newRoll} {JOINER.join(successes)}"
    if successes[WHATAHERO] > 0:
        response = f"{newRoll} Oh! What a hero!"

    return response

def flipResponse():
    return f"You got {flip()}!"
