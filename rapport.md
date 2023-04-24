# EmaFamille

![Logo](https://emafamille.fr/static/Logo_EMAFamille.PNG)

## Membres de l'équipe

- Emile Delmas [@emiledelmas](https://www.github.com/emiledelmas)
- Simon Chalmé [@simonchalme](https://www.github.com/simonchalme)
- Laura Bertieaux [@NapsyGit](https://www.github.com/napsygit)
- Ludovic Terrasson [@Ludooooooooo](https://www.github.com/Ludooooooooo)
- Arthur Rubio [@Hermes075](https://www.github.com/Hermes075)
- Charlotte Houzé [@cha0601](https://www.github.com/cha0601)
- Ilyane Gomis [@IlyaneGomis](https://www.github.com/IlyaneGomis)
- Florian Laporte

## Liens vers le projet et les dépôts GitHub

- [EmaFamille.fr](https://emafamille.fr)
- [Github Repos Front](https://github.com/emiledelmas/EmaFamilleFront)
- [Github Repos Back](https://github.com/emiledelmas/EmaFamille-Back)

## Expression du besoin

## Organisation globale du projet

## Description fonctionnelle du résultat obtenu

## Description de l’architecture technique et applicative du projet avec justification des choix effectués

## Notice d’installation

### Recommandé :

Nous vous conseillons d'utiliser la version de production de EmaFamille afin de la tester. Pour cela, rendez-vous sur [EmaFamille.fr](https://emafamille.fr).

### Installation en local (mode de développement) :

Si vous souhaitez installer le projet en local, suivez les étapes suivantes :
(Attention, le projet nécessite la création de comptes car la base de données n'est pas partagée)

Extrait de Readme.md du dépôt [EmaFamille-Back](https://github.com/emiledelmas/EmaFamille-Back)

1. Clone the repository

```bash
  git clone https://github.com/emiledelmas/EmaFamille-Back.git
```

2. Go to the project directory

```bash
  cd EmaFamille-Back
```

3. Setup virtual environment (recommended jump to step 5 if you don't want to use virtual environment)

```bash
  python -m venv venv
```

4. Activate virtual environment

```bash
  source venv/bin/activate
```

5. Install dependencies

```bash
  pip install -r requirements.txt
```

5. Go to the Django directory

```bash
  cd emaFamille
```

6. Create a database

```bash
  python manage.py makemigrations
  python manage.py migrate
```

7. Create a superuser

```bash
  python manage.py createsuperuser
```

8. Run the server

```bash
  python manage.py runserver
```

9. Go to http://localhost:8000/admin/, login with superuser account and create a profile (Profiles) for the superuser.

10. Go to localhost:8000 and enjoy !

## Notice d'utilisation

## Tests

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Nous avons choisi la licence MIT car elle est très permissive et nous permet de garder la propriété de notre code.

## Perspectives
