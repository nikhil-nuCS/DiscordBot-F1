# DiscordBot-F1

## Sports tech Project

### Members: Nikhil Khandelwal, Preeti Subbiah, Rutuja Kajave

## Description

A simple bot application using the `discord.py` library to view [Formula 1](https://www.formula1.com/) statistics within Discord. The bot fetches data from [Ergast API](http://ergast.com/mrd/) using commands invoked by members of the discord server which can then display data such as driver career, world driver championship, world constructor championship and even predictions about future races.

## Installation

This application requires Python 3.7+ to be installed.

`$ git clone https://github.com/nikhil-nuCS/DiscordBot-F1.git` <br/>
`$ cd DiscordBot-F1`

## Creating a Bot user

Open [Discord Developer Portal](https://discord.com/developers/applications/) and create a new application. The name you use for the application will be displayed as the username of your bot. On the application page, choose the Bot from the settings menu and then click the 'Add Bot' button to turn your application into a bot.

Copy the Token of your bot to the `main.py` file in the `src/out` folder and replace it with the value of the `TOKEN` key. Your token is like a password and hence do not share it with anyone.

Alternatively, you can store the token in an environment variable so that you avoit adding it to the main file. The environment variable will be checked first when loading the bot. This is a useful way to work around the project if you use a cloud based host.

## Inviting your Bot

To add the bot to a server, you need to generate an OAuth2 URL for authentication and permissions purpose. To do so

1. Open the [Application](https://discord.com/developers/applications/) page of your Bot and under the settings section, choose OAuth2.
2. In the Scopes section, check 'bot'.
3. Scroll to Permissions section and enable features which you might use for your bot.
4. The Scopes section will now share a url representing the scope and permissions of your bot.
5. Copy this URL to invite your Bot to a server which you have permissions to.

## Usage

To run the application, execure `python main.py` from your main directory. This will start the bot process and attempt to connect with the provided Token. The console will display log messages to monitor the bot status. `Ctrl + C` will stop the process and close the connection to the bot.

## Commands

Invoke a command in discord by typing the prefix `!b` (this symbol can be changed in the code block) and one of the following commands:

`!b purpose` - Displays the purpose of this project <br/>
`!b career [driver id/ driver given name / driver number]` - Displays details about the driver as well as his career statistics. <br/>
`!b circuits [season]` - Displays all the circuits for that particular year. If a season isn't mentioned in the command, it will by default display the circuits for the last season.<br/>
`!b circuit [circuit id]` - Displays the details and the route for a particular circuit. <br/>
`!b wdc [season]` - Displays World Driver Championship standings. If a season isn't mentioned, the program will by default send back the standings for the latest season.<br/> 
`!b wcc [season]` - Displays World Constructor Championship standings. If a season isn't mentioned, the program will by default send back the standings for the latest season.<br/> 
`!b results [season][round]` - Displays the standings for a particular season for a particular round. If season and round are not mentioned, standings for latest season's last round will be displayed by default. <br/>
`!b quali [season][round]` - Displays the standings qualifiers for a particular season for a particular round. If season and round are not mentioned, standings for latest season's last round will be displayed by default. <br/>
`!b pitstops [season][round]` - Displays pitstops taken by players during a particular round in a particular season. If season and round are not mentioned, pitstop information for latest season's last round will be displayed by default.<br/>
`!b predict [race/quali]` - Will predict results for either a race or a qualifier, depending on the suffix used in the command using past race data for the drivers. <br/>
`!b plot timings [season][round][driver1, driver2, ... n]` - Plots a graph for lap timings of drivers included in the array. Drivers can be addressed using driver id, given name or driver number. 