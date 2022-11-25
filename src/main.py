import ergast_py
import pprint
import discord
from discord.ext import commands
import random
import asyncio
from discord import Colour
from tabulate import tabulate

readymade_api = ergast_py.Ergast()
# try:
#     seasons = readymade_api.limit(100).get_seasons()
#     print(seasons)
#     # for driver in drivers:
#     #     print(driver)
# except Exception as e:
#     print(e)
# print("LOSA")

# Change the token before doing any changes
TOKEN = "MTA0NTEyNTQ4NTIwNzc2MTAyNw.G7wap7.8tzyD8EdPE2Eqjfhcj8ZUXGIA8X4DoOpBJ5Ws0"
intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix="!fb ", intents=intent)


def too_long(message):
    """Returns True if the message exceeds discord's 2000 character limit."""
    return len(message) >= 2000


def make_table(data, headers='keys', fmt='fancy_grid'):
    """Tabulate data into an ASCII table. Return value is a str.
    The `fmt` param defaults to 'fancy_grid' which includes borders for cells. If the table exceeds
    Discord message limit the table is rebuilt with borders removed.
    If still too large raise `MessageTooLongError`.
    """
    table = tabulate(data, headers=headers, tablefmt=fmt)
    # remove cell borders if too long
    if too_long(table):
        table = tabulate(data, headers=headers, tablefmt='simple')
        # cannot send table if too large even without borders
        if too_long(table):
            print('Table too large to send.')
    return table


DISABLE_DM = False


async def get_target(ctx, msg_type):
    """Check if the target of a command response should be direct message or channel.
    Returns an object of `ctx.author` or the original `ctx`.
    Parameters
    ----------
    `ctx` : Context
        The invocation context of the command.
    `msg_type`: str
        Type of message response: 'table', 'file', 'image', 'error' or 'embed'. Regular text will
        be sent to the channel unless part of the command response of the previous types.
    """
    if DISABLE_DM:
        DM = False
    if DM:
        return ctx.author
    else:
        return ctx


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
