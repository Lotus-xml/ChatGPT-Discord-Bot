import sys
import time
import asyncio
import os
import discord
import poe
from discord.ext import commands

poe.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
uwu = poe.Client("poe token here")

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

def giantcock():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")

@bot.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pinging! Please Wait!")
    ping = (time.monotonic() - before) * 1000
    await asyncio.sleep(0.1)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⌛ Bot Ping: {int(ping)}ms ⏳")
    await asyncio.sleep(2.5)
    await message.edit(content=f"⏳ Bot Ping: {int(ping)}ms ⌛")

@bot.event
async def on_ready():
    Servers = len(bot.guilds)
    await bot.change_presence(activity=discord.Game(name="With ChatGPT"))
    giantcock()
    print(f"""
           _____ _           _    _____ _____ _______ 
          / ____| |         | |  / ____|  __ \__   __|
         | |    | |__   __ _| |_| |  __| |__) | | |   
         | |    | '_ \ / _` | __| | |_ |  ___/  | |   
         | |____| | | | (_| | |_| |__| | |      | |   
          \_____|_| |_|\__,_|\__|\_____|_|      |_|   \n
        Made By: Lotus
        I used Poe-API: https://github.com/ading2210/poe-api\n
        User:    {bot.user.name}#{bot.user.discriminator}
        ID:      {bot.user.id}
        Guilds:  {Servers}\n
        Commands:\n
        !chat            - Sends specified message to ChatGPT
        !clear           - Clears the console
        !clear_context   - Clears the context of the chat
        !delete_messages - Deletes specified amount of messages from the Poe chat
        !help            - Shows commands
        !ping            - Shows bot latency
        """.format(bot.command_prefix))


@bot.command()
async def clear(ctx):
    Servers = len(bot.guilds)
    giantcock()
    print(f"""
           _____ _           _    _____ _____ _______ 
          / ____| |         | |  / ____|  __ \__   __|
         | |    | |__   __ _| |_| |  __| |__) | | |   
         | |    | '_ \ / _` | __| | |_ |  ___/  | |   
         | |____| | | | (_| | |_| |__| | |      | |   
          \_____|_| |_|\__,_|\__|\_____|_|      |_|   \n
        Made By: Lotus
        I used Poe-API: https://github.com/ading2210/poe-api\n
        User:    {bot.user.name}#{bot.user.discriminator}
        ID:      {bot.user.id}
        Guilds:  {Servers}\n
        Commands:\n
        !chat            - Sends specified message to ChatGPT
        !clear           - Clears the console
        !clear_context   - Clears the context of the chat
        !delete_messages - Deletes specified amount of messages from the Poe chat
        !help            - Shows commands
        !ping            - Shows bot latency
        """.format(bot.command_prefix))
    await ctx.send('Console cleared!')

@bot.command()
async def clear_context(ctx):
    uwu.send_chat_break("chinchilla")
    await ctx.send('Context cleared!')

@bot.command()
async def delete_messages(ctx, mcount):
    if mcount.lower() == "all":
        uwu.purge_conversation("chinchilla")
        await ctx.send('All messages deleted!')
    else:
        mcount = int(mcount)
        uwu.purge_conversation("chinchilla", mcount)
        await ctx.send(f'{mcount} message(s) deleted!')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", color=0xff0000, description="Commands:")
    embed.add_field(name="!chat", value="Sends specified message to ChatGPT", inline=False)
    embed.add_field(name="!clear", value="Clears the console", inline=False)
    embed.add_field(name="!clear_context", value="Clears the context of the chat", inline=False)
    embed.add_field(name="!delete_messages", value="Deletes specified amount of messages from the Poe chat", inline=False)
    embed.add_field(name="!help", value="Prints this help message", inline=False)
    embed.add_field(name="!ping", value="Gets bot latency", inline=False)
    embed.set_footer(text="Made By: Lotus")
    await ctx.send(embed=embed)

@bot.command()
async def chat(ctx, *, message):
    try:
        response = ''
        for chunk in uwu.send_message("chinchilla", message, timeout=15):
            response += chunk["text_new"]
        await ctx.send(f"```{response}```")
    except Exception as e:
        await ctx.send(f"Error: {e}")

bot.run('discord token here')
