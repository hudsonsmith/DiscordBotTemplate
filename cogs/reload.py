import os

import config

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

# Self won't work inside the decorators.
# That's why I make set it outside of the class.
cogs: list = [
    f"{i.replace('.py', '')}" for i in os.listdir("./cogs") if i.endswith(".py")
]

class Reload(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @app_commands.command(
        name="reload",
        description="Reload the cogs of the bot."
    )

    @app_commands.describe(
        cog="What cog to reload"
    )

    @app_commands.choices(
        cog = [
            Choice(name=i, value=i) for i in cogs
        ]
    )

    @commands.is_owner()
    async def reload(self, interaction: discord.Interaction, cog: str="all") -> None:
        if cog == "all":
            for file in os.listdir("./cogs"):
                if file.endswith(".py"):
                    await self.bot.reload_extension(f"cogs.{file.replace('.py', '')}")

            await interaction.response.send_message(f"Reloaded all cogs")
        
        else:
            await self.bot.reload_extension(f"cogs.{cog}")
            await interaction.response.send_message(f"Reloaded ` {cog}.py `")

        for server in config.SERVERS:
            synced = await self.bot.tree.sync(guild=discord.Object(id=server))
            await interaction.response.send_message(f"Synced across {synced} server(s)")
    
async def setup(bot: commands.Bot) -> None:
    guilds: list = [discord.Object(i) for i in config.SERVERS]

    await bot.add_cog(
        Reload(bot),
        guilds=guilds
    )