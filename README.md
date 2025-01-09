# Daft Punk Album Store

Application Django permettant de gérer et afficher les albums de Daft Punk.

## Fonctionnalités
- Liste des albums avec leurs informations (titre, description, prix, date de sortie, pochette).
- Page de détails pour chaque album.

## Installation
1. Clonez le projet :
   ```bash
   git clone <URL_DU_REPOSITORY>
   cd daft_store
   ```
2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Configurez la base de données :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

## Utilisation
- Accédez à [http://127.0.0.1:8000/albums/](http://127.0.0.1:8000/albums/) pour voir la liste des albums.
- Cliquez sur un album pour afficher ses détails.
