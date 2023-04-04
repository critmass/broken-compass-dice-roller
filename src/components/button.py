import discord
from .responses import rerollResponse
from ..utils.constants import SUCCESSTYPES

def makeButtonView(roll, successes, rerollDone = False, riskDone = False):

    class ButtonView(discord.ui.View):

        @discord.ui.button(label="Reroll", disabled = (rerollDone or riskDone))
        async def rerollButtonCallback(self, button, interaction):

            response = rerollResponse(roll)

            for child in self.children:
                child.disabled = True
            await interaction.response.edit_message(view=self)

            await interaction.respond(response)

        @discord.ui.button(label="Risk", disabled = riskDone)
        async def riskButtonCallback(self, button, interaction):

            pass

    return ButtonView
