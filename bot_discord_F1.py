import discord
from discord.ext import commands
from decouple import config
import grandprix as gp


mainRoomID = 586582112388382731

#Esta variável armazena a função Bot que é o prefixo para chamar algum comando
robot = commands.Bot("!")

#channel = robot.get_channel(mainRoomID)

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

    comandos = f"Olá, {username}. Estes são os comandos:\n**!proximogp:** Comando que retorna informações sobre o próximo Grand Prix da Fórmula 1\n**!listagp:** Retorna a lista de todos os grande prêmios, trazendo informações de cada um deles."

    await channel.send(comandos)



@robot.command(name="listagp")
async def consultaGPs(ctx):
    username = ctx.author.name
    channel = robot.get_channel(mainRoomID)
    allcommandsGP = gp.allcommandsGP

    gpl = gp.grandPrix_list

    response = f"{username}, para consultar informações dos grandes prêmios, digite:\n"+allcommandsGP

    await channel.send(response)



@robot.command(name="proximogp")
async def grandPrix(ctx):
    username = ctx.author.name
    channel = robot.get_channel(mainRoomID)

    #channel = robot.get_channel(mainRoomID)

    response = "O próximo Grande Prêmio será:\n***Grande Prêmio de Miami***\n**Data:** 08/05/2022\n**Horário (Brasília):** 16h30\n**Pole position:** Charles Leclerc"
    try:
        await channel.send(response)
    except Exception as e:
        print(e)


TOKEN_DD = config("PRIVATETOKEN")
robot.run(TOKEN_DD)