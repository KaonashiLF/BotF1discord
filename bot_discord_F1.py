import discord
from discord.ext import commands
from decouple import config
import grandprix as gp
import consultDatabase as cdb


mainRoomID = 586582112388382731

robot = commands.Bot("!")


#Este é um evento que indica que o bot está pronto para ser executado
@robot.event 
async def on_ready():
    startMessage = 'Lights out and away we go!\n\nPara consultar todos os comandos, digite "**!comandos**"'

    channel = robot.get_channel(mainRoomID)

    await channel.send(startMessage)


@robot.event
async def on_message(msg):
    channel = robot.get_channel(586582112388382731)

    if msg.author == robot.user:
        return

    if msg.content.startswith("!"):
        listaGP = ["gpBahrein", "gpArábiaSaudita", "gpAustrália", "gpEmíliaRomanha", "gpMiami", "gpEspanha", "gpMônaco", "gpAzerbaijão", "gpCanadá", "gpInglaterra", "gpÁustria", "gpFrança", "gpHungria", "gpBélgica", "gpHolanda", "gpItália", "gpSingapura", "gpJapão", "gpEUA", "gpMéxico", "gpSãoPaulo", "gpAbuDhabi"]
        
        msgcontent = msg.content

        if msg.content[1:] in listaGP:
            msgg = msg.content
            gpName = cdb.consultGP.consultGPname(msgg[1:])
            gpDate = cdb.consultGP.consultGPdate(msgg[1:])
            gpTime = cdb.consultGP.consultGPtime(msgg[1:])
            channel = robot.get_channel(586582112388382731)
            link = r"https://www.band.uol.com.br/esportes/automobilismo/formula-1/ao-vivo"

            response = f"***{gpName[5:]}***\n**Data:** {gpDate[5:]}\n**Horário (Brasília):** {gpTime[5:]}\n**Link: **{link}"

            await channel.send(response)



        elif msg.content[1:] == "comandos":
            username = msg.author.name
            channel = robot.get_channel(mainRoomID)

            with open(gp.pathCommands+"allCommands.txt",encoding="utf-8") as x:
                allCommands = x.read()

            comandos = f"Olá, {username}. Estes são os comandos:\n"+allCommands

            await channel.send(comandos)



        elif msg.content[1:] == "listagp":
            username = msg.author.name
            channel = robot.get_channel(mainRoomID)
            allcommandsGP = gp.allcommandsGP

            response = f"{username}, para consultar informações dos grandes prêmios, digite:\n"+str(allcommandsGP)

            await channel.send(response)



        elif msg.content[1:] == "link":
            link = r"https://www.band.uol.com.br/esportes/automobilismo/formula-1/ao-vivo"
            response = "Band Fórmula 1 - Link: "+link

            channel = robot.get_channel(mainRoomID)

            await channel.send(response)

    else:
        return



TOKEN_DD = config("PRIVATETOKEN")
robot.run(TOKEN_DD)