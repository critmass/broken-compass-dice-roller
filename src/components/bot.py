import os
import discord
from discord.ext import commands

from ..content.descriptions import rollDescription, flipDescription
from .responses import rollResponse, flipResponse

TOKEN = os.environ.get("DISCORD_TOKEN")


def runDiscordBot():
    token = TOKEN
    bot = commands.Bot()

    @bot.slash_command(name = "roll", description = rollDescription)
    async def roll(context, dice):
        try:
            diceToRoll = int(dice)
            response, buttons = rollResponse(diceToRoll)
            await context.respond(response, view=buttons)
        except Exception as err:
            print(err)

    @bot.slash_command(name = "flip", description = flipDescription)
    async def flip(context):
        await context.respond(flipResponse())

    bot.run(token)
