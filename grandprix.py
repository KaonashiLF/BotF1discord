from discord.ext import commands
from decouple import config
from bot_discord_F1 import robot

#from robot import robot

pathCommands = "I:\\Documentos\\Programacao\\Repos\\GitHub\\BotF1discord\\commands\\"


with open(pathCommands+"commandsGP.txt",encoding="utf-8") as x:
    allcommandsGP = x.read()

@robot.command(name="gpBahrein")
async def gpBahrein(ctx):
    username = ctx.author.name
    channel = robot.get_channel(586582112388382731)
    gpName = ""
    gpDate = ""
    gpTime = ""
    gpPolePosition = ""
    gpWinner ="" #Se a data do GP for menor do que a data atual, igualmente para hora, ele deverá mostrar o vencedor
    response = "***Grande Prêmio do Bahrein***\n**Data:** 08/05/2022\n**Horário (Brasília):** 16h30\n**Pole position:** N/A"

    await channel.send(response)