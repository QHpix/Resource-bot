async def Resource(author_id, message):
    msg = message.split(' ')
    if len(msg) < 2:
        await client.send_message(discord.User(id=author_id), \
    'Please request for a category, use `$resource -c` to view all categories that are available')
    elif len(msg) >= 2:
        option = msg[1]
        if option == '-c':
            await client.send_message(discord.User(id=Authorid), \
    'The following categories are available:\n*   ' + '\n*   '.join(categories))
        elif option == '-gs':
            resource = msg[2]
            await client.send_message(discord.User(id=author_id), \
    'Subcategories of {}:\n{}'.format(resource, '\n'.join(subcategories[resource]))
        elif option == 'get':
            resource = msg[2]
            await client.send_message(discord.User(id=author_id), \
    'You requested the resource: {}'.foramt(resource))
