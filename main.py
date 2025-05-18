import discord
from discord.ext import commands
import random

# Create bot instance with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Enable members intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Separate lists for welcome messages, additional texts, and images
welcome_greetings = [
    "Welcome! {member.name}", "Yo! {member.name}", "Hey there {member.name}",
    " Konnichiwa {member.name}"
]

welcome_messages = [
    "🔥A new soul enters the serververse — show us your power!",
    "✨ New member detected. Booting up anime-core systems...",
    "⚔️ You've entered the realm — gear up and enjoy the vibes!",
    "💠May your path through pixels and plotlines be epic! ",
    "🌸 You're among legends now — let's make some memories!"
]

welcome_images = [
    "https://imgs.search.brave.com/qoDl7UYezLvsqV1Z6UtT8SMHByDYmOgNL-s0fW7D3BI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/d2FsbHBhcGVyc2Fm/YXJpLmNvbS8zMy84/OC9aa1FnQ2YuanBn",  # Discord welcome banner
    "https://imgs.search.brave.com/0VMzOCGO6doQAZEsJCpoN2tv5h1Rm1QV-zGGx74cYyo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93MC5w/ZWFrcHguY29tL3dh/bGxwYXBlci8zMDcv/NDUwL0hELXdhbGxw/YXBlci1hbmltZS1t/eS1kcmVzcy11cC1k/YXJsaW5nLW1hcmlu/LWtpdGFnYXdhLmpw/Zw",  # Discord celebration image
    "https://imgs.search.brave.com/J0Bnyw8s8pXHdoFI24aXbpenEFFd_8T1zYfA-3QNn2Q/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hbml5/dWtpLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMy8wMi9h/bml5dWtpLW1ha2lt/YS03Mi5qcGc",  # Discord welcome wave
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
  embed = discord.Embed(title=f"THE SUMMONING PORTAL",
                        description=f"{member.mention}, {greeting}\n{message}",
                        color=discord.Color.blue())
  embed.set_footer(text=f"User: {member.name}#{member.discriminator}")
  embed.set_image(url=image)

  # Send to specific channel
  channel_id = int(os.getenv('WELCOME_CHANNEL_ID',
                             '0'))  # Get channel ID from secrets
  if channel_id:
    channel = member.guild.get_channel(channel_id)
    if channel and channel.permissions_for(member.guild.me).send_messages:
      await channel.send(embed=embed)


@bot.command(name='welcome')
async def welcome(ctx):
  # Select random messages and image
  greeting = random.choice(welcome_greetings)
  message = random.choice(welcome_messages)
  image = random.choice(welcome_images)

  # Create embed
  embed = discord.Embed(title="THE SUMMONING PORTAL",
                        description=f"{greeting}\n{message}",
                        color=discord.Color.blue())
  embed.set_image(url=image)

  await ctx.send(embed=embed)


# Replace 'YOUR_TOKEN' with your bot token in the secrets
import os

bot.run(os.getenv('DISCORD_TOKEN'))
