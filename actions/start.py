import discord

from actions.action import AbstractAction
from actions.action_list import ActionList

from game.game import Game, GameList, get_lang_dico, languages


def lang_names():
    lang_names = []
    for lang in languages:
        lang_names.append(lang[0])
    return lang_names


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
        return lang_names()

    @staticmethod
    async def on_call(message, client):
        # create game and add it to games list
        game = Game()
        GameList.games[message.channel] = game

        # get language if any
        split = message.content.split()
        if len(split) > 1:
            if split[1] in lang_names():
                game.lang = split[1]
            else:
                embed = discord.Embed()
                embed.description = "Langue inconnue"
                embed.color = discord.Color.red()
                await message.channel.send(embed=embed)
                return

        # start game
        print('Start game')
        await game.start()

        embed = discord.Embed()
        embed.title = "Jouons ensemble"
        embed.description = "Les mots sont `{}`".format(", ".join(game.dico))
        embed.color = discord.Color.green()
        embed.set_footer(text="Niveau de jeu " + game.niveau)

        await message.channel.send(embed=embed)
