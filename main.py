import discord
from decouple import config

discord_token = config('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  user_name = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{user_name}: {user_message} ({channel})')

  if message.author == client.user:
    return
  if message.channel.name == "scores-and-chokes":
    if message.content.startswith("!help"):
      await message.channel.send("On my way "+user_name)
      return

client.run(discord_token)