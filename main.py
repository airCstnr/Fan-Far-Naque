import sys

import discord

from actions.action_list import ActionList

# Don't orget to include here your new actions
from actions.help import Help
from actions.start import Start

from game import Game


# Check if token was given
if len(sys.argv) < 2:
    print("ERROR: Missing token")
    print("Usage: python3 main.py TOKEN [, --test]")
    exit()

TOKEN = sys.argv[1]
test_mode = False

# Check test mode
if len(sys.argv) > 2 and sys.argv[2] == "--test":
    test_mode = True

client = discord.Client()

if test_mode:
    # Add logging system
    import logging
    logging.basicConfig(level=logging.DEBUG)


# Add here your different actions
ActionList.add_action(Help)
ActionList.add_action(Start)


def action_called(action, message_content):
    first_word = message_content.split()[0]
    full = first_word == ("test" if test_mode else "") + action.command()
    short = action.command_short() is not None and \
            first_word == ("test" if test_mode else "") + action.command_short()
    return full or short


async def parse_command(message):
    for action in ActionList.actions:
        if action_called(action, message.content):
            await action.on_call(message, client)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # get ongoing game
    game = Game()
    if game.game_started:

        # check if message is part of the game
        if message.content not in ["fan", "far", "naque"]:
            return

        # get current state
        cur_state = game.order[game.current_state]
        if message.content == cur_state[0]:
            # if message is correct, go to next item
            game.current_state+=1
            # avoid out of range
            if game.order[game.current_state][0] == "END":
                game.game_started = False
                await message.channel.send("Bravo, tu es arrivé au bout du jeu!")
                return
            # ok, continue the game
            #await message.channel.send("Super, continue!")
            return
        else:
            # you lost the game
            game.current_state = 0
            await message.channel.send("Raté! Tu en étais à {0}, recommence!".format(cur_state[1]))
            return

    await parse_command(message)


@client.event
async def on_ready():
    print()
    print('Logged in as', client.user.name)
    print('with id', client.user.id)
    print('READY')
    print()


client.run(TOKEN)
