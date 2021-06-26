from Fun import *
from Info import *
from Math import *
from Moderation import *

def setup(client):
    client.add_cog(Fun(client))
    client.add_cog(Info(client))
    client.add_cog(Math(client))
    client.add_cog(Moderation(client))