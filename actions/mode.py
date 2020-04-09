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
        footer = None

        # get ongoing game
        game = GameList.games.get(message.channel)

        if game:
            # get argument
            split = message.content.split()
            if len(split) == 1:
                # no argument --> info
                description = "Mode de jeu `{}`".format(game.mode)
                color = discord.Color.green()
            elif len(split) == 2:
                if split[1] in ["strict", "sympa"]:
                    # 1 argument --> set
                    game.mode = split[1]
                    description = "Nouveau mode de jeu `{}`".format(game.mode)
                    color = discord.Color.green()
                else:
                    # 1 other --> invalid
                    description = "Argument invalide"
                    color = discord.Color.red()
                    footer = "Mode de jeu " + game.mode
            else:
                # more --> invalid
                description = "Arguments invalides"
                color = discord.Color.red()
                footer = "Mode de jeu " + game.mode
        else:
            description = "Aucune partie en cours"
            color = discord.Color.orange()
            footer = "Créez une partie avec /start ou /s"

        # create embed
        embed = discord.Embed()
        embed.description = description
        embed.color = color
        if footer:
            embed.set_footer(text=footer)

        await message.channel.send(embed=embed)
