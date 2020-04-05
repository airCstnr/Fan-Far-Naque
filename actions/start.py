from actions.action import AbstractAction
from actions.action_list import ActionList

from game import Game, get_lang_dico


class Start(AbstractAction):

    @staticmethod
    def command():
        return "/start"

    @staticmethod
    def command_short():
        return "/s"

    @staticmethod
    def help_description():
        return "Commencer une partie avec une langue au choix " + \
            "(latin, fanf, poke)"

    @staticmethod
    def help_args():
        return ["[game]"]

    @staticmethod
    async def on_call(message, client):
        # get singleton game
        game = Game()

        # get language if any
        split = message.content.split()
        if len(split) > 1:
            game.dico = get_lang_dico(split[1])

        # start game
        print('Start game')
        game.game_started = True
        game.current_state = 0

        help_txt = "Jouons ensemble! Les mots dispo sont `" + \
            ", ".join(game.dico) + \
            "`"

        await message.channel.send(help_txt)
