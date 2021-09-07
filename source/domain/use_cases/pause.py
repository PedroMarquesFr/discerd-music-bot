import discord


def pause(ctx, client, discord=discord):
    async def pause(ctx=ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            voice.resume()

    return pause
