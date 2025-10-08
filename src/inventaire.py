import asyncio

import discord
from discord.ext import commands
import pyautogui

from bot import bot
from utilitaire import clique

@bot.command()
async def inv(ctx):
    """
    Commande pour ouvrir l'inventaire
    """
    await clique("e")
    await ctx.send("E cliqué")
    print("E cliqué")
    
