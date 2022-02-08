import aiohttp
import discord
from discord.ext import commands

class Animals(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    @commands.command(aliases=["meow", "kitty"])
    async def cat(self, ctx):
        async with self.session.get("https://aws.random.cat/meow") as res:
            res = await res.json()
            url = res["file"]
        embed = discord.Embed(color=discord.Color.from_rgb(54, 57, 63), title="Meow 🐈")
        embed.set_image(url=url)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["quack", "qwuak"])
    async def duck(self, ctx):
        async with self.session.get("https://random-d.uk/api/random") as res:
            res = await res.json()
            url = res["url"]
        embed = discord.Embed(color=discord.Color.from_rgb(54, 57, 63), title="Quack Quack 🦆")
        embed.set_image(url=url)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Animals(client))
