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
        return "Aller à une valeur random"

    @staticmethod
    def help_args():
        return [""]

    @staticmethod
    async def on_call(message, client):
        footer = None

        # get ongoing game
        game = GameList.games.get(message.channel)

        if game:
            # get a random index between 0 and len(order)
            index = random.randrange(len(game.order))

            # set current value to first element of value pointed by index
            current_value = game.order[index][1]
            while current_value == game.order[index-1][1]:
                index -= 1
                current_value = game.order[index][1]

            # set game state to index
            game.current_state = index

            description = current_value
            color = discord.Color.blue()
        else:
            description = "Aucune partie en cours"
            color = discord.Color.orange()
            footer = "Créez une partie avec /start ou /s"

        # create embed
        embed = discord.Embed()
        embed.title = "Donne moi la valeur"
        embed.description = description
        embed.color = discord.Color.blue()

        await message.channel.send(embed=embed)
