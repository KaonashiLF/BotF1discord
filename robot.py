from discord.ext import commands
from decouple import config

mainRoomID = 586582112388382731


robot = commands.Bot("!")

PRIVATETOKEN = config("PRIVATETOKEN")

robot.run(PRIVATETOKEN)