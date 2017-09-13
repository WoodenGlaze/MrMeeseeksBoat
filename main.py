import discord
import asyncio
import random as r

from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix=commands.when_mentioned_or('css)', 'csgo)', 'cs'), description=description)

@bot.event
async def on_ready():
	print('Logged in as: {0.name} (ID:{0.id})'.format(bot.user))

@bot.event
async def on_resumed():
	print('Connection resumed.')


@bot.event
async def on_member_joined(member):
	server = member.server
	roll = r.randrange(1, 10)
	print(roll)
	await bot.say(server, "Rolled {}".format(roll))

@bot.command(pass_context=True, hidden=True)
async def find_roles():
	server = ctx.message.server
	roles = server.roles
	print(roles)


bot.run("")