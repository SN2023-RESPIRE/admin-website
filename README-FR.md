# admin-website

## Mise en place

1. Clonez ce dépôt
2. Créez un environnement virtuel Python (venv) (optionnel)
3. Installez les packages depuis `requirements.txt`
4. Créez un fichier .env
5. Créez une entrée `SECRET_KEY` dans le fichier .env avec une clé secrète valide pour le site.
6. Lancez

### Notes supplémentaires

- La clé secrète peut être générée via n'importe quelle méthode. La méthode utilisée durant le développement du projet est la suivante :
```python
import os
print(os.urandom(16).hex())  # Copiez la sortie
```
- Par défaut il n'y a pas d'utilisateurs sur le site. Vous devrez en créer un en lançant le script `register_user.py` depuis un terminal.
