import discord

from actions.action import AbstractAction
from actions.action_list import ActionList

from game.game import Game, GameList


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
        # get ongoing game
        game = GameList.games.get(message.channel)
        if game:
            # get argument
            split = message.content.split()
            if (len(split) == 2 and
                split[1] in ["strict", "sympa"]) :
                game.mode = split[1]
                description = "Mode de jeu `{}`".format(split[1])
                color = discord.Color.green()
            else:
                description = "Arguments invalides."
                color = discord.Color.red()
        else:
            description = "Aucune partie en cours."
            color = discord.Color.orange()

        # create embed
        embed = discord.Embed()
        embed.description = description
        embed.color = color

        await message.channel.send(embed=embed)
