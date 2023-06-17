from __future__ import unicode_literals
import os
import discord
import yt_dlp
from yt_dlp import YoutubeDL
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client)


@tree.command(name = "download_yt_audio", description = "Give me a URL to extract audio from", guild=discord.Object(id=223167064112627714))
async def seccond_command(interaction: discord.Interaction, text: str):
    await interaction.response.defer()
    
    brukerid = interaction.user.id
    mp3_filepath = fr'C:\Users\ander\Documents\Progging\DiscordBotPython\{brukerid}.mp3'
    ydl_opts = {
    'format': 'best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192', }],
    'verbose': True,
    'windowsfilenames': True,
    'outtmpl': fr'C:\Users\ander\Documents\Progging\DiscordBotPython\{brukerid}',
    'ffmpeg_location': r'C:\Users\ander\Documents\Progging\DiscordBotPython\ffmpeg-2023-06-11-git-09621fd7d9-full_build\bin\ffmpeg.exe',
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f'{text}'])
        except yt_dlp.utils.DownloadError:
            await interaction.followup.send("Feil: Er dette en fullstendig og gyldig URL?")
            return
        
    
    mp3_file = discord.File(fp=mp3_filepath, filename='Funny meme.mp3')
    channel = await interaction.user.create_dm()

    await channel.send(content='I gotchu chief: ', file=mp3_file)
    await interaction.followup.send("Sjekk postkassen din. Mvh")
    
    os.remove(mp3_filepath) 


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=223167064112627714))
    print(f'{client.user} Has connected to Discord!')


client.run(TOKEN)
