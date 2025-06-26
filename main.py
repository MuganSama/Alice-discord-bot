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
welcome_greetings = ["Welcome! ", "Yo! ", "Hey there ", " Konnichiwa "]

welcome_messages = [
    "🔥A new soul enters the serververse — show us your power!",
    "✨ New member detected. Booting up anime-core systems...",
    "⚔️ You've entered the realm — gear up and enjoy the vibes!",
    "💠May your path through pixels and plotlines be epic! ",
    "🌸 You're among legends now — let's make some memories!"
]

welcome_images = [
    "https://shorturl.at/14qMj",  # Discord welcome banner
    "https://shorturl.at/61nrD",  # Discord celebration image
    "https://shorturl.at/SGfWP",  # Discord welcome wave
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
      title=f"THE SUMMONING PORTAL",
      description=f" {greeting}, {member.mention}\n{message}",
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


@bot.event
async def on_member_remove(member):
  # Get the remaining member count (excluding bots)
  remaining_members = len([m for m in member.guild.members if not m.bot])
  
  # Create goodbye embed
  embed = discord.Embed(
      title="🌙 FAREWELL PORTAL",
      description=f"**{member.name}** has left the server.\n\n👥 **{remaining_members}** members remaining in our realm.",
      color=discord.Color.red())
  embed.set_footer(text=f"User: {member.name}#{member.discriminator}")
  embed.set_thumbnail(url=member.display_avatar.url)

  # Send to the same channel as welcome messages
  channel_id = int(os.getenv('WELCOME_CHANNEL_ID', '0'))
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


@bot.command(name='testgoodbye')
async def test_goodbye(ctx):
  # Get the remaining member count (excluding bots)
  remaining_members = len([m for m in ctx.guild.members if not m.bot])
  
  # Create goodbye embed using the command author as example
  embed = discord.Embed(
      title="🌙 FAREWELL PORTAL",
      description=f"**{ctx.author.name}** has left the server.\n\n👥 **{remaining_members}** members remaining in our realm.",
      color=discord.Color.red())
  embed.set_footer(text=f"User: {ctx.author.name}#{ctx.author.discriminator}")
  embed.set_thumbnail(url=ctx.author.display_avatar.url)

  await ctx.send(embed=embed)


# Replace 'YOUR_TOKEN' with your bot token in the secrets
import os

bot.run(os.getenv('DISCORD_TOKEN'))
