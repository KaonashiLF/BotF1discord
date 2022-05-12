#Retorna a lista de comandos de todos as corridas
pathCommands = r"I:\Documentos\Programacao\Repos\GitHub\BotF1discord\commands\\"

with open(pathCommands+"commandsGP.txt",encoding="utf-8") as x:
    allcommandsGP = x.read()