import discord
from discord.ext import commands
import os
import numpy as np

print("\nParalelogramos Bot:\n -> Bot Privado del servidor Paralelogramos.\n -> Bot desarrollado por Gondoraragorn#1173.\n -> Invitación al servidor de Paralelogramos: https://discord.gg/PgCBfVErYd \n")
print("Bot Starting...")
client = commands.Bot(command_prefix='.', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bot en desarrollo por Newtoniano'))
    print('Bot is Online')
    print(f"Ping: {np.round(client.latency * 1000)}ms")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')
        print(f"Error: Please pass in all required arguments // by {ctx.message.author}")
    if isinstance(error, commands.MissingRole):
        await ctx.send('Insuficient Permissions')
        print(f"Error: Insuficient Permissions //  by {ctx.message.author}")
    if isinstance(error, commands.CommandNotFound):
        print(f"Error: Command does not exist //  by {ctx.message.author}")
        await ctx.send('Command does not exist')
    if isinstance(error, commands.MemberNotFound):
        print(f"Error: Member not found // by {ctx.message.author}")
        await ctx.send('Member not found')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    HelpCommand = discord.Embed(title="__Paralelogramos Bot Help__", description="Bot exclusivo del servidor Paralelogramos. Los comandos estan a continuación: ", color=0x00ff00)
    HelpCommand.add_field(name="**Fun:**", value="iq -> Te dice el IQ que aparentas\n search -> Buscar algo en google\n yopino -> Hace falta definir esto?", inline=False)
    HelpCommand.add_field(name="**Info:**", value="ping -> Ver la latencia del Bot \n time -> Hora actual \n link -> Invitación al servidor\n avatar -> Ver el avatar de alguien\n invite -> Pedir una invitación al servidor de un solo uso\n minecraft -> La ip del servidor de minecraft\n poll -> Iniciar una votación", inline=False)
    HelpCommand.add_field(name="Este Bot sigue en desarrollo por [👑] Newtoniano , esta es una versión beta", value="Para cualquier problema hablen con Administración o Moderación", inline=False)
    HelpCommand.set_image(url="https://cdn.discordapp.com/attachments/710493297520410644/841686804980695090/tenor.gif")
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

@client.command()
@commands.has_role("Bot Perms")
async def stop(ctx):
    await ctx.send('Bot status is turning offline. See you!')
    exit()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    client.run('NzEwMTI0NDY0MTAwMzQzODQ5.Xrv48Q.NtA7iy49OJ3Uo9jh60GLQ4XRQYY')
