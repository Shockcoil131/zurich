import os
import random
import discord
from dotenv import load_dotenv
import csv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

with open('./zurich_quotes.csv', newline='') as f:
    reader = csv.reader(f)
    zurich_quotes = list(reader)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    percentage_chance = 0.025
    if random.random() < percentage_chance:
        response = random.choice(zurich_quotes)[0]
        await message.channel.send(response)

client.run(TOKEN)
