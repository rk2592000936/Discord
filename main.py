import discord
from discord.ext import commands

bot = commands.Bot()

@bot.event
async def on_ready():
    print('Bot has been online')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(687239571007864832)
    await channel.send('{}join!'.format(member))

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(687239628205588509)
    await channel.send('{}leave!'.format(member))

# 'ping'就是用于控制bot回复的指令名称，可使用任意名称
#ctx包含了使用者，id，所在服务器，所在频道等信息，用于提示bot在哪里进行回复
@bot.command()
async def ping(ctx):
    await ctx.send('hello')
