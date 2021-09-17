import discord #Importing the discord.py module

bot = commands.Bot(command_prefix="Your prefix") #Creating a bot variable and configure a prefix

@bot.command() #Creating a command
async def test(ctx): #Set the name of the command
  await ctx.send("The bot is working !") #Set instructions when the command is used ("here sends "The bot is working")

bot.run("Your token") #Run the bot with the token
