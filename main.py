import asyncio
import discord
from creds import c_token,db_user,db_password
from categories import categories


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
        msg = message.content.split(' ')

        if len(msg) < 2:
            await client.send_message(discord.User(id=author_ID), \
'Please request for a category, use `$resource -c` to view all the categories that are available')

        elif len(msg) >= 2:
            option = msg[1]
            if option == '-c':
                await client.send_message(discord.User(id=author_ID), \
'The following categories are available:\n*   ' + '\n*   '.join(categories))

            elif option == 'get':
                resource = msg[2]
                await client.send_message(discord.User(id=author_ID), \
'You requested the resource: {}'.format(resource))

if __name__ == "__main__":
    client.run(c_token)
