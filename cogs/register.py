import sqlite3

import config

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class Register(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        self.conn: sqlite3.Connection = sqlite3.connect("database.db")
        self.cur: Cursor = self.conn.cursor()
    
    @app_commands.command(
        name="register",
        description="Register yourself with the bot!"
    )

    @commands.is_owner()
    async def register(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Thank you for registering, <#{interaction.user.id}>")
    
async def setup(bot: commands.Bot) -> None:
    guilds: list = [discord.Object(i) for i in config.SERVERS]

    await bot.add_cog(
        Register(bot),
        guilds=guilds
    )