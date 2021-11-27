import discord
from discord.ext import commands
from numpy import round
#from discord_slash import SlashCommand

if __name__ == '__main__':
    client = commands.Bot(command_prefix='.', help_command=None)
    #slash = SlashCommand(client, sync_commands=True)

HelpCommand = discord.Embed(title="__Paralelogramos Bot Help__", description="Bot exclusivo del servidor Paralelogramos. Los comandos estan a continuación: ", color=0x00ff00)
HelpCommand.add_field(name="**Fun:**", value="iq -> Te dice el IQ que aparentas\n search -> Buscar algo en google\n yopino -> Hace falta definir esto?", inline=False)
HelpCommand.add_field(name="**Info:**", value="ping -> Ver la latencia del Bot \n time -> Hora actual \n link -> Invitación al servidor\n avatar -> Ver el avatar de alguien\n invite -> Pedir una invitación al servidor de un solo uso\n minecraft -> La ip del servidor de minecraft\n poll -> Iniciar una votación", inline=False)
HelpCommand.add_field(name="**Math**", value="math -> Para ver todos los comandos de mates")
HelpCommand.add_field(name="Este Bot sigue en desarrollo por [👑] Newtoniano , esta es una versión beta", value="Para cualquier problema hablen con Administración o Moderación", inline=False)
HelpCommand.set_image(url='https://cdn.discordapp.com/attachments/695641854045061150/858449065737453568/b6b86a3ebcc9161f5086626f596fd5fd.png')

@client.event
async def on_ready():
    print('Bot is Online')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bot Privado de Paralelgoramos'))
    print(f"Ping: {int(round(client.latency * 1000))}ms \n\n ==== Log ====\n")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')
        print(f"Error: Missing required arguments // by {ctx.message.author}")
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
    await ctx.send(f'Pong! {int(round(client.latency * 1000))}ms')

@client.command()
async def help(ctx, theme=None):
    await ctx.send(embed=HelpCommand)

@client.command()
@commands.has_permissions(administrator=True)
async def stop(ctx):
    await ctx.send('Bot status is turning offline. See you!')
    print("Bot status turning offline\n Shutting Down...")
    await client.close()

if __name__ == '__main__':
    print("\nParalelogramos Bot:\n -> Bot Privado del servidor Paralelogramos.\n -> Bot desarrollado por Newtoniano#1173.\n -> Invitación al servidor de Paralelogramos: https://discord.gg/PgCBfVErYd \n")
    print("Bot Starting...")

    client.load_extension(f'Commands')

    KEY = ""
    client.run(KEY)
