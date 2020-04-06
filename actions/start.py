import discord

from actions.action import AbstractAction
from actions.action_list import ActionList

from game.game import Game, get_lang_dico


class Start(AbstractAction):

    @staticmethod
    def command():
        return "/start"

    @staticmethod
    def command_short():
        return "/s"

    @staticmethod
    def help_description():
        return "Commencer une partie avec une langue au choix"

    @staticmethod
    def help_args():
        return ["latin", "fanf", "poke"]

    @staticmethod
    async def on_call(message, client):
        # get singleton game
        game = Game()

        # get language if any
        split = message.content.split()
        if len(split) > 1:
            game.lang = split[1]
        else:
            game.lang = "fanf"

        # start game
        print('Start game')
        await game.start()

        embed = discord.Embed()
        embed.title = "Jouons ensemble"
        embed.description = "Les mots sont `{}`".format(", ".join(game.dico))
        embed.color = 10751

        await message.channel.send(embed=embed)
