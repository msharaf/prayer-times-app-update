import sys
import os
from discordwebhook import Discord

discord_url=  os.environ['DISCORD_URL']
discord = Discord(url=discord_url)
discord.post(content=sys.argv[1])



