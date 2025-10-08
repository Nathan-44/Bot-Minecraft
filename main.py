"""
Config :
    -touches : 
        z: avancer
        s: reculer
        r: courir
        shift: s'accroupir
    -accroupir : basuler
    -courir : basuler
    -controle -> parametre souris -> entrée brute : Non

Necessite .env qui contient le token discord
"""

from bot import *

# Initialisation du bot
init_bot()
commandes_basique()

# Importation des commandes principales
from mouvement import *
from inventaire import *

# Démarrer la fonction principale dans bot.py (déployer le bot)
launch()
