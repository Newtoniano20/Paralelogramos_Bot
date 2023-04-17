import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
        print('Fun is Online')

    @commands.command()
    async def invite(self, ctx):
        invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
        await ctx.send(f'La invitación al servidor de discord es: {invitelink}')

    @commands.command()
    async def avatar(self, ctx, *,  member : discord.Member=None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=member).set_image(url=member.avatar.url)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def minecraft(self, ctx):
        await ctx.send(f'Actualmente no hay ningun servidor de minecraft hosteado por paralelogramos.')

def setup(client):
    client.add_cog(Info(client))
