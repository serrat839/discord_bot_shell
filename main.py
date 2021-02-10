import discord
import logging

# discord.py documentation is found here
# https://discordpy.readthedocs.io/en/latest/#

# set up client stuff for discord.py
# this was taken from their get started tutorial and lets the discord bot look at all members
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# read the token from user in "secret.txt"
token = open("secret.txt", "r").read()

# set up logging just in case shit goes bad
logging.basicConfig(level=logging.INFO)

# when the bot is ready and connected to server, fires this command
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# whenever the bot detects a new message in whatever server it is in, fire this function off
# async means that the function is allowed to use the await keyword
# await stops code that is allowed to run in paralell, meaning it must finish its line before moving on.
# tldr; its webdev javascript shit
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
@client.event
async def on_message(message):
    """
    To see what is in each message object, refer to this:
    https://discordpy.readthedocs.io/en/latest/api.html?highlight=message#discord.Message

    The parameters within the object have useful things that you can use for your bot
    Things like, the server it was from, the channel it was from, and who sent it!

    :param message: a message object generated whenever a message is sent
    :return:
    """

    # helpful link to figure out how you can mess with strings:
    # https://www.w3schools.com/python/python_ref_string.asp

    # tbh, this would be a really op way to learn more about strings and classes

    # if the bot sent the message, ignore the message
    if message.author == client.user:
        return

    # Hello world for discord.py
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    # How to send an image
    elif message.content.startswith("$bazinga"):
        await message.channel.send(file=discord.File("images/hello_world.png"))

    # recommendations:
    # figure out how to get all members in a discord server
    # roll a d20
    # make a calculator
    # make a duel command: target user and randomly mute one user in a "duel"

# run the bot
client.run(token)
