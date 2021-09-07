import discord
import os


def stop(ctx, client, discord=discord):
    async def stop(ctx=ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        os.remove("song.mp3")

    return stop
