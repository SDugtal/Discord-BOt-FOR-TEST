import discord
from discord.ext import commands
from discord  import FFmpegPCMAudio
import requests
from discord import Member
from discord.ext.commands import has_permissions 
#from discord.ext.commands import  Missing_Permissions
import os
from dotenv import load_dotenv
load_dotenv()

#intents=discord.Intents.default()
#intents.members=True
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#client= commands.Bot(command_prefix= '!' ,intents=intents)
# intents=discord.Intents.all()) and enable all the "intents" in the bot section of the developer portal.
@client.event
async def on_ready():
    print("the bot is now ready for use --")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
@client.command()
async def chintan(ctx):
    await ctx.send("pagal")
    client.command()       
@client.command()
async def hello(ctx):
    await ctx.send("hello , i am shirshak the bot ")
    client.command()
@client.command()
async def discord(ctx):
    await ctx.send("for try")
    print("for tryy")
@client.command()
async def goodbye(ctx):
    await ctx.send("goodbye broooo")
@client.command()
async def mani(ctx):
    await ctx.send("4 foot ki hai ")
#server join and leave 
@client.event
async def on_member_join(member):
    channel=client.get_channel(1155884215108391115)
    await channel.send('Welcome to the server ')
@client.event    
async def on_member_remove(member):
    channel=client.get_channel(1155884215108391115)
    await channel.send('removed ')
    #join and remove function with audio 
@client.command(pass_context=True)
async def join(ctx):
    if(ctx.author.voice):
        channel=ctx.message.author.voice.channel
        voice=await channel.connect()
        source=FFmpegPCMAudio('tune.mp3')
        player= voice.play(source)
    else:
        await ctx.send("you are not in voice channel , you must be in voice channel to run this command ")
@client.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("i leave the voice channel ")
    else:
        await ctx.send("i am not in the voice channel ")     
# aayien?
'''
@client.command(pass_context = True)
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause
  else: 
    await ctx.send("`Nothing is currently playing right now!`")

@client.command(pass_context = True)
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send("`Nothing is currently paused right now!`")
    '''
@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()
@client.command(name='stop', help='This command stops the song!')    
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()   
@client.event
async def on_message(message):
    lis = ["fuck","chintan"]
    #these stars are abusive language
    for i in lis:
        if message.content == i:
            await message.delete()

            await message.channel.send("don't send this message other wise you will be banned")  
            
            continue 
            
        else:
            await client.process_commands(message) 
            break

@client.command()
@has_permissions(kick_member=True) 
async def kick(ctx ,member=discord.member,* ,reason =None):
    await member.kick(reason=reason)
    await ctx.send(f'user {member}has been kick ')
@kick.error()
async def kick_error(ctx ,error):
    if isinstance(error , Missing.Permission):
        await ctx.send("you don't have permisssion to kick someone")

id_key = os.getenv('idk_hide')
client.run(id_key)
