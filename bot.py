import discord
import os
from discord.ext import commands
from Utilities.get_token import get_token

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    for file in os.listdir("./Cogs"):
        if not file.endswith('.py'):
            continue
        
        cog = f"Cogs.{file[:-3]}"
        try:
            await bot.load_extension(cog)
            print(f"Loaded {cog}")
        except Exception as e:
            print(f"An error occurred while loading {cog}: {e}")

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(get_token())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())