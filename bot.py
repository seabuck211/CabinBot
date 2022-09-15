import discord
import responses
import os


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(
            response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'TOKEN'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Infinite loop fix
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # User message containing '?' in front of the message becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Run bot
    client.run(os.getenv('TOKEN'))