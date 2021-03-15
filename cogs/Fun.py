import discord
from discord.ext import commands
import random as rnd
import math

class Fun(commands.Cog):
    def __init__(self, client):
        client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is online')
    
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
    async def eq(self, ctx, a=0, b=0, c=0):
        x1 = 0
        d = 0
        d = b*b - 4*a*c

        if b == 0:
            x1 = math.sqrt((- c)/a)
            await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}          ')
        
        elif a == 0:
            x1 = (- c)/b
            await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}          ')

        elif d < 0:
            await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c}\n Does not have a solution:\nDiscriminator = {d}                ')

        elif d == 0:
            try:
                x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
                await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}          ')
            except:
                await ctx.send("Math error: 0/0")
                await ctx.send(f'-[{b}] + math.sqrt([{b}]^2 - 4·[{a}]·[{c}]) / 2·[{a}]')
        else:
            try:
                x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
                x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
                await ctx.send('', f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have both solutions\nx1 = {x1} x2 = {x2}         ')
            except:
                await ctx.send("Math error: 0/0")
                await ctx.send(f'-[{b}] + math.sqrt([{b}]^2 - 4·[{a}]·[{c}]) / 2·[{a}]')
        try:
            await ctx.send("X1 = ", x1)
            await ctx.send("X2 = ", x2)
        except:
            await ctx.send("d = ", d)
    @commands.command()
    async def sqrt(self, ctx, num):
        num = math.sqrt(int(num))
        await ctx.send(f"El resultado es: {num}")

    @commands.command()
    async def mult(self, ctx, a=0, b=0):
        x1 = a * b
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def div(self, ctx, a=0, b=0):
        x1 = a / b
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def sum(self, ctx, a=0, b=0):
        x1 = a + b
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def sub(self, ctx, a=0, b=0):
        x1 = a - b
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def log(self, ctx, a, b):
        if a == "e":
            a = math.e
        if b == "e":
            b = math.e
        x1 = math.log(int(b), int(a))
        await ctx.send(f"El resultado es: {x1}")


def setup(client):
    client.add_cog(Fun(client))
