# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:57:37 2022

@author: Kevin
"""

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    #await client.change_presence(status = discord.Status.online, activity = discord.Game('Plotting his revenge'))
    print('Bot is online')

@client.command(aliases = ['wheresmatt', 'Wheresmatt', 'WhereIsMatt', 'whereismatt'], brief = 'Tells user where Matt Crump is')
async def WheresMatt(ctx):
    myid = '<@160482712807931904>'
    await ctx.send('*BANG*')
    await ctx.send(myid + " is on the couch")

@client.command(aliases = ['shootmason', 'Shootmason', 'shootMason'], brief = 'Shoots Mason')
async def ShootMason(ctx):
    myid = '<@295250323893780481>'
    await ctx.send('*BANG*')
    await ctx.send(myid + " has died")
    
client.run('secrets.TOKEN')
