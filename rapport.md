# 👪 EMA Famille

![Logo](https://emafamille.fr/static/Logo_EMAFamille.PNG)

Version PDF disponible avec : [md2pdf](https://md2pdf.netlify.app/)

## 🚀 Membres de l'équipe

- Emile Delmas [@emiledelmas](https://www.github.com/emiledelmas)
- Simon Chalmé [@simonchalme](https://www.github.com/simonchalme)
- Laura Bertieaux [@laurabertieaux](https://www.github.com/laurabertieaux)
- Ludovic Terrasson [@Ludooooooooo](https://www.github.com/Ludooooooooo)
- Arthur Rubio [@Hermes075](https://www.github.com/Hermes075)
- Charlotte Houzé [@cha0601](https://www.github.com/cha0601)
- Ilyane Gomis [@Ilyanee](https://www.github.com/Ilyanee)
- Florian Laporte

## 🔗 Liens vers le projet et les dépôts GitHub

- [EmaFamille.fr](https://emafamille.fr)
- [Github Repos Back](https://github.com/emiledelmas/EmaFamille-Back)
- [Github Repos Front](https://github.com/emiledelmas/EmaFamilleFront)

## 🤔 Expression du besoin

Notre objectif est de rendre la communication entre les emayens plus simple et spontanée, et mettre en avant les différentes familles présentes à l'EMA (groupes d'étudiants de différentes promotions s'entendant bien) et leur offrir une plateforme privilégiée pour partager des souvenirs. Nous voulons aussi rendre ces familles plus accessibles aux nouveaux élèves, pour qu'ils puissent s'intégrer plus facilement au sein de l'école

Prenons pour exemple un élève s'appelant Pierre.
Pierre vient d'intégrer l'école des Mines et ne connaît pas encore l'organisation des différents élèves en son sein. Suite à une recommandation d'un ami, Pierre décide de s'inscrire sur EMA Famille et découvre les différentes familles de l'école. Pierre peut donc d´ores et déjà, grâce aux différents tags présents sur le profil de la famille, estimer si l'ambiance de la famille va lui plaire.

## 🦾 Organisation globale du projet

### ✨ Front

Pour se familiariser avec tout les languages nécéssaires pour notre projet, nous avons fait le choix de commencer par développer le front pour avoir une première approche avec le language HTML et CSS. Nous avons ensuite utilisé la librairie bootstraps et les snippets, une fois que le language était assimilé par chacun, pour avoir le temps de s'occuper du back par la suite.

### 🗂️ Base de données

Il nous fallait ensuite un moyen d'enregistrer les comptes des utilisateurs et leurs informations. Pour cela nous avons eu recours à une base de données.

Les informations stockées pour les utilisateurs sont:

- identifiant (obligatoire)
- nom (obligatoire)
- prénom (obligatoire)
- promotion (obligatoire)
- photo de profil (optionnel)
- description (optionnel)
- adresse mail (obligatoire)

                            **_vérifier si il manque pas des trucs  + dire ce qui est obligatoire/optionnel_**

### 👨‍💻 Back

Il nous fallait ensuite rendre le site fonctionnel, nous sommes ainsi passé sur PyCharm, où nous avons téléchargé tout le travail éffectué précédemment sur IntelliJ.

#### Liens entre les pages

Les pages étaient créées et ordonnées cependant aucune connexion entre elles n´existait; nous avons donc commencé par rendre tous les boutons fonctionnels afin de pouvoir naviguer sur l'ensemble des pages composant le site.

#### Controle pour accès au site

Grâce a la création de la base de données nous avons pu rendre fonctionnelle la page de connexion. Ainsi pour avoir accès au site il faut un identifiant enregistré dans la base de données et le mot de passe correspondant.

#### Création des profils

Ensuite l'affichage doit s'adapter au compte connecté. Il a fallut modifier certaines pages pour qu'elles affichent les informations propre au compte connecté.

#### Les posts sur le feed

Lorsque les profils étaient oppérationnels, nous avons codé la possibilité de poster des messages et des images visibles par tous. Chaque post est enregistré dans la base de données avec sa date de publication, son auteur (identifiant)

                            **_vérifier s'il manque pas des trucs  + dire ce qui est obligatoire/optionnel_**

Après quelques test, nous avons ajouté la possibilité de supprimer les posts en tant qu'auteur, d'aimer et de commenter.

#### Possibilité d'avoir des amis

Une fois les comptes créés il était possible de connecté les comptes avec le système d'amis. Certaines fonctionnalités ont été ajoutés comme l'affichage du nombre d'ami, ou le tri des post pour afficher seulement ceux des amis.

#### Les familles

Le but de ce site était de permettre aux gens de trouver une "Famille" à l'EMA. Une fois que le site était globalement fonctionnel, nous avons ajouter la possibilité de faire parti d'une famille. Pour cela une page entierement dédiée a la à été ajoutée. Et pour les personnes n'en ayant pas, ils peuvent soit demander à être ajoutés dans une famille, soit en créer une. Et c'est grace aux posts du forum que les gens peuvent être mis au courant des activités organisées par les familles pour les rencontrer.

Les familles sont enregistrées dans la base de données avec les informations suivantes:

- nom
- chef
- logo
- description
- membres

Les familles ont accès à un forum reservé, une galerie photo privée et la gestion des noveaux membre est gérée par le chef de famille (créateur de la famille sur le site).
Dans cette phase de la conception du projet, c'est donc un ensemble de fonctionnalités qui ont été ajoutées aux éléments existants.

### 🌎 Lancement du projet en ligne

La dernière étape à été de mettre une version de notre site sur internet pour permettre à des étudiants de l'école de la tester.

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

Nous avons choisi SQLite comme base de données car elle est très simple à mettre en place et suffisante pour notre projet. Elle est également très bien intégrée à Django. Pour une utilisation plus avancé avec plus d'utilisateurs, nous aurions pu utilisé PostgreSQL qui est plus adapté à une utilisation en production.

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

Nous vous conseillons d'utiliser la version de production de EmaFamille afin de la tester. Pour cela, rendez-vous sur [EmaFamille.fr](https://emafamille.fr) !

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

```python
class TestViews(TestCase):

    def test_login_GET(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PageConnexion.html')

    def test_login_POST(self):
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PageConnexion.html')
```

## 🔓 Licence

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Nous avons choisi la licence MIT car elle est très permissive et nous permet de garder la propriété de notre code.
Cette licence autorise :

- l'utilisation à des fins commerciales
- la modification
- la distribution
- l'utilisation privée

La condition est de citer les auteurs du code.

Les limitations de cette licence sont :

- aucune responsabilité des auteurs
- aucune garantie du logiciel

## 🙃 Perspectives

Nous avons plusieurs idées d'améliorations pour le projet :

- Ajout d'une mention légale (obligatoire)
- Feed avec que les amis/ la famille
- Avoir des stories
- Conversations privées
- Conversation de famille
- Arbre généalogique de la famille
- Badges sur les assos et listes

Cette liste est non-exhaustive et nous avons d'autres idées en tête.

D'autres aspects comme le coût financier ou la sécurité doivent être envisagés avant de les mettre en place.
