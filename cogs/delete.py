import config

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @app_commands.command(
        name="delete",
        description="Delete the current channel and create a new one."
    )

    async def delete(self, interaction: discord.Interaction) -> None:
        await interaction.channel.delete()

    
async def setup(bot: commands.Bot) -> None:
    guilds: list = [discord.Object(i) for i in config.SERVERS]

    await bot.add_cog(
        Test(bot),
        guilds=guilds
    )
