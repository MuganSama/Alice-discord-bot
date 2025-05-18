
import discord
from discord.ext import commands
import random

# Create bot instance with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Separate lists for welcome messages, additional texts, and images
welcome_greetings = [
    "Welcome to our awesome server! 🎉",
    "A wild new member appears! ⭐",
    "Welcome aboard! 🚀"
]

welcome_messages = [
    "Hope you'll have a great time here!",
    "Feel free to introduce yourself!",
    "Don't forget to check out our rules!"
]

welcome_images = [
    "https://i.imgur.com/example1.png",
    "https://i.imgur.com/example2.png",
    "https://i.imgur.com/example3.png"
]

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    # Select random messages and image
    greeting = random.choice(welcome_greetings)
    message = random.choice(welcome_messages)
    image = random.choice(welcome_images)
    
    # Create embed
    embed = discord.Embed(
        title="Welcome!",
        description=f"{member.mention}, {greeting}\n{message}",
        color=discord.Color.blue()
    )
    embed.set_image(url=image)
    
    # Send to the first text channel we can find
    for channel in member.guild.text_channels:
        if channel.permissions_for(member.guild.me).send_messages:
            await channel.send(embed=embed)
            break

@bot.command(name='welcome')
async def welcome(ctx):
    # Select random messages and image
    greeting = random.choice(welcome_greetings)
    message = random.choice(welcome_messages)
    image = random.choice(welcome_images)
    
    # Create embed
    embed = discord.Embed(
        title="Welcome!",
        description=f"{greeting}\n{message}",
        color=discord.Color.blue()
    )
    embed.set_image(url=image)
    
    await ctx.send(embed=embed)

# Replace 'YOUR_TOKEN' with your bot token in the secrets
import os
bot.run(os.getenv('DISCORD_TOKEN'))
