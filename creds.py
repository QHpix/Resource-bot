try:
    with open('token', 'r') as File:
        c_token = File.read().strip('\n')
except IOError as e:
    print(e)
    exit()
try:
    with open('db_creds', 'r') as File:
        creds = File.read().split(':')
        db_user = creds[0]
        db_password = creds[1]
except IndexError as e:
    print('Use the format "username:password" for the database credentials file')
    exit()
