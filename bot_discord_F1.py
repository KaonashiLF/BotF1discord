import discord
from discord.ext import commands
#from decouple import config
import grandprix as gp
import consultDatabase as cdb


mainRoomID = 586582112388382731

robot = commands.Bot("!")

client = discord.Client()

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


#@robot.command(name="gpBahrein")
@robot.event
async def on_message(msg):
    channel = robot.get_channel(586582112388382731)

    if msg.author == robot.user:
        return

    if msg.content.notstartswith("!"):
        return

    listaGP = ["gpBahrein", "gpArábiaSaudita", "gpAustrália", "gpEmíliaRomanha", "gpMiami", "gpEspanha", "gpMônaco", "gpAzerbaijão", "gpCanadá", "gpInglaterra", "gpÁustria", "gpFrança", "gpHungria", "gpBélgica", "gpHolanda", "gpItália", "gpSingapura", "gpJapão", "gpEUA", "gpMéxico", "gpSãoPaulo", "gpAbuDhabi"]
    if msg.content in listaGP:
        msgg = msg.content
        gpName = cdb.consultGP.consultGPname(msgg)
        gpDate = cdb.consultGP.consultGPdate(msgg)
        gpTime = cdb.consultGP.consultGPtime(msgg)
        channel = robot.get_channel(586582112388382731)
        link = r"https://www.band.uol.com.br/esportes/automobilismo/formula-1/ao-vivo"

        response = f"***{gpName[5:]}***\n**Data:** {gpDate[5:]} (Ano-Mês-Dia)\n**Horário (Brasília):** {gpTime[5:]}\n**Link: **{link}"

        await channel.send(response)
    else:
        await channel.send("mamou")



#TOKEN_DD = config("PRIVATETOKEN")
robot.run("OTY0NjAxNTEwMzA4NzQ5Mzg1.GqvhSD.YEndDsMOkVS8EQb5xOsxr_e5iiPUgMjbPuCMyo")