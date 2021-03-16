import discord
from discord.ext import commands
import time
import os

client = commands.Bot(command_prefix='.', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bot en desarrollo por Newtoniano'))
    print('Bot is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')
    if isinstance(error, commands.MissingRole):
        await ctx.send('Insuficient Permissions')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist')
    if isinstance(error, commands.MemberNotFound):
        await ctx.send('Member not found')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    HelpCommand = discord.Embed(title="__Paralelogramos Bot Help__", description="Bot exclusivo del servidor Paralelogramos. Los comandos estan a continuación: ", color=0x00ff00)
    HelpCommand.add_field(name="**Fun:**", value="iq -> Te dice el IQ que aparentas", inline=False)
    HelpCommand.add_field(name="**Info:**", value="ping -> Ver la latencia del Bot \n time -> Hora actual \n link -> Invitación al servidor\n avatar -> Ver el avatar de alguien\n invite -> Pedir una invitación al servidor de un solo uso\n minecraft -> La ip del servidor de minecraft\n poll -> Iniciar una votación", inline=False)
    HelpCommand.add_field(name="Este Bot sigue en desarrollo por [👑] Newtoniano , esta es una versión beta", value="Para cualquier problema hablen con Administración o Moderación", inline=False)
    HelpCommand.set_image(url="https://cdn.discordapp.com/attachments/695641854045061150/787416144163110912/Sin_titulo.mp4.gif")
    await ctx.send(embed=HelpCommand)

@client.command()
@commands.has_role("Bot Perms")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded extension: {extension}')

@client.command()
@commands.has_role("Bot Perms")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded extension: {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('NzEwMTI0NDY0MTAwMzQzODQ5.Xrv48Q.NtA7iy49OJ3Uo9jh60GLQ4XRQYY')
