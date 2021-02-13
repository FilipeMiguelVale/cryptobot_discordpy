import discord
from discord.ext import commands
from secret import secret as token
#from logger import logger

#create roles file for auto roler

bot = commands.Bot(command_prefix='$')  # set the command prefix to !

bot.load_extension('watchdog')

#Logger configs

@bot.event
async def on_ready():

	print('We are online')

# EXCEPTIONS HANDLER
@bot.event
async def on_command_error(ctx, error):
	caught_error = False
	if isinstance(error, commands.CommandOnCooldown):
		description = f"You can only use this command again in {format_seconds(error.retry_after)}!"
		caught_error = True

	elif isinstance(error, commands.CommandNotFound):
		description = "The command doesn't exist! Please type !help to see all the existing commands."
		caught_error = True

	if caught_error:
		embed = discord.Embed(
				title="Something went wrong...",
				description=description,
				colour= 0xd60000
			)
		await ctx.send(embed=embed)

	raise error  # re-raise the error so all the errors will still show up in console


################################################################################ ROLES

def format_seconds(sec):
	s = int(sec%60)
	m = int(sec/60)%60
	h = int(sec/3600)
	return f"{h} hours {m} minutes {s} seconds"


bot.run(token)