import discord
from discord.ext import commands

class UserJoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.join_channel = 1434035994465796107
        self.leave_channel = 1434221758419833023
    



    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed  = discord.Embed(
            title= "Witamy nowego użytkownika!",
            description = f"Witaj {member.mention} na **Biuro Ochrony Programistów**! 🎉",
            color = discord.Color.green()
        )

        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        channel = self.bot.get_channel(self.join_channel)
        await channel.send(embed=embed)
    


    @commands.Cog.listener()
    async def on_member_leave(self, member):
        embed = discord.Embed(
            title = "Żegnamy jednego z naszych użytkowników 😭",
            description = f"Mamy nadzieję, że do nas wrócisz...",
            color = discord.Color.red()
        )

        embed.set_thumbnail(url = member.avatar.url if member.avatar else member.default_avatar.url)
        channel = self.bot.get_channel(self.leave_channel)
        await channel.send(embed=embed)



async def setup(bot):
    await bot.add_cog(UserJoinLeave(bot))