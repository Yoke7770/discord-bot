# Example Discord bot using discord.py

import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("Discord Token")
if not TOKEN:
    print("Error: DISCORD_TOKEN environment variable not set.")
    sys.exit(1)

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")

@bot.command(name="ping")
async def ping(ctx):
    """Prefix command: !ping"""
    await ctx.send("Pong!")

@bot.tree.command(name="ping")
async def slash_ping(interaction: discord.Interaction):
    """Slash command: /ping"""
    await interaction.response.send_message("Pong!")

if __name__ == '__main__':
    bot.run(TOKEN)
