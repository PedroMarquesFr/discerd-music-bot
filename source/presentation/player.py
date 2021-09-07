import discord
from discord.errors import ClientException
from discord.ext import commands
import youtube_dl
import os
from domain.use_cases.leave import leave as leave_use_case
from domain.use_cases.pause import pause as pause_use_case
from domain.use_cases.stop import stop as stop_use_case

client = commands.Bot(command_prefix="!")

def initialize_bot():
    
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
        leave_use_case(ctx, client)


    @client.command()
    async def pause(ctx):
        pause_use_case(ctx, client)


    @client.command()
    async def stop(ctx):
        stop_use_case(ctx, client)


    client.run(os.getenv("DISC_TOKEN"))
