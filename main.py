import discord
import os
from replit import db
from keep_alive import keep_alive
from update_cock import update_cock

intent=discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)

#member IDs
squidID = 248584896409370624
kaiID = 493298384019652609

woeID = 250142648701026304
landriID = 703752834532769892

floochooID = 260955153111187457

#bot startup
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

#on message
@client.event
async def on_message(message):
    #ignores self
  if message.author == client.user:
    return

  #individual cocks
  if message.author.id == squidID:
    update_cock("squid")
    squidCock = db["squid"]
    await message.channel.send(f"Squid cock! \nSquid has a {squidCock} inch cock!")
  elif message.author.id == landriID:
    update_cock("landri")
    landriCock = db["landri"]
    await message.channel.send(f"Landri cock! \nLandri has a {landriCock} inch cock!")
  elif message.author.id == floochooID:
    update_cock("floochoo")
    floochooCock = db["floochoo"]
    await message.channel.send(f"Floochoo cock! \nFloochoo has a {floochooCock} inch cock!")
  else:
    return

my_secret = os.environ["botToken"]
keep_alive()
client.run(my_secret)