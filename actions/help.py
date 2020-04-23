import discord

from actions.action import AbstractAction
from actions.action_list import ActionList


class Help(AbstractAction):

    @staticmethod
    def command():
        return "/help"

    @staticmethod
    def command_short():
        return "/h"

    @staticmethod
    def help_description():
        return "Afficher cet ecran d'aide"

    @staticmethod
    def help_args():
        return [""]

    @staticmethod
    async def on_call(message, client):
        help_txt = ""
        shorts = []
        fulls = []
        descriptions = []
        for action in ActionList.actions:
            shorts.append(action.command_short() if action.command_short() is not None else "")

            full = action.command()
            if len(action.help_args()) > 1:
                full += " ["
                for arg_possibility in action.help_args():
                    full += arg_possibility + ", "
                full = full[:-2] + "]"
            elif action.help_args()[0] != "":
                full += " " + action.help_args()[0]
            fulls.append(full)

            descriptions.append(action.help_description())

        for i in range(len(shorts)):
            help_txt += "`{}` ou `{}`\n{}\n\n".format(
                shorts[i],
                fulls[i],
                descriptions[i]
            )

        embed = discord.Embed()
        embed.description = help_txt
        embed.color = discord.Color.blue()

        await message.channel.send(embed=embed)
