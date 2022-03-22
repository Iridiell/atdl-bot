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
    global bot_role
    print('We have logged in as {0.user}'.format(client))
    atdl = client.get_guild(SERVER)
    bot_channel = atdl.get_channel(CHANNEL)
    bot_role = atdl.get_role(ROLE)
    iridiel = client.get_user(IRIDIEL)
    argodog = client.get_user(422773482959667220)
# on message function
@client.event
async def on_message(message):
    global bot_channel
    global atdl
    global iridiel
    global argodog
    global bot_role
    if message.author == client.user:
        return
    
    # if message.author == argodog:
    #     await message.add_reaction("\U0001F415")
    if message.guild == atdl and message.channel == bot_channel:
        if message.author == iridiel:
            if "details" in message.content:
                await message.channel.send(atdl)
                await message.channel.send(bot_channel)
                await message.channel.send(bot_role)
        if message.content.startswith("$exit"):
            await client.close()
        if iridiel in message.mentions: 
            await message.channel.send("dont ping pls")
        if message.content.startswith("$schedule"):
            msg = message.content
            split_msg = msg.strip().split(" ")
            msg_mentions = message.role_mentions
            msg_mentions.remove(bot_role)
            msg_mentions = list(sorted(msg_mentions, key=lambda role: role.position))

            if(len(msg_mentions)) != 3:
                await message.channel.send("Need 3 parameters, 2 teams and division")
            else:
                team1 = msg_mentions[0]
                team2 = msg_mentions[1]
                division = msg_mentions[2]
                time = split_msg[split_msg.index("GMT")-1]
                await message.channel.send(team1.name)
                await message.channel.send(team2.name)
                await message.channel.send(division.name)
                await message.channel.send(time)

        if bot_role in message.role_mentions:
            await message.channel.send("you have pinged the bot role")
client.run(TOKEN)