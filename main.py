import discord
from discord.ext import tasks

import os
import subprocess
from utils import coloredString
from utils import commandWho
from utils import commandCheckAuth

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)

CHANNEL = int(os.environ['CHANNEL'])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("----------")
    loop.start()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "!who":
        await message.reply(commandWho())


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


