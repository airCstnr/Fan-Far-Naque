import sys
import json


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
]

def get_lang_dico(lang):
    for name, words_list in languages:
        if lang == name:
            return words_list


@singleton
class Game():

    game_started = False
    current_state = 0

    def __init__(self):
        print("Init", __class__.__name__)
        self.dico = get_lang_dico("fanf")
        with open('order.json') as f:
            data = json.load(f)
            self.order = data['order']

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
                await message.channel.send("Bravo, tu es arrivé au bout du jeu!")
                return
            # ok, continue the game
            #await message.channel.send("Super, continue!")
            return
        else:
            # you lost the game
            self.current_state = 0
            await message.channel.send("Raté! Tu en étais à {0}, recommence!".format(cur_state[1]))
            return
