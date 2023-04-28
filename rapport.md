# 👪 EmaFamille

![Logo](https://emafamille.fr/static/Logo_EMAFamille.PNG)

## 🚀 Membres de l'équipe

- Emile Delmas [@emiledelmas](https://www.github.com/emiledelmas)
- Simon Chalmé [@simonchalme](https://www.github.com/simonchalme)
- Laura Bertieaux [@NapsyGit](https://www.github.com/napsygit)
- Ludovic Terrasson [@Ludooooooooo](https://www.github.com/Ludooooooooo)
- Arthur Rubio [@Hermes075](https://www.github.com/Hermes075)
- Charlotte Houzé [@cha0601](https://www.github.com/cha0601)
- Ilyane Gomis [@IlyaneGomis](https://www.github.com/IlyaneGomis)
- Florian Laporte

## 🔗 Liens vers le projet et les dépôts GitHub

- [EmaFamille.fr](https://emafamille.fr)
- [Github Repos Back](https://github.com/emiledelmas/EmaFamille-Back)
- [Github Repos Front](https://github.com/emiledelmas/EmaFamilleFront)

## 🤔 Expression du besoin

## 🦾 Organisation globale du projet

## ⚙️ Description fonctionnelle du résultat obtenu

### Technologies utilisées

- Front : HTML, CSS, JavaScript, Bootstrap 5
- Back : Python, Django
- Serveur : Nginx, Gunicorn, Docker

### Django : fonctionnement

Schéma de l'architecture de Django:
![Schema](https://raw.githubusercontent.com/emiledelmas/EmaFamille-Back/master/images%20Rapport/django%20schema.jpg)

## 🏗️ Description de l’architecture technique et applicative du projet avec justification des choix effectués

### 💻 Developpement Web

#### Front

Le front est développé en HTML, CSS et JavaScript. Nous avons utilisé le framework Bootstrap 5 pour le design et la mise en page.

#### Back

Le back est développé en Python avec le framework Django. Nous avons choisi Django car il est très complet et permet de développer rapidement des applications web. Il est également très bien documenté et dispose d'une communauté active.

### 🔒 Base de données

Nous avons choisi SQLite comme base de données car elle est très simple à mettre en place et suffisante pour notre projet. Elle est également très bien intégrée à Django.

### 🖥️ Serveur et déploiement

Nous avons choisi d'utiliser Docker pour le déploiement de notre application. Docker permet de créer des conteneurs qui contiennent tous les éléments nécessaires au fonctionnement de l'application. Cela permet de déployer l'application facilement et de la rendre indépendante de l'environnement de déploiement.

Nous avons ainsi créé 2 conteneurs :

- Un conteneur Django qui contient le code de l'application et qui est lancé avec Gunicorn
- Un conteneur Nginx qui sert de serveur web et qui est relié au conteneur Django, il sert à servir les fichiers statiques et à rediriger les requêtes vers le conteneur Django

Un troisième conteneur est utilisé pour la mise en place de l'HTTPS avec Let's Encrypt. Il est lancé en même temps que les deux autres conteneurs et permet de gérer automatiquement les certificats SSL/TLS.

Schéma de l'architecture de déploiement :
![Schema](https://raw.githubusercontent.com/emiledelmas/EmaFamille-Back/master/images%20Rapport/architecture%20serveur.jpg)

## 💾 Notice d’installation

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

10. Go to http://localhost:8000 and enjoy !

## ⌨️ Notice d'utilisation

### Utilisation de base

En arrivant sur la page d'accueil, vous pouvez vous connecter ou vous inscrire.
Une fois connecté, vous arrivez sur la page Feed : vous pouvez voir les posts des personnes sur Emafamille.

En haut vous pourrez faires des posts (texte et/ou image).

Vous pouvez éditer votre profil à gauche et ajouter des nouveaux amis à droite.

### Utilisation avancée, Famille

Vous pouvez créer une famille en cliquant sur le bouton "Rejoindre/ Créer une famille" en haut à droite.

Les personnes voulants ensuite rejoindre votre famille devront envoyer une demande que vous pourrez accepter ou refuser.

En étant chef de famille, vous pouvez supprimer des membres de votre famille et modifier complètement votre famille (nom, description, image). Vous pouvez également quitter votre famille et désigner un nouveau chef de famille.

Les familles possèdent également un album photo, vous pouvez y ajouter des photos et les supprimer.

## 🧪 Tests

Nous avons choisi les tests intégrés à Django pour tester notre application. Nous avons testé la fonction login afin de voir les codes d'erreurs retournés.

## 🔓 Licence

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Nous avons choisi la licence MIT car elle est très permissive et nous permet de garder la propriété de notre code.

## 🙃 Perspectives

Nous avons plusieurs idées d'améliorations pour le projet :

- Feed avec que les amis/ la famille
- Avoir des stories
- Conversations privées
- Conversation de famille
- Arbre généalogique de la famille
- Badges sur les assos et listes

Cette liste est non-exhaustive !
