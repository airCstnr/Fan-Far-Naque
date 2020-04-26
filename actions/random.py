import random

import discord

from actions.action import AbstractAction
from actions.action_list import ActionList

from game.game import Game, GameList


class Random(AbstractAction):

    @staticmethod
    def command():
        return "/random"

    @staticmethod
    def command_short():
        return "/r"

    @staticmethod
    def help_description():
        return ":twisted_rightwards_arrows: Activer/Desactiver le mode aléatoire"

    @staticmethod
    def help_args():
        return [""]

    @staticmethod
    async def on_call(message, client):
        footerText = None

        # get ongoing game
        game = GameList.games.get(message.channel)

        if game:
            # toggle random mode
            description = "Mode aléatoire "
            if not game.random:
                game.random = True
                description += "activé :twisted_rightwards_arrows:"
            else:
                game.random = False
                description += "désactivé :arrow_right:"
            color = discord.Color.blue()
        else:
            description = "Aucune partie en cours"
            color = discord.Color.orange()
            footerText = "Créez une partie avec /start ou /s"

        # create embed
        embed = discord.Embed()
        embed.description = description
        embed.color = color
        if footerText:
            embed.set_footer(text=footerText)

        # send embed
        await message.channel.send(embed=embed)

        # prompt new random item
        if game and game.random:
            await game.newRandItem(message)
