import discord
import os
from datetime import date
import time

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("-----")

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send('Hello')

if __name__ == '__main__':
    client.run(os.environ['DISCORD_TOKEN'])
