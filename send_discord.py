import sys
import os

from discordwebhook import Discord

discord_url=  os.environ['DISCORD_URL']
discord = Discord(url=discord_url)
discord.post(content=sys.argv[1])

# channel_number = os.environ['channel_number']
# discord_client_secret = os.environ['discord_client_secret']
# print(channel_number)
# print(discord_client_secret)
# # Set up a Discord client
# client = discord.Client()

# # Define a function to send a message to the channel
# async def send_discord_message(channel_id, message):
#     channel = client.get_channel(channel_id)
#     await channel.send(message)

# # Log in to Discord
# @client.event
# async def on_ready():
#     print(f'Logged in as {client.user}')

#     # Send a message to the channel
#     channel_id = channel_number # Replace with the ID of your channel
#     message = sys.argv[1]
#     await send_discord_message(channel_id, message)
#     await client.close()

# # Start the client
# client.run(discord_client_secret)


