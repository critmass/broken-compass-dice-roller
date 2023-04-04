import discord
from discord.ext import commands
from ..utils.constants import TOKEN
from ..utils.descriptions import rollDescription, flipDescription
from .responses import rollResponse, flipResponse


def runDiscordBot():
    token = TOKEN
    bot = commands.Bot()

    @bot.slash_command(name = "roll", description = rollDescription)
    async def roll(context, dice):
        try:
            diceToRoll = int(dice)
            response = rollResponse(diceToRoll)
            await context.respond(response)
        except Exception as err:
            print(err)

    @bot.slash_command(name = "flip", description = flipDescription)
    async def flip(context):
        await context.respond(flipResponse())

    bot.run(token)