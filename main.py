import asyncio
import discord
from creds import c_token,db_user,db_password
from categories import categories, subcategories
import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Bot loaded')
    await client.change_presence(game=discord.Game(name='$resource -h for help'))

@client.event
async def on_message(message):
    #get the id of the author to send it in a dm
    author_ID = message.author.id

    if message.content.startswith('$resource'):
        commands.Resource(author_ID, message)

if __name__ == "__main__":
    client.run(c_token)
