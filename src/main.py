"""
Module de lancement du bot
"""

# Initialisation des variables d'environnement
from utilitaire import load_env
load_env()

from bot import *

# Initialisation du bot
init_bot()
commandes_basique()

# Importation des commandes principales
from mouvement import *
from inventaire import *

# Démarrer la fonction principale dans bot.py (déployer le bot)
launch()
