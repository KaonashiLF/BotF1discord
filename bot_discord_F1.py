import discord
from discord.ext import commands
from decouple import config
import grandPrix as gp


mainRoomID = 586582112388382731

robot = commands.Bot("!")


#Este é um evento que indica que o bot está pronto para ser executado
@robot.event 
async def on_ready():
    startMessage = 'Lights out and away we go!\n\nPara consultar todos os comandos, digite "**!comandos**"'

    channel = robot.get_channel(mainRoomID)

    await channel.send(startMessage)



@robot.command(name="comandos")
async def allCommands(ctx):
    username = ctx.author.name
    channel = robot.get_channel(mainRoomID)

    with open(gp.pathCommands+"allCommands.txt",encoding="utf-8") as x:
        allCommands = x.read()

    comandos = f"Olá, {username}. Estes são os comandos:\n"+allCommands

    await channel.send(comandos)



@robot.command(name="listagp")
async def consultaGPs(ctx):
    username = ctx.author.name
    channel = robot.get_channel(mainRoomID)
    allcommandsGP = gp.allcommandsGP


    response = f"{username}, para consultar informações dos grandes prêmios, digite:\n"+str(allcommandsGP)


    await channel.send(response)



@robot.command(name="proximogp")
async def grandPrix(ctx):
    username = ctx.author.name
    channel = robot.get_channel(mainRoomID)

    #channel = robot.get_channel(mainRoomID)

    response = "O próximo Grande Prêmio será:\n***Grande Prêmio de Miami***\n**Data:** 08/05/2022\n**Horário (Brasília):** 16h30\n**Pole position:** N/A"
    try:
        await channel.send(response)
    except Exception as e:
        print(e)


@robot.command(name="link")
async def link(ctx):
    link = r"https://www.band.uol.com.br/esportes/automobilismo/formula-1/ao-vivo"
    response = "Band Fórmula 1 - Link: "+link

    channel = robot.get_channel(mainRoomID)

    await channel.send(response)


@robot.command(name="gpBahrein")
async def gpBahrein(ctx):
    username = ctx.author.name
    channel = robot.get_channel(586582112388382731)
    gpName = "gpBahrein"
    gpDate = ""
    gpTime = ""
    gpPolePosition = ""
    gpWinner ="" #Se a data do GP for menor do que a data atual, igualmente para hora, ele deverá mostrar o vencedor
    response = "***Grande Prêmio do Bahrein***\n**Data:** 08/05/2022\n**Horário (Brasília):** 16h30\n**Pole position:** N/A"

    await channel.send(response)


TOKEN_DD = config("PRIVATETOKEN")
robot.run(TOKEN_DD)