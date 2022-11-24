import ergast_py
import pprint
import discord
from discord.ext import commands
import random

readymade_api = ergast_py.Ergast()
# try:
#     seasons = readymade_api.limit(100).get_seasons()
#     print(seasons)
#     # for driver in drivers:
#     #     print(driver)
# except Exception as e:
#     print(e)
# print("LOSA")

TOKEN = "MTA0NTA4ODUxMjIzNzY0OTk3MQ.GNj7w0.8KpwEC7Jr3JhTieTAJKoCmZX6n6Pz3-NrqrAA4"
intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix="!fb ", intents=intent)


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


# @bot.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#     print(f'{username}: {user_message} ({channel})')
#
#     if message.author == client.user:
#         return
#
#     if channel == "stl-f1-bot":
#         if user_message.lower() == "hello":
#             await message.channel.send("Hello there!")
#             return
#         elif user_message.lower() == "bye":
#             await message.channel.send("See you later")
#             return


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def course(ctx):
    await ctx.send("STL - CS 397")


@bot.command()
async def driver(ctx, driver_id):
    print(driver_id)
    driver_info = readymade_api.driver(driver_id).get_driver()
    await ctx.send(driver_info.given_name + " " + driver_info.family_name)


@bot.command()
async def stats(ctx, driver_id):
    embed = discord.Embed(title="Driver Stats Request Response",description="Apna Kaam Banta Bhad mein jaye jaanta")
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    driver_info = readymade_api.driver(driver_id).get_driver()

    embed.add_field(name="Driver Name", value= driver_info.given_name + " " + driver_info.family_name)
    embed.add_field(name="Code", value= driver_info.code)
    embed.add_field(name="Driver Number", value= driver_info.permanent_number)
    embed.add_field(name="Nationality", value= driver_info.nationality)
    embed.add_field(name="DOB", value= driver_info.date_of_birth)
    embed.add_field(name="Driver ID", value= driver_info.driver_id)
    embed.add_field(name="URL", value= driver_info.url)
    await ctx.send(embed=embed)

bot.run(TOKEN)
