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

def stop():
    global avancer_en_cours
    global reculer_en_cours
    pyautogui.keyUp("z")
    pyautogui.keyUp("s")
    reculer_en_cours = False
    avancer_en_cours = False


@bot.command()
async def av(ctx):
    """
    Commande pour avancer
    """
    global avancer_en_cours
    global reculer_en_cours

    if reculer_en_cours:
        stop()
    
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

    if avancer_en_cours:
        stop()

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
    stop()
    await ctx.send("Le joueur s'arret")
    print("Arret")

@bot.command()
async def sa(ctx):
    """
    Commande pour sauter
    """
    # Permet au joueur de sauter
    await clique("space")
    await ctx.send("Le joueur saute")
    print("Saut")

@bot.command()
async def sh(ctx):
    """
    Commande pour se mettre en shift
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
    pyautogui.leftClick()
    await ctx.send("Clique gauche de souris.")
    print("Click gauche.")

@bot.command()
async def cr(ctx):
    """
    Commande pour donner un coup critique (jump + hit)
    """
    await ta(ctx)
    await sa(ctx)

@bot.command()
async def s(ctx, x: float, y: float):
    """
    Commande pour bouger la souris en fonction de l'angle (degrés).
    """
    # Conversion des degrés en pixels
    pixels_x = x / DEGRES_PAR_PIXEL
    pixels_y = y / DEGRES_PAR_PIXEL

    # Déplacer la souris de manière relative
    pyautogui.moveRel(pixels_x, pixels_y)
    
    await ctx.send(f"La souris a bougé de {pixels_x} pixels en X et {pixels_y} pixels en Y, correspondant à {x} degrés horizontalement et {y} degrés verticalement.")
    print(f"La souris a bougé de {pixels_x} pixels en X et {pixels_y} pixels en Y.")

@bot.command()
async def min(ctx, secondes: float):
    """
    Commande pour basculer le mode minage
    """
    global minage_en_cours

    # Si le mode minage est activé, le désactivé, sinon l'activer
    if minage_en_cours:
        minage_en_cours = False
        pyautogui.mouseUp(button="left")
        await ctx.send("Mode minage désactivé")
    
    else:
        minage_en_cours = True
        pyautogui.mouseDown(button="left")
        await ctx.send("Mode minage activé")

@bot.command()
async def ut(ctx):
    """
    Commande pour simuler un clique droit
    """
    pyautogui.rightClick()
    await ctx.send("Clique droit de souris.")
    print("Click droit.")
    
