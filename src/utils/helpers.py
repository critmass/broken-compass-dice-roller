from .constants import REROLL, RISKROLL, ALL_OR_NOTHING



REROLL_DISALLOWED = True
RISK_DONE = True
REROLL_ALLOWED = False
RISK_NOT_DONE = False



def rollsAllowed(rollType):

    if rollType == REROLL:
        return REROLL_DISALLOWED, RISK_NOT_DONE
    elif rollType == RISKROLL or rollType == ALL_OR_NOTHING:
        return REROLL_DISALLOWED, RISK_DONE
    else:
        return REROLL_ALLOWED, RISK_NOT_DONE



async def respondToButtonClick(view, interaction, response, buttons=None):
    selfID = interaction.message.id

    await interaction.response.send_message(response, view=buttons)

    for child in view.children:
        child.disabled = True

    await interaction.followup.edit_message(selfID, view=view)
