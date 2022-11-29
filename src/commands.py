import asyncio

import plot as plot
from tabulate import tabulate
from utils import is_future, get_driver_full_name, get_formatted_date, get_formatted_pit_stop_time
from fetch import fetch
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
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    driver_info = ergast_api.driver(driver_id).get_driver()
    embed = discord.Embed(title=f"{driver_info.driver_id} Information:",
                          description="Information about the requested driver can be seen here",
                          url=driver_info.url)
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
        ans.append([circuit.race_name, circuit.circuit.location.country, get_formatted_date(circuit.date)])
    table_format = tabulate(ans, headers=["Name", "Location", "Date"], tablefmt="simple")
    await ctx.send(f"```\n{table_format}\n```")
    return


@bot.command()
async def circuit(ctx, circuit_name):
    circuit_info = ergast_api.circuit(circuit_name).get_circuit()
    print(circuit_info)
    return


@bot.command()
async def nextrace(ctx):
    next_race = ergast_api.season().status()
    print(next_race)
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


@bot.command()
async def predict(ctx, event="race"):
    url = "https://www.f1-predictor.com/api-next-race-prediction/"
    res = await fetch(url)
    print(res)
    ans = []
    ind = 1
    if event == "race" or event == "qualifying":
        for driver, driver_num in res[event]["ranking"].items():
            ans.append([ind, driver])
            ind += 1
        table = tabulate(ans, headers=["Position", "Name"])
        await ctx.send(f"```\n{table}\n```")
        return
    else:
        ctx.send("Can only predict 'race' and 'qualifying'")
        return


@bot.command()
async def pitstops(ctx, season="current", round_no="last"):
    if not season == "current" and int(season) < 2012:
        await ctx.send("Pit stop data available only after 2012 season")
        return

    stops = ergast_api.season(season).round(round_no).get_pit_stops()[0]
    ans = []
    for pit_stop in stops.pit_stops:
        ans.append([pit_stop.lap, pit_stop.driver_id, pit_stop.stop, get_formatted_pit_stop_time(pit_stop.duration)])
    table = tabulate(ans, headers=["Lap Number", "Driver ID", "Stop number", "Pit time (sec)"])
    await ctx.send(f"```\n{table}\n```")
    return

# @plot.command(aliases=['laps'])
# async def timings(ctx, season: int = 'current', rnd: int = 'last', *drivers):
#     if not (len(drivers) == 0 or drivers[0] == 'all'):
#         driver_list = [ergast_api.driver(d).get_driver().driver_id for d in drivers]
#     else:
#         driver_list = []
#     laps_task = asyncio.create_task(ergast_api.season(season).round(rnd).get_all_laps())
