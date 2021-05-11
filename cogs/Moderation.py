import discord
from discord.ext import commands
import time

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    @commands.has_role("Bot Perms")
    async def clear(self, ctx, ammount=5):
        await ctx.channel.purge(limit=ammount+1)
        await ctx.send(f":thumbsup: I've deleted {ammount} messages")
        time.sleep(2)
        await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.has_role("Bot Perms")
    async def kick(self, ctx, member: discord.member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_role("Bot Perms")
    async def ban(self, ctx, member: discord.member, *, reason=None):
        await member.ban(reason=reason)

def setup(client):
    client.add_cog(Moderation(client))
