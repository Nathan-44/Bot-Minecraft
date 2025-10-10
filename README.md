# Bot Discord Minecraft

Ce projet est un bot Discord utilisant Python qui permet de jouer à un jeu minecraft lancé sur le PC où est lancé le bot en utilisant des commandes sur discord.

## Configuration

### Installer le bot :
- Cloner le dépot : `git clone https://github.com/Nathan-44/Bot-Minecraft.git`
- Se déplacer dans le bon dossier : `cd Bot-Minecraft`

- Créer l'environnement de développement virtuel : `python -m venv venv`
  - Window : `venv\Scripts\activate`
  - Linux/Mac : `source venv/bin/activate`
- Intsaller les dépendances : `pip install -r requirements.txt`

- Créer le fichier `.env`
- Y mettre :
  ```
  DISCORD_TOKEN="Votre token"
  
  DISTANCE_CASE="Distance entre les cases de l'inventaire

  X_INV="Coordonnée x de la premiere case de l'inventaire"
  Y_INV="Coordonnée y de la première case de l'inventaire"
  Y_INV_HOT="Coordonnée y de la première case de la hotbar lorsque l'inventaire est ouvert"

  X_CRAFT="Coordonnée x de la premiere case de l'inventaire lorsque la table de craft est ouverte"
  Y_CRAFT="Coordonnée y de la premiere case de l'inventaire lorsque la table de craft est ouverte"
  Y_CRAFT_HOT="Coordonnée y de la première case de la hotbar lorsque la table de craft est ouverte"
  
- Démarrer le programme : `python src/main.py`

### Dans Minecraft
- Touches : 
  - z: avancer
  - s: reculer
  - r: courir
  - shift: s'accroupir
  - Sensibilité caméra: 100%

- Accroupir : basuler
- Courir : basuler

- Controle -> parametre souris -> entrée brute : Non

- Penser à cliquer sur la fenetre minecraft

## Bibliothèques utilisées

- [discord.py](https://github.com/Rapptz/discord.py) (MIT License)
- [PyAutoGUI](https://github.com/asweigart/pyautogui) (BSD License)

## Avertissements

- Ne jamais inclure de tokens Discord ou de mots de passe dans ce dépôt.
- Utilisez un fichier `.env` ou des variables d'environnement pour les clés sensibles.
- Faire attention en l'utilisant : le bot simule des touches sur le pc où il est lancé.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE.txt` pour plus de détails.
