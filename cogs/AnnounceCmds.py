import discord
from discord.ext import commands

class AnnounceCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Prefix Commands", description="These commands can only be used by using sr.", color=0x00F9FF)
        embed.set_thumbnail(url="")
        embed.add_field(name="Prefix Commands Only", value="_", inline=False)
        embed.add_field(name="sr.funCmds", value="Shows the list of user commands", inline=True)
        embed.add_field(name="sr.announce", value="Posts a announcement in the selected channel", inline=True)
        embed.add_field(name="sr.update", value="Posts a Update in the selected channel", inline=True)
        embed.add_field(name="sr.imp", value="Posts a announcement for staff", inline=True)
        embed.add_field(name="sr.DM", value="DMs a user mentions", inline=True)
        embed.set_footer(text="- SkyRise Development Team -")
        await ctx.send(embed=embed)

  
    @commands.command() # Announcement slash comman
    @commands.has_permissions(ban_members=True)
    async def announce(self, ctx, channel: discord.TextChannel = None, *, message:str):
        embed = discord.Embed(color=0x99CCFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044355749939261460/1067932033009070121/SkyRise.png")
        embed.add_field(name=f"Server Announcement", value=message, inline=False)
        embed.set_footer(text="SkyRise Management")
        await channel.send("<@&1027760873634271262>", embed=embed)
        await ctx.send(f"✅ Sent to {channel}")

    @commands.command() # Update slash command
    @commands.has_permissions(ban_members=True)
    async def update(self, ctx, channel: discord.TextChannel = None, *, message:str):
        embed = discord.Embed(color=0x99CCFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044355749939261460/1067932033009070121/SkyRise.png")
        embed.add_field(name=f"Update", value=message, inline=False)
        embed.set_footer(text="SkyRise Management")
        await channel.send("<@&1028023396220538922>", embed=embed)
        await ctx.send(f"✅ Sent to {channel}")

    @commands.command() # Announcement slash command
    @commands.has_permissions(ban_members=True)
    async def imp(self, ctx, channel: discord.TextChannel = None, *, message:str):
        embed = discord.Embed(color=0x99CCFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044355749939261460/1067932033009070121/SkyRise.png")
        embed.add_field(name=f"Staff Announcement", value=message, inline=False)
        embed.set_footer(text="SkyRise Management")
        await channel.send("<@&1021129227581530256>", embed=embed)
        await ctx.send(f"✅ Sent to {channel}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def DM(self, ctx, user : discord.User, *, msg):
        try:
            embed = discord.Embed(title=f'This message was sent from SkyRise Management.',description=f"Please do not **share** this message.",color=0x99CCFF)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044355749939261460/1067932033009070121/SkyRise.png")
            embed.add_field(name=f"To: {user}",value=f"{msg}\n**From: SkyRise Management**",inline=False)
            await user.send(embed=embed)
            await ctx.send(f':white_check_mark: Your Message has been sent to {user}')
        except:
            await ctx.send(':x: Member had their dm close, message not sent')
  
async def setup(client):
    await client.add_cog(AnnounceCmds(client))