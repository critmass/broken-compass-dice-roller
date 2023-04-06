import discord

from ..features.successCalculator import *
from ..features.diceRoller import *
from ..utils.helpers import rollsAllowed, respondToButtonClick
from ..utils.constants import \
    SUCCESSTYPES, WHATAHERO, JOINER, UNPAIRED, ALL_OR_NOTHING, \
        REGULAR_ROLL, REROLL, RISKROLL



def generateResponse(rolls, successes, rollType = REGULAR_ROLL):
    successList = [f"{key}: {successes[key]}" for key in SUCCESSTYPES]
    response = f"{rolls} {JOINER.join(successList)}"
    buttons = None
    unpaired = successes.pop(UNPAIRED)

    if successes.get(WHATAHERO) > 0:
        response = f"{rolls} Oh! What a hero!"

    elif unpaired == len(rolls):
        response = f"{rolls} Oh no! No successes!"

    elif unpaired > 0 and \
        rollType != ALL_OR_NOTHING and sum(successes.values()) > 0:

        rerollDisabled, riskDone = rollsAllowed(rollType)
        buttons = makeButtonView(\
            rolls, successes, rerollDisabled, riskDone)

    return response, buttons



def rollResponse(diceToRoll):
    if diceToRoll < 2 or diceToRoll > 9:
        return "Roll is out of range"

    diceRolled = roll(diceToRoll)
    successes = calculateSuccess(diceRolled)
    response = generateResponse(diceRolled, successes, REGULAR_ROLL)

    return response



def rerollResponse(oldRolls):

    newRolls = reroll(oldRolls)
    successes = calculateSuccess(newRolls)
    response = generateResponse(newRolls, successes, REROLL)

    return response



def riskResponse(oldRolls, oldSuccesses):

    newRolls = reroll(oldRolls)
    for success in SUCCESSTYPES:
        if oldSuccesses[success] > 0:
            success2risk = success
            break

    successes = calculateRiskySuccess(newRolls, success2risk)
    response = generateResponse(newRolls, successes, RISKROLL)

    return response



def allOrNothingResponse(oldRolls, oldSuccesses):

    newRolls = reroll(oldRolls)
    successes = calculateAllOrNothing(newRolls, oldRolls)
    response, throwAway = generateResponse(newRolls, successes, ALL_OR_NOTHING)

    return response



def flipResponse(): return f"You got {flip()}!"



def makeButtonView(rolls, successes, rerollDisabled, riskDone):

    class ButtonView(discord.ui.View):

        @discord.ui.button(label="Reroll", disabled=rerollDisabled)
        async def rerollButtonCallback(self, button, interaction):

            response, buttons = rerollResponse(rolls)

            await respondToButtonClick(self, interaction, response, buttons)

        if riskDone:
            @discord.ui.button(label="All or Nothing", disabled=False)
            async def allOrNothingButtonCallback(self, button, interaction):

                response = allOrNothingResponse(rolls, successes)

                await respondToButtonClick(self, interaction, response)

        else:
            @discord.ui.button(label="Risk", disabled=False)
            async def riskButtonCallback(self, button, interaction):

                response, buttons = riskResponse(rolls, successes)

                await respondToButtonClick(self, interaction, response, buttons)

    return ButtonView()
