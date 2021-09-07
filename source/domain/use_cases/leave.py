import discord


def leave(ctx, client, discord=discord):
    async def leave(ctx=ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    return leave
