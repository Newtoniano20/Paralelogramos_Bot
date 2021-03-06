import discord
from discord.ext import commands
import math as mh

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def math(self, ctx):
        Math = discord.Embed(title="__Math Commands__", description="Estos son los comandos de mates programados en el bot: ", color=0x00ff00)
        Math.add_field(name="**Comandos Basicos:**", value="eq -> Resolución de equaciones. \n Uso: .eq <a> <b> <c> \n sum -> Sumar dos numeros \n Uso: .sum <a> <b>\n sub -> Restar dos numeros \n Uso: .sub <a> <b>\n mult -> Multiplicar dos numeros \n Uso: .mult <a> <b>\n div -> Dividir dos numeros \n Uso: .div <a> <b>", inline=False)
        Math.add_field(name="**Trigonometria:**", value="LOS ANGULOS ESTAN EN RADIANES!!\nPara usar el numero pi, simplemente poned 'pi'\n.sin -> sin(a)\n.cos -> cos(a)\n.tg -> tg(a)", inline=False)
        await ctx.send(embed=Math)

    @commands.command()
    async def sin(self, ctx, a):
        if a == "pi":
            await ctx.send(f"El resultado es: 0")
        else:    
            x1 = mh.sin(float(a))
            await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def cos(self, ctx, a):
        if a == "pi":
            a = mh.pi
        x1 = mh.cos(float(a))
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def tg(self, ctx, a):
        if a == "pi":
            await ctx.send(f"El resultado es: -1")
        else:
            x1 = mh.tan(float(a))
            await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def eq(self, ctx, a=0, b=0, c=0):
        d = b*b - 4*a*c
        q = 2*a
        try:
            if a == 0 and b == 0:
                await ctx.send(f"Polynomial:\n{str(a)}x^2 / {str(b)}x / {c}\n Does not have a solution: {c} = 0")

            elif a == 0:
                x1 = (- c)/b
                await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}')

            elif b == 0:
                try:
                    x1 = mh.sqrt((- c)/a)
                    await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have both solutions: \nx1 = {x1}\nx2 = {-x1}')
                except: 
                    await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c}\n Does not have a solution:\nDiscriminator = {-c/a}')
            elif c == 0:
                x1 = 0
                x2 = -b/a
                await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have both solutions: \nx1 = {x1}\nx2 = {x2}')
            
            elif d < 0:
                await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c}\n Does not have a solution: \nDiscriminator = {d}')

            elif d == 0:
                x1 = -b/(q)
                await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}')
            else:
                x1 = (-b + mh.sqrt(d)) / (q)
                x2 = (-b - mh.sqrt(d)) / (q)
                await ctx.send('', f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have both solutions\nx1 = {x1} x2 = {x2}')
        except:
            await ctx.send("Pon la a, b y c separadas por un espacio y no pongas nada que no sea un numero")
    @commands.command()
    async def sqrt(self, ctx, num):
        num = mh.sqrt(float(num))
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
    async def sum(self, ctx, a=0, b=0, c=0, d=0):
        x1 = a + b + c + d
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def sub(self, ctx, a=0, b=0):
        x1 = a - b
        await ctx.send(f"El resultado es: {x1}")
    
    @commands.command()
    async def log(self, ctx, a, b):
        if a == "e":
            a = mh.e
        if b == "e":
            b = mh.e
        x1 = mh.log(float(b), float(a))
        await ctx.send(f"El resultado es: {x1}")
    

def setup(client):
    client.add_cog(Math(client))