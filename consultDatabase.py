
import pandas as pd
import datetime

db_path = 'databases\\'

df = pd.read_excel("main_database.xlsx",sheet_name="db_structuredDatas")


#Classe de consulta das informações das corridas
class consultGP:

    #Função para retornar o nome do Grande Prêmio
    def consultGPname(cod):
        cod = str(cod)
        n = df.loc[df['command'] == cod, 'gpName',].to_string()
        return n

    #Função para retornar a data do Grande Prêmio
    def consultGPdate(cod):
        cod = str(cod)
        n = df.loc[df['command'] == cod, 'date_race',].to_string()
        return n

    #Função para retornar a hora do Grande Prêmio
    def consultGPtime(cod):
        cod = str(cod)
        n = df.loc[df['command'] == cod, 'startTime_race',].to_string()
        return n