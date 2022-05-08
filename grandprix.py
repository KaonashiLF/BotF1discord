import discord
from discord.ext import commands
from decouple import config


grandPrix_list = ["!gpBahrein", "!gpArábiaSaudita", "!gpAustrália", "!gpEmíliaRomanha", "!gpMiami", "!gpEspanha", "!gpMônaco", "!gpAzerbaijão", "!gpCanadá", "!gpInglaterra", "!gpÁustria", "!gpFrança", "!gpHungria", "!gpBélgica", "!gpHolanda", "!gpItália", "!gpSingapura", "!gpJapão", "!gpEUA", "!gpMéxico", "!gpSãoPaulo", "!gpAbuDhabi"]

allcommandsGP = """
**!gpBahrein: **Grande Prêmio do Bahrein

**!gpArábiaSaudita: **Grande Prêmio da Arábia Saudita

**!gpAustrália: **Grande Prêmio da Austrália

**!gpEmíliaRomanha: **Grande Prêmio da Emília-Romanha

**!gpMiami: **Grande Prêmio de Miami

**!gpEspanha: **Grande Prêmio da Espanha

**!gpMônaco: **Grande Prêmio de Mônaco

**!gpAzerbaijão: **Grande Prêmio do Azerbaijão

**!gpCanadá: **Grande Prêmio do Canadá

**!gpInglaterra: **Grande Prêmio da Inglaterra

**!gpÁustria: **Grande Prêmio da Áustria

**!gpFrança: **Grande Prêmio da França

**!gpHungria: **Grande Prêmio da Hungria

**!gpBélgica: **Grande Prêmio da Bélgica

**!gpHolanda: **Grande Prêmio da Holanda

**!gpItália: **Grande Prêmio da Itália

**!gpSingapura: **Grande Prêmio de Singapura

**!gpJapão: **Grande Prêmio do Japão

**!gpEUA: **Grande Prêmio dos EUA

**!gpMéxico: **Grande Prêmio do México

**!gpSãoPaulo: **Grande Prêmio de São Paulo

**!gpAbuDhabi: **Grande Prêmio de Abu Dhabi


"""

robot = commands.Bot("!")

class consultGrandPrix:

    @robot.command("gpBahrein")
    async def requestGPinfo(ctx):
        name = ctx.author.name

        response = ""