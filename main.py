import discord, dotenv, os, random
dotenv.load_dotenv()
frankeToken = str(os.getenv("frankeTOKEN"))
testToken = str(os.getenv("testTOKEN"))
bot = discord.Bot()

@bot.slash_command(description="Testing?")
async def poopy(ctx: discord.ApplicationContext, user: discord.User=None):
    user = user or ctx.author
    ctx.send(f'```@{user} is a poopy head!```')

@bot.slash_command(description="Amogus2")
async def amongus(ctx: discord.ApplicationContext, user: discord.User=None):
    print('hi')
    user = user or ctx.author
    await ctx.respond(f'''{user} you wanted this?\n 
⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀
⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆
⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟
⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀
⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀
⠀⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿
''')

@bot.slash_command(description="pfps")
async def pfp2(ctx: discord.ApplicationContext, user: discord.User=None):
    user = user or ctx.author
    await ctx.respond(f'{user.display_avatar.url}')

@bot.command()
async def gtn(ctx):
    await ctx.respond("Guess a number between 1 and 10")
    guess = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
    num = random.randint(1, 10)


    if(guess.content) == num:
        await ctx.send(f'Answer: {num}, you win!')
    else:
        await ctx.send(f'Answer: {num}, you lose!')

print('started')

bot.run(testToken) # ASDFASDF BOT


#bot.run(frankeToken) # FRANKE BOT
