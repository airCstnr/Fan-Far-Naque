import sys
import json
import discord


def singleton(className):
    """ Holds singletons of className objects """
    instances = {}
    def get_instance():
        if className not in instances:
            instances[className] = className()
        return instances[className]
    return get_instance


latin = ["i", "v", "x", "l", "c", "d", "m"]
languages = [
    ("latin", latin),
    ("fanf", ["fan", "far", "naque", "gre", "noble", "cd", "troll"]),
    ("poke", ["po", "ke", "mon", "gotta", "catch", "em", "all"]),
    ("ombi", ["om", "bi", "chou", "à", "la", "cr", "ème"]),
]

def get_lang_dico(lang):
    for name, words_list in languages:
        if lang == name:
            return words_list
    return latin


class GameList:
    games = {}


class Game():

    game_started = False
    current_state = 0
    lang = "fanf"
    mode = "sympa"

    def __init__(self):
        print("Init", __class__.__name__)
        with open('order.json') as f:
            data = json.load(f)
            self.order = data['order']

    async def start(self):
        self.dico = get_lang_dico(self.lang)
        self.game_started = True
        self.current_state = 0


    async def evaluate(self, message):
        # check if message is part of the game
        if message.content not in self.dico:
            return

        # get the appropriate latin word
        for lat_word, lang_word in zip(latin, self.dico):
            if message.content == lang_word:
                word = lat_word
                break

        # get current state
        cur_state = self.order[self.current_state]
        if word == cur_state[0]:
            # if message is correct, go to next item
            self.current_state+=1

            # avoid out of range
            if self.order[self.current_state][0] == "END":
                self.game_started = False

                embed = discord.Embed()
                embed.title = "Bravo"
                embed.description = "Tu es arrivé au bout du jeu!"
                embed.color = discord.Color.green()
                await message.channel.send(embed=embed)
                return

            # ok, continue the game
            return

        else:
            msg = "Tu en étais à {0}.\n\n".format(cur_state[1])

            if self.mode == "strict":
                # you lost the game
                self.current_state = 0
                msg += "Recommence!"
                color = discord.Color.red()
            else:
                msg += "Continue!"
                color = discord.Color.orange()

            embed = discord.Embed()
            embed.title = "Raté"
            embed.description = msg
            embed.color = color
            await message.channel.send(embed=embed)
            return
