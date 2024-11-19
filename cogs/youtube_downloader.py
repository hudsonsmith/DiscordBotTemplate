import config

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

import yt_dlp

class YoutubeDownloader(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @app_commands.command(
        name="download_audio",
        description="Download audio from a youtube video."
    )

    @app_commands.describe(
        url="Link to youtube video"
    )

    async def download_audio(self, interaction: discord.Interaction, url: str) -> None:
        with yt_dlp.YoutubeDL() as ydl:
            info: dict = ydl.extract_info(url, download=False)
        
        await interaction.response.send_message(f"Downloading: ` {info['title']} `")


    @commands.is_owner()
    def my_hook(d) -> None:
        if d["status"] == "downloading":
            ...
            


    
async def setup(bot: commands.Bot) -> None:
    guilds: list = [discord.Object(i) for i in config.SERVERS]

    await bot.add_cog(
        YoutubeDownloader(bot),
        guilds=guilds
    )