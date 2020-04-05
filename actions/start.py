from actions.action import AbstractAction
from actions.action_list import ActionList


class Start(AbstractAction):

    @staticmethod
    def command():
        return "/start"

    @staticmethod
    def command_short():
        return "/s"

    @staticmethod
    def help_description():
        return "Commencer une partie"

    @staticmethod
    def help_args():
        return [""]

    @staticmethod
    async def on_call(message, client):
        help_txt = "Jouons ensemble!"

        await message.channel.send(help_txt)
