import asyncio

import discord
from discord.ext import commands
import pyautogui

from bot import bot
from utilitaire import clique

# Variables globales
avancer_en_cours = False
reculer_en_cours = False
minage_en_cours = False
DEGRES_PAR_PIXEL = 0.1


def stop(ctx):
    """
    Fonction qui arrête complètement tout déplacements.

    Args:
        - None
    
    Returns:
        - None
    """

    global avancer_en_cours
    global reculer_en_cours

    # Relève les deux touches de déplacement
    pyautogui.keyUp("z")
    pyautogui.keyUp("s")

    reculer_en_cours = False
    avancer_en_cours = False

    ctx.send("Le mouvement est arrêté.")
    print("Touches 'z' est 's' relevées.")


@bot.command()
async def av(ctx):
    """
    Commande pour avancer.

    Args
    """
    global avancer_en_cours
    global reculer_en_cours

    # Si on recule, on s'arrete
    if reculer_en_cours:
        stop(ctx)
    
    # Si on avance pas, on se met à avancer
    if not avancer_en_cours:
        pyautogui.keyDown("z")
        await ctx.send("Le joueur avance")
        print("Avancer")
        avancer_en_cours = True

@bot.command()
async def re(ctx):
    """
    Commande pour reculer
    """
    global reculer_en_cours
    global avancer_en_cours

    # Si on avnace, on s'arrete
    if avancer_en_cours:
        stop(ctx)

    # Si on ne recule pas, on se met à reculer
    if not reculer_en_cours:
        pyautogui.keyDown("s")
        await ctx.send("Le joueur recule")
        print("Reculer")
        reculer_en_cours = True

@bot.command()
async def st(ctx):
    """
    Commande pour s'arreter
    """
    stop(ctx)
    await ctx.send("Le joueur s'arret")
    print("Arret")

@bot.command()
async def sa(ctx):
    """
    Commande pour sauter
    """
    await clique("space")
    await ctx.send("Le joueur saute")
    print("Saut")

@bot.command()
async def sh(ctx):
    """
    Commande pour se mettre en shift (s'accroupir)
    """
    await clique("shift")
    await ctx.send("Le joueur basule la touche shift")
    print("Shift basculé")


@bot.command()
async def co(ctx):
    """
    Commande pour courir
    """
    await clique("r")
    await ctx.send("Baculement de la course")
    print("R basculer")

@bot.command()
async def ta(ctx):
    """
    Commande pour frapper
    """
    global minage_en_cours
    
    pyautogui.leftClick()
    # Pour ne pas entrer en conflit avec le minage
    minage_en_cours = False
    await ctx.send("Clique gauche de souris.")
    print("Click gauche.")

@bot.command()
async def cr(ctx):
    """
    Commande pour donner un coup critique (jump + hit).

    Args:
        - None

    Returns:
        - None
    """
    global minage_en_cours

    await clique("space")
    pyautogui.leftClick()
    # Pour ne pas entrer en conflit avec le minage
    minage_en_cours = False
    await ctx.send("Coup critique effectué")
    print("Coup critique effectué")

@bot.command()
async def s(ctx, x: float, y: float):
    """
    Commande pour bouger la souris en fonction d'une valeur arbitraire.

    Args:
        - x (float): Le nombre pour l'abscisse.
        - y (float): Le nombre pour l'ordonnée.
    Returns:
        - None

    HELP:
        - 5 ~= Une case de l'inventaire
    """

    # Conversion des degrés en pixels
    pixels_x = x / DEGRES_PAR_PIXEL
    pixels_y = y / DEGRES_PAR_PIXEL

    # Déplacer la souris de manière relative
    pyautogui.moveRel(pixels_x, pixels_y)
    
    await ctx.send(f"La souris a bougé de {pixels_x} pixels en X et {pixels_y} pixels en Y.")
    print(f"La souris a bougé de {pixels_x} pixels en X et {pixels_y} pixels en Y.")

@bot.command()
async def sx(ctx, x: float):
    """
    Commande pour bouger la souris horizontalement en fonction d'un nombre.
    """

    # Conversion en pixels
    pixels_x = x / DEGRES_PAR_PIXEL

    # Déplacer la souris de manière relative
    pyautogui.moveRel(pixels_x, 0)
    
    await ctx.send(f"La souris a bougé de {pixels_x} pixels en X.")
    print(f"La souris a bougé de {pixels_x} pixels en X.")

@bot.command()
async def sy(ctx, y: float):
    """
    Commande pour bouger la souris verticalement en fonction d'un nombre.
    """

    # Conversion en pixels
    pixels_y = y / DEGRES_PAR_PIXEL

    # Déplacer la souris de manière relative
    pyautogui.moveRel(0, pixels_y)
    
    await ctx.send(f"La souris a bougé de {pixels_y} pixels en Y.")
    print(f"La souris a bougé de {pixels_y} pixels en Y.")

@bot.command()
async def min(ctx):
    """
    Commande pour basculer le mode minage     
    """
    global minage_en_cours

    # Si on n'est pas en train de miner, on mine
    if not minage_en_cours:
        minage_en_cours = True
        pyautogui.mouseDown(button="left")
        await ctx.send("Mode minage activé")
        print("Mode minage activé")
    
    # Sinon on s'arrete
    else:
        minage_en_cours = False
        pyautogui.mouseUp(button="left")
        await ctx.send("Mode minage désactivé")
        print("Mode minage désactivé")

@bot.command()
async def cd(ctx):
    """
    Commande pour simuler un clique droit
    """
    pyautogui.rightClick()
    await ctx.send("Clique droit de souris.")
    print("Clique droit.")
    
