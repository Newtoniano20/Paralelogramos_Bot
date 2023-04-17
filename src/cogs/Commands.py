from .Fun import *
from .Info import *
from .Math import *
from .Moderation import *

async def setup(client):
    await client.add_cog(Fun(client))
    await client.add_cog(Info(client))
    await client.add_cog(Math(client))
    await client.add_cog(Moderation(client))