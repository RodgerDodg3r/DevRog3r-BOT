import discord
from discord.ext import commands



class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles = {1434941737327132903: 1434034488098426940}
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        user_id = payload.user_id
        message_id = payload.message_id
        emoji = payload.emoji
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(user_id)
        print("asdasd")

        if (user_id == self.bot.user.id):
            print("1")
            return
        
        if (message_id not in self.roles):
            print("Message id not in array")
            return
        
        if (str(emoji) == "✅"):
            if (guild is None):
                return
            role = guild.get_role(self.roles[message_id])
            if (role is None):
                print("Role doesn't exits")
                return

            if (member is not None):
                print("Adding role")
                await member.add_roles(role)
    



async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))