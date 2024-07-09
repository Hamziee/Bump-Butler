# Initialize dot env
import os
from dotenv import load_dotenv
load_dotenv()

# Define the dot env vars
token = os.getenv('token')
ownerID = os.getenv('ownerID')
startMessage = os.getenv('startMessage')

# Import Deps
import selfcord
import asyncio

bot = selfcord.Bot(prefixes=["$#$"])

@bot.on("ready")
async def ready(time):
    print(f"Connected To {bot.user} \nStartup took {time:0.2f} seconds")

async def bump_task(ctx):
    await ctx.channel.send("ok")
    cmd = await ctx.channel.get_slash_commands(name="bump")
    while True:
        print(cmd)
        await ctx.channel.trigger_slash(cmd)
        print(f"[!] Bumped Guild: {ctx.guild.id}")
        await asyncio.sleep(7215) #2 hours: 7200 (added 15 seconds for correction)

@bot.on("message")
async def stuff(message):
    if message.author.id == ownerID:
        if message.content == startMessage:
            asyncio.create_task(bump_task(message))

bot.run(token)