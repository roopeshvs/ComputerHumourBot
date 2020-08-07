import discord
from discord.ext import commands
import configparser
import random
import ftfy #Convert Bad Unicode to Good Unicode

client = commands.Bot(command_prefix = '{}')

#Get Secret Token From Config File
config = configparser.ConfigParser()
config.read('token.config')
token = config['DISCORD']['TOKEN']

#We delete default help command
client.remove_command('help')

#Responds With A Random Quote
@client.command()
async def quote(ctx):
    responses = open('quotes.txt','r').read().splitlines()
    random.seed(a=None)
    response = ftfy.fix_encoding(random.choice(responses))
    await ctx.send(response)

#Embeded help with list and details of commands
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='{}quote', value='Get inspired by a powerful quote', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def add(ctx, a:int, b:int):
    await ctx.send(a+b)

@client.command()
async def sub(ctx, a:int, b:int):
    await ctx.send(a-b)

#Reacts <3 to any message
@client.event
async def on_message(ctx):
    if 'QuoteBot' in ctx.content:
        emoji ='\N{HEAVY BLACK HEART}'
        await ctx.add_reaction(emoji)
    await client.process_commands(ctx)

#Greeting On New Member Joining
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Hello, World. Here's {member.mention}!""")


client.run(token)