import discord
import os
from dotenv import load_dotenv
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
load_dotenv()

iridiel = client.get_user(260402732047794176)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if iridiel in message.mentions:
        await message.channel.send('Dont ping him!')
    if message.content.startswith("$exit"):
        await client.close()
    if message.content == "a":
        id = message.author.id
        print(id)
        user = await client.fetch_user(id)
        await message.channel.send(user.mention)
client.run(os.getenv('TOKEN'))