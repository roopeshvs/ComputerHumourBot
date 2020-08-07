# ComputerHumourBot

A Discord Bot that responds with a random one-liner from a massive collection of the distilled wisdom and humor of the ages.

## Setting Up The Bot

Create a Discord Bot at https://discord.com/developers/applications/
Authenticate the Bot and Add it to your Discord Server.

## Cloning The Repo

Clone the repository using the command

`git clone https://github.com/roopeshvs/ComputerHumourBot.git`

## Creating A Python Virtual Environment

For Linux, use
`python3 -m venv QuoteBot`

For Windows, use
`python -m venv QuoteBot`

## Activating A Python Virtual Environment

For Linux Bash, use
`QuoteBot/bin/activate`

For Windows Command Prompt, use
`QuoteBot\Scripts\activate.bat`

## Configuring The Bot

Get The Bot Token from Discord.
Note that Token and Client Secret are not the same.

Create a file called token.config and enter the follwing,
> [DISCORD]

> TOKEN = "Paste Your Bot Token Here. Without Quotes."

## Installing Dependencies

Install the required dependencies by running the command,
`pip install -r requirements.txt`

## You Are All Set

Run the Bot using the command,
`python QuoteBot.py` or `python3 QuoteBot.py`

The Bot should be online in your Discord Server Now.

## Bot Commands

`{}help` - List of Commands.

`{}quote` - A Random One-Liner from quotes.txt

`{}add` - Add two numbers

`{}sub` - Subtract two numbers

## Bot Events

- Greets New Users
- If any message contains the string QuoteBot, the bot responds with a heart.

## Usage

Please feel free to modify anything and everything.
Created this to use as a template for any bots I create.