import pandas as pd
import datetime

from pyparsing import Regex

db_path = 'I:\\Documentos\\Programacao\\Repos\\GitHub\\BotF1discord\\databases\\'

df = pd.read_excel(db_path+"main_database.xlsx",sheet_name="db_structuredDatas")

dfDrivers = pd.read_excel(db_path+"main_database.xlsx",sheet_name="db_drivers",index_col=0)

dfSummary = pd.read_excel(db_path+"main_database.xlsx",sheet_name="summary_race_info")


#Retorna um valor baseado no id (gpBahrein neste caso)
x = df.query('command=="gpBahrein"')['gpName']