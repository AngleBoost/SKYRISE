# SkyRise discord bot

This script is a Discord bot written in Python using the discord.py library. It utilizes the discord.ext.commands extension for command handling and the discord.tasks module for background tasks. The bot is case-insensitive and uses a custom prefix of either "sr." or "SR.". It sets up event handlers for the bot's status, user join events, and command errors. The bot also uses aiohttp for HTTP requests.

When the bot is ready, it starts the change_status loop task that changes the bot's status message every 5 seconds. When a new member joins either of two specified guilds, the bot sends a welcome message to a specified channel in that guild. The welcome message includes information about the new member and a list of suggested channels to check out. The bot also implements an on_command_error handler that sends an error message when a user attempts to use a command they do not have permission to use.

## Getting Started

These instructions will get you up and running with the bot on your Discord server.

### Prerequisites

- A Discord account and server
- [Discord Developer Portal](https://discord.com/developers/applications) account
- [Python](https://www.python.org/downloads/) 3.x installed on your machine
- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) library installed (`pip install discord.py`)

### Installation

1. Clone or download the repository to your local machine
2. Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications)
3. Create a new bot for the application
4. Copy the bot token
5. Open the project in your terminal and run `pip install -r requirements.txt` to install the dependencies
6. Create a `.env` file in the root of the project and paste the following, replacing `BOT_TOKEN` with the token you copied earlier:
7. Run the bot by executing `python bot.py`

## Usage

The bot will automatically respond to certain commands, but you can also write your own commands. See the [discord.py documentation](https://discordpy.readthedocs.io/en/latest/index.html) for more information.

## Contributing

If you would like to contribute to the development of the bot, please follow these guidelines:

1. Fork the repository
2. Create a new branch for your changes
3. Make the changes and commit them to your branch
4. Open a pull request, explaining your changes

## License

This project is licensed under the MIT License.

## Acknowledgments

- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html)
- [Python](https://www.python.org/downloads/)
