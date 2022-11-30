from tabulate import tabulate

import load
import utils
from utils import is_future, get_driver_full_name, get_formatted_date, get_formatted_pit_stop_time, get_formatted_quali_time
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
    await ctx.send("Discord F1 Bot for CS 397 - STL Final Project")


@bot.command()
async def career(ctx, driver_inp):
    await ctx.send("*Gathering driver data, this may take a few moments...*")
    driver_id = utils.find_driver(driver_inp)["driverId"]
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


@bot.command(aliases=['races'])
async def circuits(ctx, season="current"):
    await ctx.send("*Gathering circuit data, this may take a few seconds...*")
    circuit_list = ergast_api.season(season).get_races()
    if not circuit_list:
        await ctx.send("This information is currently not available.")
        return
    ans = []
    for circuit in circuit_list:
        ans.append([circuit.race_name, circuit.circuit.location.country, get_formatted_date(circuit.date)])
    table_format = tabulate(ans, headers=["Name", "Location", "Date"], tablefmt="simple")
    await ctx.send("\n Circuit information for {}".format(season))
    await ctx.send(f"```\n{table_format}\n```")
    return


@bot.command()
async def circuit(ctx, circuit_name):
    circuit_info = ergast_api.circuit(circuit_name).get_circuit()
    embed = discord.Embed(title=f"Circuit Information:",
                          description="Information about the requested circuit and layout",
                          url=circuit_info.url)
    embed.add_field(name="Circuit Name", value=circuit_info.circuit_name)
    embed.add_field(name="Country", value=circuit_info.location.locality + ", " + circuit_info.location.country)
    embed.add_field(name="Laps", value=load.get_circuit_lap_number(circuit_name))
    embed.add_field(name="Circuit Length", value=load.get_circuit_length(circuit_name))
    embed.set_image(url=load.load_track_layout(circuit_name))
    await ctx.send(embed=embed)
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
    await ctx.send("\n World Drivers' Championship information for {}".format(season))
    await ctx.send(f"```\n{table}\n```")
    return


@bot.command()
async def wcc(ctx, season="current"):
    standings = ergast_api.season(season).get_constructor_standings()[0]
    ans = []
    for standing in standings.constructor_standings:
        ans.append([standing.position, standing.constructor.name, standing.points])
    table = tabulate(ans, headers=["Position", "Team", "Points"])
    await ctx.send("\n World Constructors' Championship information for {}".format(season))
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
        await ctx.send("\n Predictions for the next {}".format(event))
        await ctx.send(f"```\n{table}\n```")
        return
    else:
        ctx.send("Can only predict 'race' and 'qualifying'")
        return


@bot.command()
async def pitstops(ctx, season="current", round_no="last"):
    if not season == "current" and int(season) < 2012:
        await ctx.send("Pit stop data is only available for seasons after 2012")
        return

    stops = ergast_api.season(season).round(round_no).get_pit_stops()[0]
    ans = []
    for pit_stop in stops.pit_stops:
        driver_info = utils.find_driver(pit_stop.driver_id)
        ans.append([pit_stop.lap, driver_info["familyName"], pit_stop.stop, get_formatted_pit_stop_time(pit_stop.duration)])
    table = tabulate(ans, headers=["Lap Number", "Driver", "Stop number", "Pit time (sec)"])
    await ctx.send("\n Pit stop data for {}".format(season))
    await ctx.send(f"```\n{table}\n```")
    return


@bot.command()
async def qualifying(ctx, season="current", round_no="last"):
    if not season == "current" and int(season) < 2012:
        await ctx.send("Qualifying data is only available for seasons after 2012")
        return

    quali_result = ergast_api.season(season).round(round_no).get_qualifying().qualifying_results
    ans = []
    for quali in quali_result:
        ans.append([
            quali.position,
            quali.driver.code,
            get_formatted_quali_time(quali.qual_1),
            get_formatted_quali_time(quali.qual_2),
            get_formatted_quali_time(quali.qual_3),
        ])
    table = tabulate(ans, headers=["Position Number", "Driver", "Q1", "Q2", "Q3"])
    await ctx.send("\n Qualifying data for {}".format(season))   
    await ctx.send(f"```\n{table}\n```")
    return


@bot.group(invoke_without_command=True, case_insensitive=True)
async def plot(ctx, *args):
    """Command group for all plotting functions."""
    await ctx.send(f"Command not recognised. Type `{bot.command_prefix}help plot` for plotting subcommands.")


@plot.command(aliases=['laps'])
async def timings(ctx, season="current", round_no="last", *drivers):
    if len(drivers) == 0:
        await ctx.send("Drivers needed")
        return
    driver_list = [utils.find_driver(d)["driverId"] for d in drivers]
    utils.get_lap_timings_plot(season, round_no, driver_list)
    plotted_figure = load.load_figure("plot_laps.png")
    await ctx.send("\n Plot of the timings of {0} for {1}".format(drivers, season))
    await ctx.send(file=plotted_figure)
    return
