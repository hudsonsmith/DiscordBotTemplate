import config

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @app_commands.command(
        name="testing",
        description="Testing if things even work."
    )

    @app_commands.describe(
        string="Give me a string",
        int="Give me an int"
    )

    @app_commands.choices(
        int = [
            Choice(name="one", value=1),
            Choice(name="two", value=2),
            Choice(name="three", value=3)
        ]
    )
    @commands.is_owner()
    async def testing(self, interaction: discord.Interaction, string: str, int: int) -> None:
        await interaction.response.send_message(f"Hello {interaction.user.display_name}!")
    
async def setup(bot: commands.Bot) -> None:
    guilds: list = [discord.Object(i) for i in config.SERVERS]

    await bot.add_cog(
        Test(bot),
        guilds=guilds
    )