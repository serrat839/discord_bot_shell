# DISCORD.py bot shell!

## Introduction:
This is a very _VERY_ simple and hollowed out bot that can be used for Discord. I recommend
using this as an opportunity to learn more about string manipulation as well as classes.

Here is a link to the main discord.py documentation

https://discordpy.readthedocs.io/en/

Be sure to check out their examples and getting started guides! they are vvv helpful.

## Installation
1. To install discord.py, follow the guide linked [here](https://discordpy.readthedocs.io/en/latest/intro.html)
2. Next follow [this](https://discordpy.readthedocs.io/en/latest/discord.html) tutorial to get your 
tokens and create a bot account. Copy and paste your token into a file named "secret.txt" and save it
in the same directory as main.py.
3. If everything works and it is in a server, try the `$hello` command. If your bot responds, you set
everything up right!

## What does the shell have?
The shell that I am providing has two basic commands available. We are overwriting the placeholder
event within discord.py with our `on_message(message)` function. Don't worry about the syntax with the
@ above it. 

All of your bot's functionality will be stored within the `on_message` function.

### the functions available are... 
- `$hello`
    - After checking the content of the message, we use the str method: startswith() to see
    if the `$hello` command was used. If it was, then we respond with hello to the channel we got the message from.
    - ***IMPORTANT*** use the await keyword before `message.channel.send`
    
- `$bazinga`
    - Same methodology as `$hello`. Checks the message content and if it starts with "$bazinga", respond with
    the bazinga picture stored in `images/`
    - I kept this one in because sending images is also hella fun lmao.
    
