import discord
from os import getenv

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client}")


@client.event
async def on_message(message):
    # print(message)
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Fala tu")

    if message.content.startswith("!play "):
        music_name_or_link = message.content.split("!play ")
        print(music_name_or_link)
        await message.channel.send("tocando a braba")
        await message.channel.send("ala")


client.run(getenv("DISC_TOKEN"))
