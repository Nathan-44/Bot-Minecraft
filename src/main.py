"""
Module de lancement du bot
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
