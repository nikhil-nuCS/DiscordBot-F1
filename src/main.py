import ergast_py
import pprint
import discord
from discord.ext import commands
from discord import Colour
from tabulate import tabulate

readymade_api = ergast_py.Ergast()
TOKEN = "MTA0NTEyNTQ4NTIwNzc2MTAyNw.G7wap7.8tzyD8EdPE2Eqjfhcj8ZUXGIA8X4DoOpBJ5Ws0"
intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix="!fb ", intents=intent)


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def course(ctx):
    await ctx.send("STL - CS 397")


@bot.command(aliases=['source', 'git'])
async def github(ctx, *args):
    """Display a link to the GitHub repository."""
    await ctx.send("https://github.com/nikhil-nuCS/DiscordBot-F1")


@bot.command()
async def driver(ctx, driver_id):
    driver = readymade_api.driver(driver_id).get_driver()
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    embed = discord.Embed(title=f"{driver.driver_id} Information:",
                          description="Information about the requested driver can be seen here",
                          url=driver.url,
                          colour=Colour.teal(),
                          )
    embed.add_field(
        name='Full Name', value=driver.given_name+" "+driver.family_name, inline=True)
    embed.add_field(
        name='Number', value=driver.permanent_number, inline=True)
    embed.add_field(name='Nationality',
                    value=driver.nationality, inline=True)
    embed.add_field(
        name='DOB', value=driver.date_of_birth, inline=True)
    embed.add_field(
        name='Code', value=driver.code, inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def stats(ctx, driver_id):
    embed = discord.Embed(title="Driver Stats ",
                          description="Statistics for the driver are mentioned below")
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    driver_info = readymade_api.driver(driver_id).get_driver()

    embed.add_field(name="Driver Name",
                    value=driver_info.given_name + " " + driver_info.family_name)
    embed.add_field(name="Code", value=driver_info.code)
    embed.add_field(name="Driver Number", value=driver_info.permanent_number)
    embed.add_field(name="Nationality", value=driver_info.nationality)
    embed.add_field(name="DOB", value=driver_info.date_of_birth)
    embed.add_field(name="Driver ID", value=driver_info.driver_id)
    embed.add_field(name="URL", value=driver_info.url)
    await ctx.send(embed=embed)

bot.run(TOKEN)
