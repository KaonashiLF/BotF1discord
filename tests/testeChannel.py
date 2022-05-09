from discord.ext import commands
from decouple import config
from channel import channel


mainRoomID = 586582112388382731

robot = commands.Bot("!")



#Este é um evento que indica que o bot está pronto para ser executado
@robot.event 
async def on_ready():
    startMessage = 'Lights out and away we go!\n\nPara consultar todos os comandos, digite "**!comandos**"'

    channel = robot.get_channel(mainRoomID)

    await channel.send(startMessage)

@robot.command(name="link")
async def link(ctx):
    link = r"https://www.band.uol.com.br/esportes/automobilismo/formula-1/ao-vivo"
    response = f"O link é este: {link}"

    await channel().send(response)


TOKEN_DD = config("PRIVATETOKEN")
robot.run(TOKEN_DD)