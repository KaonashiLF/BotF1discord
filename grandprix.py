#Retorna a lista de comandos de todos as corridas
pathCommands = "commands\\"

with open(pathCommands+"commandsGP.txt",encoding="utf-8") as x:
    allcommandsGP = x.read()