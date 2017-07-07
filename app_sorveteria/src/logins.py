import responses

users = {
'valeska':{
    'name':'valeska',
    'password':'000'
    },
'maria':{
    'name':'mariazinha',
    'password':'111'
    }
}


def reset_globals():
    responses.USERNAME_ALREADY_EXISTS = False
    responses.USER_CREATED = False
    responses.OK = False
    responses.WRONG_PASSWORD = False
    responses.WRONG_USERNAME = False
    return


def add_user(username, password, name):
    reset_globals()
    new_user = {}
    if username in users:
        responses.USERNAME_ALREADY_EXISTS = True
        return
    users[username] = {}
    users[username]['password'] = password
    users[username]['name'] = name
    responses.USER_CREATED = True
    return


def check_user(username, password):
    reset_globals()
    if username in users:
        if users[username]['password'] == password:
            responses.OK = True
            return
        else:
            responses.WRONG_PASSWORD = True
            return
    else:
       responses.WRONG_USERNAME = True
       return

def get_name_user(username):
    reset_globals()
    if username in users:
        return users[username]['name']
    else:
        responses.WRONG_USERNAME = True
        return 'undefined'
