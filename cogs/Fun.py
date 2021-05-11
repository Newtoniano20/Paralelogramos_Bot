import discord
from discord.ext import commands
import random as rnd
from googlesearch import search
from mpmath.functions.functions import im
import random

class Fun(commands.Cog):
    def __init__(self, client):
        client = client

    @commands.command()
    async def iq(self, ctx):
        num = rnd.randrange(0, 201)
        if num <= 65:
            await ctx.send(f'Eres Literalmente Mongolo! Con un iq de: {num}')
        if 65 < num < 100:
            await ctx.send(f'Eres Normal! Con un iq de: {num}')
        if 100 < num < 150:
            await ctx.send(f'Eres Inteligente! Un pedazo iq de: {num}')
        if 150 < num < 180:
            await ctx.send(f'Eres un Genio! Un pedazo iq de: {num}')
        if 180 < num < 199:
            await ctx.send(f'Eres Einstein! Un Legendario iq de: {num}')
        if num == 200:
            await ctx.send(f'Lo has conseguido! Eres Mejor que Einstein! Un Inmejorable iq de: {num}')
    
    @commands.command()
    async def poll(self, ctx, *theme): 
        await ctx.channel.purge(limit=1)
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        polls = discord.Embed(title=f"**{themes}**", description=f"Esta es una votación para decidir si: {str(themes)}", color=0x00ff00)
        test = await ctx.send(embed=polls)
        emoji = '\N{THUMBS UP SIGN}'
        emoji2 = "\N{THUMBS DOWN SIGN}"
        await test.add_reaction(emoji)
        await test.add_reaction(emoji2)

    @commands.command()
    async def search(self, ctx, *theme):
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        try:    
            x1 = search(themes)
            await ctx.send(x1[0])
        except:
            await ctx.send("error")

    @commands.command()
    async def yopino(self, ctx, member=None):
        listn2 = ["Majo pero no me liaria", "No hablamos mucho pero molaria quedar", "Eres completamente inutil"]
        phrase = random.choice(listn2)
        if member != None:
            await ctx.send(f"Mi opinon sobre {member} es: {phrase}")
        else:
            await ctx.send(f"Hola <@{ctx.message.author.id}>, {phrase}")
            
    @commands.command()
    async def search2(self, ctx, *theme):
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        try:    
            x1 = search(themes)
            await ctx.send(x1[1])
        except:
            await ctx.send("error")
    
    @commands.command()
    async def searchall(self, ctx, *theme):
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        try:    
            x1 = search(themes)
            await ctx.send(x1)
        except:
            await ctx.send("error")

def setup(client):
    client.add_cog(Fun(client))
