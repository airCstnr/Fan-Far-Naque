import discord

from actions.action import AbstractAction
from actions.action_list import ActionList

from game import Game


class Mode(AbstractAction):

    @staticmethod
    def command():
        return "/mode"

    @staticmethod
    def command_short():
        return "/m"

    @staticmethod
    def help_description():
        return "Choisir un mode"

    @staticmethod
    def help_args():
        return ["strict", "sympa"]

    @staticmethod
    async def on_call(message, client):
        # get mode
        split = message.content.split()
        if (len(split) == 2 and
            split[1] in ["strict", "sympa"]) :
            game = Game()
            game.mode = split[1]
            description = "Mode set to `{}`".format(split[1])
        else:
            description = "Wrong command. Use `strict` or `sympa`"

        embed = discord.Embed()
        embed.description = description
        embed.color = 10751

        await message.channel.send(embed=embed)
