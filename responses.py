import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == '!roll':
        return str(random.randint(1, 100))

    if p_message == '!help':
        return "`Dongers.`"

    #  return 'Try typing "!help".'