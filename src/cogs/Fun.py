import discord
from discord.ext import commands
from googlesearch import search
from random import choice, randrange, shuffle


class Fun(commands.Cog):
    def __init__(self, client):
        client = client
        print("Fun is Online")

    @commands.command()
    async def iq(self, ctx):
        num = randrange(0, 201)
        if num <= 65:
            await ctx.send(f"Eres Literalmente Mongolo! Con un iq de: {num}")
        if 65 < num < 100:
            await ctx.send(f"Eres Normal! Con un iq de: {num}")
        if 100 < num < 150:
            await ctx.send(f"Eres Inteligente! Un pedazo iq de: {num}")
        if 150 < num < 180:
            await ctx.send(f"Eres un Genio! Un pedazo iq de: {num}")
        if 180 < num < 199:
            await ctx.send(f"Eres Einstein! Un Legendario iq de: {num}")
        if num == 200:
            await ctx.send(
                f"Lo has conseguido! Eres Mejor que Einstein! Un Inmejorable iq de: {num}"
            )

    @commands.command()
    async def poll(self, ctx, *theme):
        await ctx.channel.purge(limit=1)
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        polls = discord.Embed(
            title=f"**Paralelovotación:**", description=f"{str(themes)}", color=0x00FF00
        )
        test = await ctx.send(embed=polls)
        emoji = "\N{THUMBS UP SIGN}"
        emoji2 = "\N{THUMBS DOWN SIGN}"
        await test.add_reaction(emoji)
        await test.add_reaction(emoji2)

    @commands.command()
    async def search(self, ctx, *theme):
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        messagesearch = discord.Embed(title=f"**Searching:** {themes}", color=0x00FF00)
        await ctx.send(embed=messagesearch)
        try:
            x1 = search(themes, lang="es")
            await ctx.send(f"Resultado: {x1[0]}")
        except:
            await ctx.send("error")

    @commands.command()
    async def yopino(self, ctx, member=None):
        phrase_list = [
            "Majo pero no me liaria",
            "No hablamos mucho pero molaria quedar",
            "Eres completamente inutil",
        ]
        phrase = choice(phrase_list)
        if member != None:
            await ctx.send(f"Mi opinon sobre {member} es: {phrase}")
        elif member == str:
            await ctx.send(f"Mi opinon sobre {member} es: {phrase}")
        else:
            await ctx.send(f"Hola <@{ctx.message.author.id}>, {phrase}")

    @commands.command()
    async def random(self, ctx, member1, *members):
        listn = []
        try:
            for m in members:
                listn.append(m)
            listn.append(member1)
        except:
            listn.append(member1)
        shuffle(listn)
        loop = 0
        res = ""
        for l in listn:
            res += l + " "
            loop += 1
        await ctx.send(res)

    @commands.command()
    async def say(self, ctx, *theme):
        test = len(theme)
        themes = ""
        for n in range(test):
            themes = themes + " " + theme[n]
        await ctx.send(themes)


def setup(client):
    client.add_cog(Fun(client))
