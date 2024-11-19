import os

import discord
from discord.ext import commands

import config

# Rule id here.
ID: int = 0

class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id=ID
        )
    
    async def setup_hook(self) -> None:
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file.replace('.py', '')}")

        for server in config.SERVERS:
            await bot.tree.sync(guild=discord.Object(id=server))
    
    async def on_ready(self) -> None:
        print(f"{self.user} is connected")

bot: MyBot = MyBot()
bot.run(config.TOKEN)
