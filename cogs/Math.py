import discord
from discord.ext import commands
import time
import math as mh

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Math is online')
    
    @commands.command()
    async def math(self, ctx):
        Math = discord.Embed(title="__Math Commands__", description="Estos son los comandos de mates programados en el bot: ", color=0x00ff00)
        Math.add_field(name="**Comandos Basicos:**", value="eq -> Resolución de equaciones. \n Uso: .eq <a> <b> <c> \n sum -> Sumar dos numeros \n Uso: .sum <a> <b>\n sub -> Restar dos numeros \n Uso: .sub <a> <b>\n mult -> Multiplicar dos numeros \n Uso: .mult <a> <b>\n div -> Dividir dos numeros \n Uso: .div <a> <b>", inline=False)
        Math.add_field(name="**Trigonometria:**", value="LOS ANGULOS ESTAN EN RADIANES!!\nPara usar el numero pi, simplemente poned 'pi'\n.sin -> sin(a)\n.cos -> cos(a)\n.tg -> tg(a)\n.cos_angle_sum -> cos(a+b)\n.cos_angle_sub -> cos(a-b)\n.sin_angle_sum -> sin(a+b)\n.sin_angle_sub -> sin(a-b)\n.tg_angle_sum -> tg(a+b)\n.tg_angle_sub -> tg(a-b)\n.two_alpha_sin -> sin(2a)\n.two_alpha_cos -> cos(2a)\n.two_alpha_tg -> tg(2a)\n.half_alpha_sin -> sin(a/2)\n.half_alpha_cos -> cos(a/2)\n.half_alpha_tg -> tg(a/2)", inline=False)
        await ctx.send(embed=Math)

    @commands.command()
    async def sin(self, ctx, a):
        if a == "pi":
            a = mh.pi
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
            a = mh.pi
        x1 = mh.tan(float(a))
        await ctx.send(f"El resultado es: {x1}")
    
    
    @commands.command()
    async def cos_angle_sum(self, ctx, alpha, beta):
        if alpha == "pi":
            alpha = mh.pi
        if beta == "pi":
            beta = mh.pi
        x1 = mh.cos(float(alpha))*mh.cos(float(beta)) - mh.sin(float(alpha))*mh.sin(float(beta))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def cos_angle_sub(self, ctx, alpha, beta):
        if alpha == "pi":
            alpha = mh.pi
        if beta == "pi":
            beta = mh.pi
        x1 = mh.cos(float(alpha))*mh.cos(float(beta)) + mh.sin(float(alpha))*mh.sin(float(beta))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def sin_angle_sum(self, ctx, alpha, beta):
        if alpha == "pi":
            alpha = mh.pi
        if beta == "pi":
            beta = mh.pi
        x1 = mh.sin(float(alpha))*mh.cos(float(beta)) +  mh.cos(float(alpha))*mh.sin(float(beta))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def sin_angle_sub(self, ctx, alpha, beta):
        if alpha == "pi":
            alpha = mh.pi
        if beta == "pi":
            beta = mh.pi
        x1 = mh.sin(float(alpha))*mh.cos(float(beta)) -  mh.cos(float(alpha))*mh.sin(float(beta))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def tg_angle_sum(self, ctx, alpha, beta):
        if alpha == "pi":
            alpha = mh.pi
        if beta == "pi":
            beta = mh.pi
        x1 = (mh.tan(float(alpha)) + mh.tan(float(beta)))/(1 - mh.tan(float(alpha))*mh.tan(float(beta)))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def tg_angle_sub(self, ctx, alpha, beta):
        if alpha == "pi":
            alpha = mh.pi
        if beta == "pi":
            beta = mh.pi
        x1 = (mh.tan(float(alpha)) - mh.tan(float(beta)))/(1 + mh.tan(float(alpha))*mh.tan(float(beta)))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def two_alpha_sin(self, ctx, alpha):
        if alpha == "pi":
            alpha = mh.pi
        x1 = 2*mh.sin(float(alpha))*mh.cos(float(alpha))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def two_alpha_cos(self, ctx, alpha):
        if alpha == "pi":
            alpha = mh.pi
        x1 = mh.cos(float(alpha))**2 - mh.sin(float(alpha))**2
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def two_alpha_tg(self, ctx, alpha):
        if alpha == "pi":
            alpha = mh.pi
        x1 = (2*mh.tan(float(alpha)))/(1 - mh.tan(float(alpha))**2)
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def half_alpha_sin(self, ctx, alpha):
        if alpha == "pi":
            alpha = mh.pi
        x1 = mh.sqrt((1 - mh.cos(float(alpha))) / 2 )
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def half_alpha_cos(self, ctx, alpha):
        if alpha == "pi":
            alpha = mh.pi
        x1 = mh.sqrt((1 + mh.cos(float(alpha))) / 2 )
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def half_alpha_tg(self, ctx, alpha):
        if alpha == "pi":
            alpha = mh.pi
        x1 = mh.sqrt((1 - mh.cos(float(alpha))) / (1 + mh.cos(float(alpha))))
        await ctx.send(f"El resultado es: {x1}")

    @commands.command()
    async def eq(self, ctx, a=0, b=0, c=0):
        x1 = 0
        d = 0
        d = b*b - 4*a*c

        if b == 0:
            x1 = mh.sqrt((- c)/a)
            await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}          ')
        
        elif a == 0:
            x1 = (- c)/b
            await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}          ')

        elif d < 0:
            await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c}\n Does not have a solution:\nDiscriminator = {d}                ')

        elif d == 0:
            try:
                x1 = (-b + mh.sqrt(b**2 - 4*a*c)) / (2*a)
                await ctx.send(f'Polynomial:\n{str(a)}x^2 / {str(b)}x / {c} \n Does have a solution but there is only one:\nx1 = {x1}          ')
            except:
                await ctx.send("Math error: 0/0")
                await ctx.send(f'-[{b}] + math.sqrt([{b}]^2 - 4·[{a}]·[{c}]) / 2·[{a}]')
        else:
            try:
                x1 = (-b + mh.sqrt(b**2 - 4*a*c)) / (2*a)
                x2 = (-b - mh.sqrt(b**2 - 4*a*c)) / (2*a)
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
    client.add_cog(Moderation(client))