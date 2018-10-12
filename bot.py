# TheKai bot by TheFire_

import discord
import random
import asyncio
import os

from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions

TheKai = discord.Client()
bot_prefix= "/"
TheKai = commands.Bot(command_prefix=bot_prefix)
TheKai.remove_command("help")

players = {}

@TheKai.event
async def on_ready():
    print ("Im ready my lord")
    print ("I am is " + TheKai.user.name)
    print ("My ID is: " + TheKai.user.id)
    await TheKai.change_presence(game=discord.Game(name="/help "))

@TheKai.command(pass_context=True)
async def ping(ctx):
    await TheKai.say(":ping_pong: pong!!")

@TheKai.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="here's what i could find of this user", color=0xff193b)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Real name: ", value=user.name, inline=True)
    embed.add_field(name="ID: ", value=user.id, inline=True)
    embed.add_field(name="Status: ", value=user.status, inline=True)
    embed.add_field(name="Highest role: ", value=user.top_role, inline=True)
    embed.add_field(name="Joined: ", value=user.joined_at, inline=True)
    embed.add_field(name="Game: ", value=user.game, inline=True)
    await TheKai.say(embed=embed)

@TheKai.command(name="kick", pass_context=True)
@has_permissions(manage_roles=True, kick_members=True)
async def _kick(ctx, *, user: discord.Member):
    await TheKai.say(":cop: Bye bye {}. Return to brush the dolls :grinning:".format(user.name))
    await TheKai.kick(user)

@_kick.error
async def _kick_error(ctx, error):
    await TheKai.say("You not have the permissions or member is invalid")

@TheKai.command(name="ban", pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def _ban(ctx, user: discord.Member):
    await TheKai.say(":cop: Bye bye {}. Return to fuck the unicorns :heart:".format(user.name))
    await TheKai.ban(user)

@_ban.error
async def _ban_error(ctx, error):
    await TheKai.say("You not have the permissions or member is invalid")

@TheKai.command(pass_context=True)
@has_permissions(manage_roles=True, manage_messages=True)
async def clear(ctx, amount=100000):
    channel = ctx.message.channel
    messages = []
    async for message in TheKai.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await TheKai.delete_messages(messages)
    await TheKai.say(":no_entry_sign: Messages has been deleted :no_entry_sign:")

@clear.error
async def clear_error(ctx, error):
    await TheKai.say("You not have the permissions")

@TheKai.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name="List of commands:")
    embed.add_field(name="ping", value="Returns Pong!", inline=False)
    embed.add_field(name="info <user>", value="Return user info", inline=False)
    embed.add_field(name="kick <user>", value="Kick the user", inline=False)
    embed.add_field(name="ban <user>", value="Ban the user", inline=False)
    embed.add_field(name="mute <user>", value="Mute the user", inline=False)
    embed.add_field(name="clear <amount>", value="Clear amount chat messages", inline=False)
    embed.add_field(name="jesus", value="Random meme jesus pic", inline=False)
    embed.add_field(name="anime", value="Random meme anime pic", inline=False)
    embed.add_field(name="baka <user>", value="Random baka pic", inline=False)
    await TheKai.send_message(author, embed=embed)

@TheKai.command(pass_context=True)
async def jesus(ctx):
        messages = ["jesus/1.jpg", "jesus/2.jpg", "jesus/3.jpg", "jesus/4.jpg", "jesus/5.jpg", "jesus/6.jpg", "jesus/7.jpg", "jesus/8.png", "jesus/9.jpg", "jesus/10.jpg"]
        await TheKai.send_file(ctx.message.channel, random.choice(messages))

@TheKai.command(pass_context=True)
async def anime(ctx):
        messages = ["anime/1.jpg", "anime/2.jpg", "anime/3.jpg", "anime/4.jpg", "anime/5.jpg", "anime/6.jpg", "anime/7.jpg", "anime/8.jpg", "anime/9.gif", "anime/10.jpg"]
        await TheKai.send_file(ctx.message.channel, random.choice(messages))

@TheKai.command(name="mute", pass_context=True)
@has_permissions(manage_roles=True)
async def mute(ctx, *, member : discord.Member = None):
    if member is None:
        await TheKai.say("Please pass in a valid user")
        return
    role = discord.utils.get(member.server.roles, name="mute")
    if role is None:
        await TheKai.say("Please create a new role with name mute")
        return
    await TheKai.add_roles(member, role)
    await TheKai.say(f"{str(member)} was muted!")

@mute.error
async def mute_error(ctx, error):
    await TheKai.say("You not have the permissions or member is invalid")

@TheKai.command(pass_context=True)
async def baka (ctx, user : discord.Member = None):
    if user is None:
        await TheKai.say("Please pass in a valid user")
        return
    embed = discord.Embed(title="{} you are a baka. ".format(user.name), description="", color=0xff193b)
    messages = ["https://i.imgur.com/H96mgtS.gif", "https://i.imgur.com/wQViGVn.gif", "https://i.imgur.com/3Lo5feQ.gif", "https://i.imgur.com/R4LkdM1.gif", "https://i.imgur.com/B9NzPhw.gif", "https://i.imgur.com/wheGx8r.gif", "https://i.imgur.com/HYxTTbK.gif"]
    embed.set_image(url=random.choice(messages))
    await TheKai.say(embed=embed)

@baka.error
async def baka_error(ctx, error):
    await TheKai.say("Please pass in a valid user")

TheKai.run("NDk3NDc0MTQ4NTk1OTI0OTkz.Dpfz4Q.uqleiVLjdGcjh-v3MkNziKbc8Vc")
