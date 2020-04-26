import sys
import json
import random

import discord

# -------------------------- SINGLETON ---------------------------------
def singleton(className):
    """ Holds singletons of className objects """
    instances = {}
    def get_instance():
        if className not in instances:
            instances[className] = className()
        return instances[className]
    return get_instance


# -------------------------- LANG --------------------------------------
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


# -------------------------- ORDER -------------------------------------
def order():
    with open('order.json') as f:
            data = json.load(f)
            return data['order']

# instanciate it once
order = order()


# -------------------------- GAME LIST ---------------------------------
class GameList:
    games = {}


# -------------------------- GAME --------------------------------------
class Game():
    game_started = False
    current_state = 0
    lang = "fanf"
    niveau = "facile"
    random = False
    order = order


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
            if not self.random:
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

            else:
                await self.nextRandomItem(message)
                return

        else:
            # message is erroneous
            msg = "Tu en étais à {0}.\n\n".format(cur_state[1])

            if self.niveau == "difficile":
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


    async def nextRandomItem(self, message):
        current_item = self.order[self.current_state][1]
        next_item = self.order[self.current_state + 1][1]
        if current_item != next_item:
            # current item is finised, continue with another random item
            await self.newRandItem(message)
        else:
            # continue current item
            self.current_state+=1


    async def newRandItem(self, message):
        # get a random index between 0 and len(order)
        index = random.randrange(len(self.order))

        # set current value to first element of value pointed by index
        current_value = self.order[index][1]
        while current_value == self.order[index-1][1]:
            index -= 1
            current_value = self.order[index][1]

        # set game state to index
        self.current_state = index

        description = current_value
        color = discord.Color.blue()

        # create embed
        embed = discord.Embed()
        embed.title = "Donne moi la valeur"
        embed.description = description
        embed.color = discord.Color.blue()

        await message.channel.send(embed=embed)
