import nextcord
from nextcord.ext import commands
import os
from config import token, status, prefix

client = commands.Bot(command_prefix=str(prefix), intents=nextcord.Intents.all())
client.remove_command('help')

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

@client.event
async def on_ready():
    print('Online')
    aktywność = nextcord.Game(name=str(status))
    await client.change_presence(activity=aktywność)

@client.command()
async def help(ctx):
    await ctx.send(f"``/ankieta``\n``/embed``\n``/reroll``\n``{prefix}ban <osoba>``\n``{prefix}kick <osoba>``\n``{prefix}clear <ilość>``\n``{prefix}tickety_ustaw``\n``{prefix}weryfikacja_ustaw``\n``{prefix}giveaway``")

client.run(str(token))