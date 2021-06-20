import discord
from discord.ext import commands
from os import listdir
from numpy import round
from discord_slash import SlashCommand

if __name__ == '__main__':
    client = commands.Bot(command_prefix='.', help_command=None)
    slash = SlashCommand(client, sync_commands=True)
    HelpCommand = discord.Embed(title="__Paralelogramos Bot Help__", description="Bot exclusivo del servidor Paralelogramos. Los comandos estan a continuación: ", color=0x00ff00)
    HelpCommand.add_field(name="**Fun:**", value="iq -> Te dice el IQ que aparentas\n search -> Buscar algo en google\n yopino -> Hace falta definir esto?", inline=False)
    HelpCommand.add_field(name="**Info:**", value="ping -> Ver la latencia del Bot \n time -> Hora actual \n link -> Invitación al servidor\n avatar -> Ver el avatar de alguien\n invite -> Pedir una invitación al servidor de un solo uso\n minecraft -> La ip del servidor de minecraft\n poll -> Iniciar una votación", inline=False)
    HelpCommand.add_field(name="Este Bot sigue en desarrollo por [👑] Newtoniano , esta es una versión beta", value="Para cualquier problema hablen con Administración o Moderación", inline=False)
    HelpCommand.set_image(url="https://cdn.discordapp.com/attachments/710493297520410644/841686804980695090/tenor.gif")

@client.event
async def on_ready():
    print('Bot is Online')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bot Privado de Paralelgoramos'))
    print(f"Ping: {int(round(client.latency * 1000))}ms")

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

#@slash.slash(name="Ping", description="Latencia del Bot")
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {int(round(client.latency * 1000))}ms')
"""
@slash.slash()
async def ping(ctx, theme=None):
    try:
        await ctx.send(f'Pong! {int(round(client.latency * 1000))}ms')
    except:
        await ctx.send("Error")

@slash.slash()
async def test(ctx):
    await ctx.send("Test")
"""
@slash.slash()
async def help(ctx, theme=None):
    await ctx.send(embed=HelpCommand)

@client.command()
async def help(ctx, theme=None):
    await ctx.send(embed=HelpCommand)

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded extension: {extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded extension: {extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def stop(ctx):
    await ctx.send('Bot status is turning offline. See you!')
    print("Bot status turning offline\n Shutting Down...")
    await client.close()
    
Ed_Moriarty = client.get_emoji(id="822892042182459512")

if __name__ == '__main__':
    print("\nParalelogramos Bot:\n -> Bot Privado del servidor Paralelogramos.\n -> Bot desarrollado por Gondoraragorn#1173.\n -> Invitación al servidor de Paralelogramos: https://discord.gg/PgCBfVErYd \n")
    print("Bot Starting...")
    for filename in listdir('./cogs'):
        if filename.endswith('.py') and filename != 'Python_Bot.py' and filename != '__init__.py':
            client.load_extension(f'{filename[:-3]}')

    #ENCODED_KEY='TnpFd01USTBORFkwTVRBd016UXpPRFE1LlhydjQ4US5OdEE3aXk0OU9KM1VvOWpoNjBHTFE0WFJRWVk='
    #KEY = str(base64.b64decode(ENCODED_KEY))
    KEY = "NzEwMTI0NDY0MTAwMzQzODQ5.Xrv48Q.NtA7iy49OJ3Uo9jh60GLQ4XRQYY"
    client.run(KEY.format(str))