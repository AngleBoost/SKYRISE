import random
import discord
import json
import requests
from discord.ext import commands

class funStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def __getitem__(self,x):
        self.x = x


    @commands.command(name='funCmds')
    async def funcmds(self, ctx):
        embed = discord.Embed(title="Command List", color=0x99CCFF)
        embed.add_field(name='sr.8ball', value='Let the 8 Ball Predict!', inline=False)
        embed.add_field(name='sr.funnyrate', value=' This command is used to rate the funniness of a given statement or phrase on a scale of 1-100%.', inline=False)
        embed.add_field(name='sr.ship', value='This command is used to generate a ship name for two given names.', inline=False)
        embed.add_field(name='sr.joke', value='This command is used to generate a random joke.', inline=False)
        embed.add_field(name='sr.roll', value='This command is used to generate a random number within a given range.', inline=False)
        embed.add_field(name='sr.rps', value='This command is used to play a game of rock-paper-scissors against the computer.', inline=False)
        embed.add_field(name='sr.catfact', value='This command is used to generate a random fact about cats.', inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='8ball', description='Let the 8 Ball Predict!\n')
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                'Yes.',
                'Positive',
                'From my point of view, yes',
                'Convinced.',
                'Most Likley.',
                'Chances High',
                'No.',
                'Negative.',
                'Not Convinced.',
                'Perhaps.',
                'Not Sure',
                'Mayby',
                'I cannot predict now.',
                'Im to lazy to predict.',
                'I am tired. *proceeds with sleeping*']
        response = random.choice(responses)
        embed=discord.Embed(title="The Magic 8 Ball has Spoken!", color=0x99CCFF)
        embed.add_field(name='Question: ', value=question, inline=True)
        embed.add_field(name='Answer: ', value=response, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def funnyrate(self, ctx):
        embed=discord.Embed(title=f"You are {random.randrange(101)}% funny!", color=0x99CCFF)
        await ctx.send(embed=embed)


    @commands.command()
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        """Ship two members together"""
        ship_percent = random.randint(1, 100)
        name1 = member1.name[:len(member1.name)//2]
        name2 = member2.name[len(member2.name)//2:]
        nameship = name1 + name2

        embed = discord.Embed(
            title=f"{member1.name} x {member2.name} = {nameship}",
            description=f"**Compatibility: {ship_percent}%**",
            color=0xFF0000
        )
    
        if ship_percent <= 35:
            embed.add_field(name="Result", value="😅 There doesn't seem to be such great chemistry going on, but who knows...?")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1067596766356185131/1068988991145259018/brokenheart_ship.gif")
        elif ship_percent > 35 and ship_percent <= 65:
            embed.add_field(name="Result", value="🫤 This combination has potential, how about a romantic dinner?")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1067596766356185131/1068989461083455548/thinking_ship.gif")
        elif ship_percent > 65:
            embed.add_field(name="Result", value="😍 Perfect combination! When will the wedding be?")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1067596766356185131/1068986257826402304/ship.gif")

        await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx, filter: str = 'Any'):
        url = f"https://jokeapi.dev/joke/{filter}?type=single&flags=nsfw-filter"
        try:
            res = requests.get(url)
            data = json.loads(res.text)
            if "setup" in data:
                joke = f"{data['setup']}...{data['delivery']}"
            else:
                joke = data["joke"]
            embed = discord.Embed(title="Joke", description=joke, color=0x99CCFF)
            await ctx.send(embed=embed)
        except requests.exceptions.RequestException as e:
            await ctx.send(f"Error: {e}")


    @commands.command()
    async def roll(self, ctx):
        """Roll a dice"""
        roll = random.randint(1, 6)
        embed = discord.Embed(title=f"Rolling a dice...", description=f"You rolled a {roll}!", color=0x99CCFF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1067596766356185131/1068993152784023705/roll-the-dice.gif")
        await ctx.send(embed=embed) 

    @commands.command()
    async def rps(self, ctx, choice: str):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        result = ""
        if choice.lower() not in choices:
            result = "Invalid choice. Please choose rock, paper or scissors."
        elif choice.lower() == computer_choice:
            result = "It's a tie! You both chose " + choice + "."
        elif (choice.lower() == "rock" and computer_choice == "scissors") or (choice.lower() == "paper" and computer_choice == "rock") or (choice.lower() == "scissors" and computer_choice == "paper"):
            result = "You win! " + choice + " beats " + computer_choice + "."
        else:
            result = "You lose! " + computer_choice + " beats " + choice + "."
        embed = discord.Embed(title="Rock, Paper, Scissors", description=result, color=0x99CCFF)
        embed.set_footer(text="Powered by RPSAPI")
        await ctx.send(embed=embed)

    @commands.command()
    async def catfact(self, ctx):
        url = "https://cat-fact.herokuapp.com/facts/random"
        fact = json.loads(requests.get(url).text)["text"]
        embed = discord.Embed(title="Fun Cat Fact", description=fact, color=0x99CCFF)
        embed.set_footer(text="Powered by CatFactsAPI")
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(funStuff(client))