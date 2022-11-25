from tabulate import tabulate
from utils import is_future, get_driver_full_name
import discord
from discord.ext import commands
import ergast_py

intent = discord.Intents.default()
intent.message_content = True
bot = commands.Bot(command_prefix="!b ", intents=intent)

ergast_api = ergast_py.Ergast()


async def check_season_validity(season_year):
    if is_future(season_year):
        return False
    return True


@bot.event
async def on_ready():
    print("Bot logged in as {0.user}. Ready for use.".format(bot))


@bot.command()
async def purpose(ctx):
    await ctx.send("F1 Bot for CS 397 - STL Final Project")


@bot.command()
async def career(ctx, driver_id):
    embed = discord.Embed(title="Driver Career Stats Request Response", description="Sample description")
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    driver_info = ergast_api.driver(driver_id).get_driver()

    embed.add_field(name="Driver Name", value=driver_info.given_name + " " + driver_info.family_name)
    embed.add_field(name="Code", value=driver_info.code)
    embed.add_field(name="Driver Number", value=driver_info.permanent_number)
    embed.add_field(name="Nationality", value=driver_info.nationality)
    embed.add_field(name="DOB", value=driver_info.date_of_birth)
    embed.add_field(name="Driver ID", value=driver_info.driver_id)
    embed.add_field(name="URL", value=driver_info.url)
    await ctx.send(embed=embed)
    return


@bot.command()
async def circuits(ctx, season="current"):
    circuit_list = ergast_api.season(season).get_races()
    if not circuit_list:
        await ctx.send("Could not find information")
        return
    ans = []
    for circuit in circuit_list:
        ans.append([circuit.race_name, circuit.circuit.location.country])
    table_format = tabulate(ans, headers=["Name", "Location"], tablefmt="simple")
    await ctx.send(f"```\n{table_format}\n```")
    return


@bot.command()
async def circuit(ctx, circuit_name):
    # if not circuit_name:
    #     return
    circuit_info = ergast_api.circuit("silverstone").get_circuit()
    print(circuit_info)
    return


@bot.command()
async def nextrace(ctx):
    # next_race = readymade_api.
    return


@bot.command()
async def wdc(ctx, season="current"):
    standings = ergast_api.season(season).get_driver_standings()[0]
    ans = []
    for standing in standings.driver_standings:
        ans.append([standing.position, get_driver_full_name(standing.driver), standing.constructors[0].name, standing.points])
    table = tabulate(ans, headers=["Position", "Driver", "Team", "Points"])
    await ctx.send(f"```\n{table}\n```")
    return


@bot.command()
async def wcc(ctx, season="current"):
    standings = ergast_api.season(season).get_constructor_standings()[0]
    ans = []
    for standing in standings.constructor_standings:
        ans.append([standing.position, standing.constructor.name, standing.points])
    table = tabulate(ans, headers=["Position", "Team", "Points"])
    await ctx.send(f"```\n{table}\n```")
    return


@bot.command()
async def results(ctx, season="current", round="last"):
    result = ergast_api.season().get_results()
    print(result)
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    return
