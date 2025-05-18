
import discord
from discord.ext import commands
import random

# Create bot instance with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# List of welcome messages with their corresponding images
welcome_messages = [
    {
        "text": "Welcome to our awesome server! 🎉",
        "image": "https://i.imgur.com/example1.png"
    },
    {
        "text": "Glad to have you here! 🌟",
        "image": "https://i.imgur.com/example2.png"
    },
    {
        "text": "Welcome aboard! Let's have fun! 🚀",
        "image": "https://i.imgur.com/example3.png"
    }
]

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

@bot.command(name='welcome')
async def welcome(ctx):
    # Select random welcome message
    message = random.choice(welcome_messages)
    
    # Create embed
    embed = discord.Embed(
        title="Welcome!",
        description=message["text"],
        color=discord.Color.blue()
    )
    embed.set_image(url=message["image"])
    
    await ctx.send(embed=embed)

# Replace 'YOUR_TOKEN' with your bot token in the secrets
import os
bot.run(os.getenv('DISCORD_TOKEN'))
