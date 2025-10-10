import asyncio
import os

import discord
from discord.ext import commands
import pyautogui

def load_env():
    """
    Charge les variables d'environnement depuis le fichier .env
    """
    with open(".env") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

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
