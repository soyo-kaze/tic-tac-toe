import discord
from discord.ext import commands
import cipher

client = commands.Bot(command_prefix = '$')

# security------------------
f = open("token.txt", "r")
t = f.read()
f.close()
#---------------------------
t = cipher.dec(t) 

@client.event
async def on_ready():
    # await send("swagat ni karoge hamara!!")
    print("UP AND RUNNING")

#____________________ Tic Tac Toe ________________________

played = []
xColumn = []
xRow= []
oColumn= []
oRow= []
xcheck = []
ocheck = []

theBoard = {"t-l":".","t-m":".","t-r":".",
            "m-l":".","m-m":".","m-r":".",
            "b-l":".","b-m":".","b-r":".",}

theCheck = {"t-l":[1,1],"t-m":[1,2],"t-r":[1,3],
            "m-l":[2,1],"m-m":[2,2],"m-r":[2,3],
            "b-l":[3,1],"b-m":[3,2],"b-r":[3,3],}
play = True
Turn = ":x:"

def ticBoard (board):
    """print(board["t-l"]+"|"+board["t-m"]+"|"+board["t-r"])
    print("-+-+-")
    print(board["m-l"]+"|"+board["m-m"]+"|"+board["m-r"])
    print("-+-+-")
    print(board["b-l"]+"|"+board["b-m"]+"|"+board["b-r"])"""
    
    return(board["t-l"]+"|"+board["t-m"]+"|"+board["t-r"]+"\n"
          +"---+---+---"+"\n"+board["m-l"]+"|"+board["m-m"]+"|"
          +board["m-r"]+"\n"+"---+---+---"+"\n"+board["b-l"]+"|"
          +board["b-m"]+"|"+board["b-r"])

@client.command()
async def tac(ctx):
    global play,xColumn,xRow,oColumn,oRow,theBoard,Turn,played,theCheck,ocheck,xcheck
    if play:
        played = []
        xColumn = []
        xRow= []
        oColumn= []
        oRow= []
        ocheck = []
        xcheck = []
        theBoard = {"t-l":".\t","t-m":"\t","t-r":" ",
                    "m-l":".\t","m-m":"\t","m-r":" ",
                    "b-l":".\t","b-m":"\t","b-r":" ",}
        Turn = ":x:"
        await ctx.send("Welcome to Tic-Tac-Toe")
        await ctx.send(ticBoard(theBoard))
        await ctx.send("Player '{}'. Move where?".format(Turn))
        play = False
    else:
        await ctx.send("Game is ongoing can't start. Use $resettic to reset")

@client.command()
async def toe(ctx,*mes):
    move = mes[0]
    global play,xColumn,xRow,oColumn,oRow,theBoard,Turn,played,theCheck
    if not play:
        if (move not in theBoard.keys()):
            await ctx.send("Please type it correctly!!")
        else:
            if move in played:
                await ctx.send("Already occupied!!")
            else:
                theBoard[move] = Turn
                played.append(move)
                if Turn == ":x:":
                    xColumn.append(theCheck[move][1])
                    xRow.append(theCheck[move][0])
                    xcheck.append(theCheck[move])
                    if (                                           
                        xColumn.count(theCheck[move][1]) == 3 
                        or xRow.count(theCheck[move][0]) == 3 
                        or ({1,2,3}==set(set(xColumn).intersection(xRow)).intersection([1,2,3])and 
                            ([2,2] in xcheck and [3,3] in xcheck and [1,1] in xcheck))
                    ):
                        #used set and intersection
                        await ctx.send("Player :x: Wins!!")
                        play = True
                    Turn = ":o:"
                else:
                    oColumn.append(theCheck[move][1])
                    oRow.append(theCheck[move][0])
                    ocheck.append(theCheck[move])
                    if (
                        oColumn.count(theCheck[move][1]) == 3 
                        or oRow.count(theCheck[move][0]) == 3 
                        or ({1,2,3}==set(set(oColumn).intersection(oRow)).intersection([1,2,3])and 
                            ([2,2] in ocheck and [3,3] in ocheck and [1,1] in ocheck))
                    ):
                        #used set and intersection
                        await ctx.send("Player :o: Wins!!")
                        play = True
                    Turn = ":x:"
                    
        await ctx.send(ticBoard(theBoard))
        if not play:
            if len(xRow + oRow) == 9:
                await ctx.send("It's a Tie!! nice")
                play = True
            else:        
                await ctx.send("Player '{}'. Move where?".format(Turn))
                
    else:
        await ctx.send("Game is not initiated use *$tic* to initialize your tic tac toe board")

@client.command()
async def resettic(ctx):
    global play,xColumn,xRow,oColumn,oRow,theBoard,Turn,played,theCheck,xcheck,ocheck
    played = []
    xColumn = []
    xRow= []
    oColumn= []
    oRow= []
    ocheck = []
    xcheck = []
    theBoard = {"t-l":" ","t-m":" ","t-r":" ",
                "m-l":" ","m-m":" ","m-r":" ",
                "b-l":" ","b-m":" ","b-r":" ",}
    Turn = ":x:"
    play = True
    await ctx.send("Game Reset")
@client.command()
async def tachelp(ctx):
    await ctx.send("""use $toe and then define the place u wanna play on
t: top, b: bottom, m: mid, l:left, r: right
place syntax: t/b/m-l/r/m""")
#_______________________end_______________________________

@client.command()
async def greet(ctx):
    await ctx.send("hello")

client.run(t)
