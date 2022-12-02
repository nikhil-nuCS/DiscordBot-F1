# DiscordBot-F1

## Sports tech Project
### Members: Nikhil Khandelwal, Preeti Subbiah, Rutuja Kajave

## Description

A simple bot application using the `discord.py` library to view [Formula 1](https://www.formula1.com/) statistics within Discord. The bot fetches data from [Ergast API](http://ergast.com/mrd/) using commands invoked by members of the discord server which can then display data such as driver career, world driver championship, world constructor championship and even predictions about future races. 

## Installation

This application requires Python 3.7+ to be installed. 

`$ git clone https://github.com/nikhil-nuCS/DiscordBot-F1.git`
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
