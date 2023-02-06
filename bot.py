# Libs
import discord
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from discord import app_commands


def mixedCase(*args):
  """
  Gets all the mixed case combinations of a string

  This function is for in-case sensitive prefixes
  """
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in string)))
    for x in list(a): total.append(x)

  return list(total)


# BOT

intents = discord.Intents.all()
intents.members = True

client =commands.Bot(case_insensitive=True, command_prefix=mixedCase("sr."), intents=intents)
status = cycle(['/help', "play.skyrisemc.net", "/funcmds"])
client.remove_command('help')

@client.event
async def on_ready():
  try: 
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} commands!")
  except:
    print('already synced')

  change_status.start()
  print(f"Sucessfully logged in as {client.user}")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    if member.guild.id == 1021125650792333445: 
        guild = client.get_guild(1021125650792333445)
        channel = guild.get_channel(1021574794963062855)
        info_user = member
        info_embed = discord.Embed(title=f'Welcome to {member.guild.name}!',description=f"We hope you enjoy your stay {member.mention}",color=0x99CCFF)
        info_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044355749939261460/1067932033009070121/SkyRise.png")
        info_embed.add_field(name=f"<:skyrise:1044216372563026010>WELCOME {member}<:skyrise:1044216372563026010>",value=f"Check out:\n<#1021131165295452243>,\n<#1021574529090330634>,\n<#1021130834796892321>!!",inline=False)
        info_embed.add_field(name="🔧 Account Created on:",value=info_user.created_at.strftime("%b %d %Y"))
        await channel.send(embed=info_embed)
    elif member.guild.id == 1067596765269864569: 
        guild = client.get_guild(1067596765269864569)
        channel = guild.get_channel(1067932421363863563)
        info_user = member
        info_embed = discord.Embed(title=f'Welcome to {member.guild.name}!',description=f"We hope you enjoy your stay {member.mention}",color=0x99CCFF)
        info_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044355749939261460/1067932033009070121/SkyRise.png")
        info_embed.add_field(name=f"<:SkyRise:1067934687571496970>WELCOME {member}<:SkyRise:1067934687571496970>",value=f"Check out:\n<#1021131165295452243>,\n<#1021574529090330634>,\n<#1021130834796892321>!!",inline=False)
        info_embed.add_field(name="🔧 Account Created on:",value=info_user.created_at.strftime("%b %d %Y"))
        await channel.send(embed=info_embed)
    

# error handler
@client.event
async def on_command_error(interaction: discord.Interaction, error):
  if isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(title=f"`❌` - Missing Permissions", description=f"You cannot use this command because you do not have high enough permission/status to use it.", color=0xe74c3c)
    embed.add_field(name="Why can't I use this command?", value="In order to use this command you need to have moderator permissions.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1014990016457478204/1015800560118677565/error.gif")
    await interaction.response.send_message(embed=embed, ephemeral=True)
  
  elif isinstance(error, commands.CommandOnCooldown):
    print(error)
            
  else:
    embed = discord.Embed(title=f"`❌` - Error", description=f"Sorry we ran into an error.", color=0xe74c3c)
    embed.add_field(name="Why am I getting an error?", value=f"This error can be about anything, from members not being in the server, to commands not existing.\n\n**This is the error you are getting:**\n{error}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1014990016457478204/1015800560118677565/error.gif")
    await interaction.response.send_message(embed=embed, ephemeral=True)
    print(error)

@client.tree.command(name='help', description="Displays the commands") # help slash command
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Commands",description="Helps mods control the server better",color=0x99CCFF)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1027346736223637536/1043993421913800805/SkyRise-01.png")
    embed.add_field(name="/socials", value="Posts SkyRise's socials.", inline=True)
    embed.add_field(name="/devhelp", value="Shows you how to contact dev support.", inline=True)
    embed.add_field(name="/clear", value="Clears messages.", inline=True)
    embed.add_field(name="/kick", value="Kicks the selected user.", inline=True)
    embed.add_field(name="/ban", value="Bans the selected user.", inline=True)
    embed.add_field(name="/unban", value="Unbans the user's ID.", inline=True)
    embed.add_field(name="/nuke", value="Nukes a selected channel.", inline=True)
    embed.add_field(name="/whois", value="Displays user infomation.", inline=True)
    embed.add_field(name="/server", value="Displays server infomation.", inline=True)
    embed.set_footer(text="- SkyRise Development Team -")
    await interaction.response.send_message(embed=embed, ephemeral=False)

@client.tree.command(name='funcmds', description="Displays the fun commands")
async def funcmds(interaction: discord.Interaction):
    embed = discord.Embed(title="Command List", color=0x99CCFF)
    embed.add_field(name='sr.8ball', value='Let the 8 Ball Predict!', inline=False)
    embed.add_field(name='sr.funnyrate', value=' This command is used to rate the funniness of a given statement or phrase on a scale of 1-100%.', inline=False)
    embed.add_field(name='sr.ship', value='This command is used to generate a ship name for two given names.', inline=False)
    embed.add_field(name='sr.joke', value='This command is used to generate a random joke.', inline=False)
    embed.add_field(name='sr.roll', value='This command is used to generate a random number within a given range.', inline=False)
    embed.add_field(name='sr.rps', value='This command is used to play a game of rock-paper-scissors against the computer.', inline=False)
    embed.add_field(name='sr.catfact', value='This command is used to generate a random fact about cats.', inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=False)

@client.tree.command(name='socials', description="Displaying all of the official social media account from SkyRiseMC")
async def socials(interaction: discord.Interaction):
    embed = discord.Embed(title="SkyRise's Socials",description="Displaying all of the official social media account from SkyRiseMC", color=discord.Color.from_rgb(135, 206, 250))
    embed.add_field(name="Twitter:", value="[@playskyrise](https://twitter.com/playskyrise)")
    embed.add_field(name="TikTok:", value="[@skyrisemc](https://www.tiktok.com/@skyrisemc?_t=8XdpJGJOJHK&_r=1)")
    embed.add_field(name="Email:", value="support@skyrisemc.net")
    embed.set_footer(text="By SkyRise Management Team")
    await interaction.response.send_message(embed=embed, ephemeral=False)


@client.tree.command(name='unban', description="Unbans the user's ID") # unban slash command
@commands.has_permissions(ban_members=True)
async def unban(interaction: discord.Interaction, userid: discord.User):
  if userid == None:
    await interaction.response.send_message("Please specify a member\nEx: `949097449740435586`", ephemeral=True)
  else:
    guild = interaction.guild
    await guild.unban(user=userid)
    embed = discord.Embed(title="Success!", description=f"{userid} was unbanned!") 
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command(name='ban', description='Bans the selected user') # ban slash command
@commands.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason:str):
    embed = discord.Embed(title=f"{member} was banned for {reason}")
    await member.ban(reason=reason)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command(name='kick', description='Kicks the selected user') # kick slash command
@commands.has_permissions(kick_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason:str):
    embed = discord.Embed(title=f"{member} was banned for {reason}")
    await member.kick(reason=reason)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command(name='clear', description='Clears messages') # clear slash command
@commands.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    await interaction.channel.purge(limit=amount + 1)
    embed = discord.Embed(title=f"Purged {amount} messages")
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command(name='nuke', description='Nukes a selected channel') # clear slash command
@commands.has_permissions(ban_members=True)
async def nuke(interaction: discord.Interaction, channel: discord.TextChannel = None):
        channel = discord.utils.get(interaction.guild.channels, name=channel.name)
        if channel is not None:
            message = await channel.send("THIS CHANNEL IS BEING NUKE IN 5")
            await asyncio.sleep(1)
            await message.edit(content='THIS CHANNEL IS BEING NUKE IN 4')
            await asyncio.sleep(1)
            await message.edit(content='THIS CHANNEL IS BEING NUKE IN 3')
            await asyncio.sleep(1)
            await message.edit(content='THIS CHANNEL IS BEING NUKE IN 2')
            await asyncio.sleep(1)
            await message.edit(content='THIS CHANNEL IS BEING NUKE IN 1')
            await asyncio.sleep(1)
            await message.edit(content='THIS CHANNEL IS BEING NUKE IN 0')
            new_channel = await channel.clone(reason="Has been Nuked!")
            await channel.delete()
            await new_channel.send("Nuked the Channel sucessfully!")

        else:
            await interaction.response.send_message(f"No channel named {channel.name} was found!", ephemeral=True)


@client.tree.command(name="whois", description="Displays user infomation.")
async def whois(interaction: discord.Interaction, member: discord.Member):
    if member:
        info_user = member
    elif member == None:
        info_user = interaction.author
    info_embed = discord.Embed(color=0x99CCFF)
    info_embed.set_thumbnail(url=f"{info_user.avatar.url}")
    info_embed.add_field(name="🔴Member:",value=f"{info_user.mention}",inline=False)
    info_embed.add_field(name="⭐Member name:",value=f"{info_user}",inline=False)
    info_embed.add_field(name="💬Nickname:",value=f"{info_user.nick}",inline=False)
    info_embed.add_field(name="📆Joined on:",value=info_user.joined_at.strftime("%b %d %Y"))
    info_embed.add_field(name='📆Created on:',value=info_user.created_at.strftime("%b %d %Y"),inline=False)
    info_embed.add_field(name="🆔Member ID:",value=f"{info_user.id}",inline=False)
    await interaction.response.send_message(embed=info_embed, ephemeral=False)

@client.tree.command(name="server", description="Displays server infomation.")
async def server(interaction: discord.Interaction):
    embed = discord.Embed(title=f"{interaction.guild.name} Info",description="Information of this Server",color=0x99CCFF)
    embed.add_field(name='🆔Server ID', value=f"{interaction.guild.id}", inline=False)
    embed.add_field(name='📆Created on',value=interaction.guild.created_at.strftime("%b %d %Y"),inline=False)
    embed.add_field(name='👑Owner',value=f"{interaction.guild.owner.mention}",inline=False)
    embed.add_field(name='👥Members',value=f'{interaction.guild.member_count} Members',inline=False)
    embed.add_field(name='💬Channels',value=f'{len(interaction.guild.text_channels)} Text | {len(interaction.guild.voice_channels)} Voice',inline=False)
    embed.set_thumbnail(url=interaction.guild.icon.url)
    await interaction.response.send_message(embed=embed, ephemeral=False)


@client.tree.command(name='devhelp', description="Reporting bugs or asking for help")
async def devhelp(interaction: discord.Interaction):
    embed = discord.Embed(title="Developer Help", description="Please message management if you find any bugs or email them with the support email. Thanks!!", color=discord.Color.from_rgb(135, 206, 250))
    embed.add_field(name="Email:", value="support@skyrisemc.net")
    embed.set_footer(text="By AngleBoost#5662")
    await interaction.response.send_message(embed=embed, ephemeral=False)


async def main():
    async with client:
        await client.load_extension('cogs.AnnounceCmds')
        print("AnnounceCmds.py loaded from cogs folder.")
        await client.load_extension('cogs.funStuff')
        print("funStuff.py loaded from cogs folder.")
        await client.start('BOT_TOKEN')

asyncio.run(main())
