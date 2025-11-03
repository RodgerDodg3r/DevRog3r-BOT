import discord
from discord.ext import commands

class UserAuth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.target_message = 1434047444848738439
        self.target_role = 1434034390454898788
        print("UserAuth cog loaded!")
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        
        # Ignore bot reactions
        if payload.user_id == self.bot.user.id:
            return
        
        # Check if it's the target message
        if payload.message_id != self.target_message:
            return
        
        # Check if it's the white check mark emoji
        if str(payload.emoji) == "✅":
            guild = self.bot.get_guild(payload.guild_id)
            if guild is None:
                return
            
            role = guild.get_role(self.target_role)
            if role is None:
                return
            
            member = guild.get_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)
    
async def setup(bot):
    await bot.add_cog(UserAuth(bot))