import os
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
    "https://cdn.discordapp.com/attachments/1141282552384622635/1141282694424875028/welcome1.gif",
    "https://cdn.discordapp.com/attachments/1141282552384622635/1141282693946617896/welcome2.gif",
    "https://cdn.discordapp.com/attachments/1141282552384622635/1141282693489635368/welcome3.gif"
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
