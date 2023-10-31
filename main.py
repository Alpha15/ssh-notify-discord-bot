import discord
from discord.ext import tasks
from discord import app_commands

import os
import subprocess
from utils import coloredString
from utils import commandWho
from utils import commandCheckAuth

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)
tree = app_commands.CommandTree(client)

CHANNEL = int(os.environ['CHANNEL'])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("----------")
    await tree.sync()
    loop.start()

@tree.command(name="who", description="you will know who logged in")
async def _who_command(ctx:discord.Interaction):
    await ctx.response.send_message(commandWho())

@tasks.loop(seconds=3.0)
async def loop():
    result = commandCheckAuth()
    if not result:
        pass
    else:
        for preMsg in result.splitlines():
            sendMessage = coloredString(preMsg)
            await send_message(sendMessage)

async def send_message(message):
    await client.get_channel(CHANNEL).send('{}'.format(message))

if __name__ == '__main__':
    client.run(os.environ['DISCORD_TOKEN'])


