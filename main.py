import discord

bot = commands.Bot(command_prefix="Your prefix")

@bot.command()
async def test(ctx):
  await ctx.send("The bot is working !")

bot.run("Your token")
