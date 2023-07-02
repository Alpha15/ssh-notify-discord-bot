import discord
from discord.ext import tasks

import os
from datetime import date
import time
import subprocess
from subprocess import PIPE

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)

CHANNEL = int(os.environ['CHANNEL'])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("----------")
    send_notify.start()

@tasks.loop(seconds=3.0)
async def send_notify():
    proc = subprocess.run("sh sshlogin_notify.sh", shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    result = proc.stdout
    if not result:
        pass
    else:
        await client.get_channel(CHANNEL).send('{}'.format(result))

if __name__ == '__main__':
    client.run(os.environ['DISCORD_TOKEN'])


