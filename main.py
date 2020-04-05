import sys

import discord

from actions.action_list import ActionList

# Don't orget to include here your new actions
from actions.help import Help
from actions.start import Start


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

    await parse_command(message)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('READY')


client.run(TOKEN)
