import discord
from decouple import config

discord_token = config('DISCORD_TOKEN')
client = discord.Client()

#let us know if bot has gone online
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#listens for all messegaes sent
@client.event
async def on_message(message):
  user_name = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{user_name}: {user_message} ({channel})')

  #doesn't replay to it's own messages
  if message.author == client.user:
    return
  #limits the channel where methode can be called
  if message.channel.name == "scores-and-chokes":
    if message.content.startswith("!help"):
      await message.channel.send("On my way "+user_name)
      return

#starts bot
client.run(discord_token)