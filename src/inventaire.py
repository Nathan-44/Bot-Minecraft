import asyncio
import os

import discord
from discord.ext import commands
import pyautogui

from bot import bot
from utilitaire import clique

# La distance entre chaque case de l'inventaire
DISTANCE_CASE = int(str(os.getenv("DISTANCE_CASE")))

# Coin supérieur gauche de l'inventaire (inventaire)
COIN_1_INV = (int(str(os.getenv("X_INV"))), int(str(os.getenv("Y_INV"))))
# Coin supérieur gauchee de la barre d'inventaire (inventaire)
COIN_2_INV = (int(str(os.getenv("X_INV"))), int(str(os.getenv("Y_INV_HOT"))))

# Coin supérieur gauche de l'inventaire (table de craft)
COIN_1_CRAFT = (int(str(os.getenv("X_CRAFT"))), int(str(os.getenv("Y_CRAFT"))))
# Coin supérieur gauchee de la barre d'inventaire (table de craft)
COIN_2_CRAFT = (int(str(os.getenv("X_CRAFT"))), int(str(os.getenv("Y_CRAFT_HOT"))))

TOUCHES = ["&", "é", "\"", "'", "(", "-", "è", "_", "ç"]

@bot.command()
async def inv(ctx):
    """
    Commande pour ouvrir et fermer l'inventaire
    """
    await clique("e")
    await ctx.send("E cliqué")
    print("E cliqué")

@bot.command()
async def seli(ctx, ligne: int, col: int):
    """
    Commande pour sélectionner une case de l'inventaire (lorsque c'est l'inventaire qui est ouvert)
    
    Args:
        - ligne(int): La ligne de la case (entre 1 et 4)
        - col(int): La colonne de la case (entre 1 et 9)
    """
    # Vérifictaion des arguments
    if ligne < 1 or ligne > 4 or not isinstance(ligne, int):
        await ctx.send("La ligne doit ettre un entier compris entre 1 et 4")
        print("Utilisation invalide(seli)")
        return
    elif col < 1 or col > 9 or not isinstance(col, int):
        await ctx.send("La colonne doit ettre un entier compris entre 1 et 9")
        print("Utilisation invalide(seli)")
        return
    
    # Si c'est l'inventaire principal
    if ligne <= 3:
        # x et y coos du coins supérieur gauche + distance entre deux case * la nombre de la case
        pyautogui.moveTo(COIN_1_INV[0] + (col-1) * DISTANCE_CASE, COIN_1_INV[1] + (ligne-1) * DISTANCE_CASE)
        await ctx.send(f"Case {ligne} {col}")
        print((f"Case {ligne} {col}"))
    # Sinon, si c'est la barre d'inventaire
    else : 
        pyautogui.moveTo(COIN_2_INV[0] + (col-1) * DISTANCE_CASE, COIN_2_INV[1])
        await ctx.send(f"Case {ligne} {col}")
        print((f"Case {ligne} {col}"))

@bot.command()
async def selc(ctx, ligne: int, col: int):
    """
    Commande pour sélectionner une case de l'inventaire (lorsque c'est la table de craft qui est ouverte)
    
    Args:
        - ligne(int): La ligne de la case (entre 1 et 4)
        - col(int): La colonne de la case (entre 1 et 9)
    """
    # Vérifictaion des arguments
    if ligne < 1 or ligne > 4 or not isinstance(ligne, int):
        await ctx.send("La ligne doit ettre un entier compris entre 1 et 4")
        print("Utilisation invalide(selc)")
        return
    elif col < 1 or col > 9 or not isinstance(col, int):
        await ctx.send("La colonne doit ettre un entier compris entre 1 et 9")
        print("Utilisation invalide(selc)")
        return
    
    # Si c'est l'inventaire principal
    if ligne <= 3:
        # x et y coos du coins supérieur gauche + distance entre deux case * la nombre de la case
        pyautogui.moveTo(COIN_1_CRAFT[0] + (col-1) * DISTANCE_CASE, COIN_1_CRAFT[1] + (ligne-1) * DISTANCE_CASE)
        await ctx.send(f"Case {ligne} {col}")
        print((f"Case {ligne} {col}"))
    # Sinon, si c'est la barre d'inventaire
    else : 
        pyautogui.moveTo(COIN_2_CRAFT[0] + (col-1) * DISTANCE_CASE, COIN_2_INV[1])
        await ctx.send(f"Case {ligne} {col}")
        print((f"Case {ligne} {col}"))

@bot.command()
async def hot(ctx, case: int):
    """
    Commande pour sélectionner une case spécifique de la hotbar.
    
    Args:
        - case (int): La case de l'inventaire (1, 9).
    
    Returns:
        - None
    """
    
    if isinstance(case, int) and case > 0 and case <= 9:
        await clique(TOUCHES[case-1])
        await ctx.send(f"Touche {case} cliquée.")
        print(f"Touche {case} cliquée.")
    else:
        await ctx.send("Mauvaise utilisation de la commande 'hot'.\nTapez 'help' pour de l'aide.")
        print("Utilisation invalide ('hot').")