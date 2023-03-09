print("defining functions")
import discord, pytube, os, threading, time
from moviepy import editor
from discord.ext.commands import Bot
bot = Bot("b!",intents=discord.Intents.all())
check = False
token = "MTA1NDA0NzcxMjkyMTc5NjcxMQ.GPvYcn.hgmsaIEiz-M0c-hvzWRaDJyfyqm4f3QIJXOy7A"
@bot.command()
async def play(ctx, arg):
    check = False
    try:
        check = vc.is_playing()
    except Exception:
        pass
        if check == False:
            await ctx.send("Downloading...")
            try:
                yt = pytube.YouTube(arg)
                print("FOUND STREAM: "+str(yt.streams.filter(only_audio=True,mime_type="audio/webm",type="audio",abr="160kbps")))
                def download(yt):
                    print("DOWNLOADING STREAM TO AUDIO.WEBM")
                    yt.streams.filter(only_audio=True,mime_type="audio/webm",type="audio",abr="160kbps").order_by("abr").first().download(filename="audio.webm")
                    print("EXPORTING TO MP3")
                    editor.AudioFileClip("audio.webm").write_audiofile("audio.webm"[:-5] + ".mp3")
                    os.remove("audio.webm")
                    print("SENDING FILE")
                    ctx.send(file=discord.File(r'audio.mp3'))
                    print("DONE")
                thread = threading.Thread(target=download, args=(yt,))
                thread.start()
                thread.join()
            except Exception:
                await ctx.send("An Error occured.")
            channel = ctx.author.voice.channel
            try:
                vc = await channel.connect()
            except Exception:
                vc = channel
            vc.play(discord.FFmpegPCMAudio(source="C:\\Users\\Administrator\\Programmier Stuff\\Python\\Bot 3\\audio.mp3", executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"))
        else:
            await ctx.send("Something already playing idk")
bot.run(token)
