import asyncio
import os

import discord
from discord.ext import commands
import pyautogui
    
TOKEN = str(os.getenv("DISCORD_TOKEN"))

def init_bot():
    """
    Fonction initialisant le bot
    """
    # Création d'un objet Intents avec les paramètres par défaut
    intents = discord.Intents.default()
    # Permet l'accès au contenu des messages
    intents.message_content = True

    # Préfixe des commandes du bot
    global bot
    bot = commands.Bot(intents=intents, command_prefix="!")

    # Quand le bot est prêt
    @bot.event
    async def on_ready():
        print(f'Bot minecraft connecté en tant que {bot.user}')

def commandes_basique():
    """
    Commandes basiques du bot qui n'entrent pas dans les catégorie mouvement ou inventaire
    """
    @bot.command()
    async def position(ctx):
        """
        Donne la position de la souris
        """
        # Envoi de la position de la souris
        await ctx.send(pyautogui.position())
    

def launch():
    """
    Fonction démarrant le bot
    """
    # Lancer le bot
    bot.run(TOKEN)