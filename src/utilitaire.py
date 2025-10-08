import asyncio

import discord
from discord.ext import commands
import pyautogui

async def clique(touche: str):
    """
    Permet de cliquer sur une touche pendant 0.3 secondes et ainsi d'être détécté par minecraft

    Args:
        touche(str) : touche sur laquelle il faut cliquer
    """
    pyautogui.keyDown(touche)
    # Attendre assez longtemps pour que minecraft le détècte
    await asyncio.sleep(0.3)
    pyautogui.keyUp(touche)