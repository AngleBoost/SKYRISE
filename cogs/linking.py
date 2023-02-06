import discord
import asyncio
import random
import string
import requests
from discord.ext import commands
import sqlite3

class linking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS links (discord_id TEXT, minecraft_username TEXT, code TEXT)''')
        self.conn.commit()

    @commands.command()
    async def linkmc(self, ctx):
        # Ask the user to enter their Minecraft username
        await ctx.send("Please enter your Minecraft username:")

        # Wait for the user's response
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.isprintable() and len(message.content) <= 16
        try:
            message = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Timed out. Please try again.")
            return
        username = message.content
        # Make a request to the Minecraft API to check if the username is valid
        url = f"https://api.mojang.com/users/profiles/minecraft/{username}"

        def generate_code():
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        try:
            response = requests.get(url)

            # Check the response status code
            if response.status_code == 200:
                # Generate a random code
                code = generate_code()

                conn = sqlite3.connect('database.db')
                c = conn.cursor()
                c.execute("INSERT INTO links (discord_id, minecraft_username, code) VALUES (?, ?, ?)", (ctx.author.id, username, code))
                conn.commit()
                conn.close()
                await ctx.author.send(f"Your code is {code}. Please enter it on the Minecraft server with the command '/linkdiscord {code}'")
            else:
                # If the status code is not 200, the
                await ctx.send("Invalid Minecraft username. Please try again.")
        except Exception as e:
            await ctx.send("An error occurred. Please try again later.")
            print(e)


    @commands.command()
    async def linkdiscord(self, ctx, code):
        try:
            # Check if the code is valid
            conn = sqlite3.connect('database.db')
            c = conn.cursor()

            c.execute("SELECT * FROM links WHERE code = ?", (code,))
            result = c.fetchone()

            if not result:
                await ctx.send("Invalid code. Please try again.")
                return

            discord_id, minecraft_username, _ = result
            c.execute("UPDATE links SET discord_id = ? WHERE minecraft_username = ?", (ctx.author.id, minecraft_username))

            conn.commit()
            conn.close()
            # Link the user's Discord account to their Minecraft account
            await ctx.send("Your accounts have been linked!")

        except Exception as e:
            await ctx.send("An error occurred: {}".format(e))


async def setup(client):
    await client.add_cog(linking(client))