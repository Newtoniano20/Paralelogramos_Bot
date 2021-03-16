import discord
from discord import message
from discord import channel
from discord import user
from discord.ext import commands
from discord import TextChannel
import time as tm

from discord.invite import Invite

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Info is online')
    
    @commands.command()
    async def time(self, ctx):
        seconds = tm.time()
        now = tm.ctime(seconds)
        await ctx.send(f'La hora actual es: {now}')
    
    @commands.command()
    async def invite(self, ctx):
        invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
        await ctx.send(f'La invitación al servidor de discord es: {invitelink}')

    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)
    
    @commands.command()
    async def minecraft(self, ctx):
        await ctx.send(f'Actualmente no hay ningun servidor de minecraft hosteado por paralelogramos.')

def setup(client):
    client.add_cog(Info(client))
