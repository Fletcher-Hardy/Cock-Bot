import discord
import os
from keep_alive import keep_alive

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
    await message.channel.send("squid cock!")
  elif message.author.id == landriID:
    await message.channel.send("landri cock!")
  elif message.author.id == floochooID:
    await message.channel.send("floochoo cock!")
  else:
    return

my_secret = os.environ["botToken"]
keep_alive()
client.run(my_secret)