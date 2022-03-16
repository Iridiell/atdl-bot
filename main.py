import discord
import os
from dotenv import load_dotenv
import discord
import logging
 
# Initializing logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Initial setup
intents = discord.Intents.all()
intents.guild_typing = False
intents.dm_typing = False
intents.presences = False
intents.typing = False
print("a")
client = discord.Client(intents=intents)
load_dotenv()
# Getting ID from .env
SERVER=int(os.getenv('GUILD_ID').strip())
ROLE=int(os.getenv('ROLE').strip())
IRIDIEL=int(os.getenv('IRIDIEL').strip())
TOKEN = os.getenv('TOKEN').strip()
CHANNEL = int(os.getenv('CHANNEL').strip())

# on ready function
@client.event
async def on_ready():
    global bot_channel
    global atdl
    global iridiel
    global argodog
    global role
    print('We have logged in as {0.user}'.format(client))
    atdl = client.get_guild(SERVER)
    bot_channel = atdl.get_channel(CHANNEL)
    role = atdl.get_role(ROLE)
    iridiel = client.get_user(IRIDIEL)
    argodog = client.get_user(422773482959667220)
# on message function
@client.event
async def on_message(message):
    global bot_channel
    global atdl
    global iridiel
    global argodog
    global role
    if message.author == client.user:
        return
    
    # if message.author == argodog:
    #     await message.add_reaction("\U0001F415")
    if message.guild == atdl and message.channel == bot_channel:
        if message.author == iridiel:
            if "details" in message.content:
                await message.channel.send(atdl)
                await message.channel.send(bot_channel)
                await message.channel.send(role)
        if message.content.startswith("$exit"):
            await client.close()
        if iridiel in message.mentions: 
            await message.channel.send("dont ping pls")
        if role in message.role_mentions:
            await message.channel.send("you have pinged the bot role")
client.run(TOKEN)