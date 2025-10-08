# Bot Discord Minecraft

Ce projet est un bot Discord utilisant Python qui permet de jouer à un jeu minecraft lancé sur le PC où est lancé le bot en utilisant des commandes sur discord.

## Configuration

- Cloner le dépot :
  ```bash
  git clone https://github.com/Nathan-44/Bot-Minecraft.git


- Se déplacer dans le bon dossier :
  ```bash
  cd Bot-Minecraft

- Créer l'environnement de développement virtuel
  ```bash
  python -m venv venv

- Window :
  ```bash
  venv\Scripts\activate
- Linux/Mac :
  ```bash
  source venv/bin/activate

- Intsaller les dépendances :
  ```bash
  pip install -r requirements.txt

-  Créer fichier `.env`

- Ajouter DISCORD_TOKEN="Votre_Token"

- Démarrer le programme
  ```bash
  python src/main.py

- Dans Minecraft
    - Touches : 
        z: avancer
        s: reculer
        r: courir
        shift: s'accroupir

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
