import discord
from discord.ext import tasks

import os
import subprocess
from subprocess import PIPE
from utils import coloredString

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

@tasks.loop(seconds=3.0)
async def loop():
    proc = subprocess.run("sh sshlogin_notify.sh", shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    result = proc.stdout
    if not result:
        pass
    else:
        for splStr in result.splitlines():
            sendMessage = coloredString(splStr)
            await send_message(sendMessage)


async def send_message(message):
    await client.get_channel(CHANNEL).send('{}'.format(message))

if __name__ == '__main__':
    client.run(os.environ['DISCORD_TOKEN'])


