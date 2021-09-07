import discord
from discord.errors import ClientException
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def play(ctx, url: str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Geral")
    try:
        await voiceChannel.connect()
    except ClientException:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
            return voice.play(discord.FFmpegOpusAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        voice.resume()


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    os.remove("song.mp3")


client.run(os.getenv("DISC_TOKEN"))
