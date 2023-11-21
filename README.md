# Codeln 3D model App

[![ci-cd](https://github.com/Soro08/codelnapps/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/Soro08/codelnapps/actions/workflows/ci_cd.yml)

Ce projet est une application web Django qui fonctionne avec Docker et Docker Compose. Il inclut une configuration pour lancer l'application localement en utilisant Docker.

## Installation
### Avec Docker
Pour exécuter ce projet localement, assurez-vous d'avoir installé Docker et Docker Compose sur votre système. Vous pouvez les installer en suivant les instructions officielles :

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

Une fois que Docker et Docker Compose sont installés, suivez ces étapes :

1. Clonez le dépôt depuis GitHub :

    ````bash
    $ git clone https://github.com/Soro08/codelnapps.git
    $ cd codelnapps

    ````

2. Copiez le fichier .env.example en tant que .env :

    ```bash
    $ cp .env.sample .env
    ```

    Modifiez les variables d'environnement dans le fichier `.env` selon vos besoins.

3. Construisez les conteneurs Docker :

    ```bash
    $ docker-compose -f docker-compose.local.yml build
    ```

4. Lancez les conteneurs Docker

    ```bash
    $ docker-compose -f docker-compose.local.yml up -d
    $ docker-compose -f docker-compose.local.yml exec web python manage.py create_badges

    $ docker-compose -f docker-compose.local.yml exec web python manage.py createsuperuser
    ```

5. Les conteneurs Docker seront démarrés, et l'application sera accessible à l'adresse:

- http://localhost:8000
- http://localhost:8000/api/
- http://localhost:8000/admin

### Sans Docker


1. Clonez le dépôt depuis GitHub :

    ````bash
    $ git clone https://github.com/Soro08/codelnapps.git
    $ cd codelnapps

    ````

2. Copiez le fichier .env.example en tant que .env :

    ```bash
    $ cp .env.sample .env
    ```

    Modifiez les variables d'environnement dans le fichier `.env` selon vos besoins.


3. Créer et activer un environnement virtuel:

    ```sh
    $ python3.11 -m venv venv && source venv/bin/activate
    ```

4. Installer les requirements:

    ```sh
    (venv)$ cd apps
    (venv)$ pip install -r requirements.txt
    ```

5. Appliquer les migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

6. Créer un superutilisateur et alimenter la base de données:

    ```sh
    (venv)$ python manage.py createsuperuser
    (venv)$ python manage.py create_badges
    ```
	
7. Lancer le projet:

    ```sh
    (venv)$ python manage.py runserver
    ```
    
l'application sera accessible à l'adresse:

- http://localhost:8000
- http://localhost:8000/api/
- http://localhost:8000/admin

## Fonctionnalités disponibles:

Vous pouvez accéder à la liste des fonctionnalitées de l'application à l'adresse suivante : https://codeln.soronbe.com/

## Documentation

La documentation complète de ce projet via postman est disponible à l'adresse : https://documenter.getpostman.com/view/4931083/2s9YXe9581

## Réalisé avec

Ce projet a été développé en utilisant les technologies suivantes :

-   ![Python Badge](https://img.shields.io/badge/Python-3.11-blue?logo=python)
-   ![Django Badge](https://img.shields.io/badge/Django-4.2.7-green?logo=django)
-   ![Django REST framework Badge](https://img.shields.io/badge/Django%20REST%20framework-3.14.0-orange?logo=django)
-   ![Celery Badge](https://img.shields.io/badge/Celery-5.3.4-red?logo=celery)
-   ![AWS S3 Badge](https://img.shields.io/badge/AWS%20S3-Latest-orange?logo=amazon-aws)
-   ![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-14-blue?logo=postgresql)
-   ![Redis Badge](https://img.shields.io/badge/Redis-7.2-red?logo=redis)

-   ![Docker Badge](https://img.shields.io/badge/Docker-20.10-blue?logo=docker)
-   ![Docker Compose Badge](https://img.shields.io/badge/Docker%20Compose-2.2.3-blue?logo=docker)

-   ![Nginx-Proxy Badge](https://img.shields.io/badge/Nginx%20Proxy-0.9-orange?logo=nginx)
-   ![Postman Badge](https://img.shields.io/badge/Postman-10.19.7-orange?logo=postman)
-   ![Ubuntu Badge](https://img.shields.io/badge/Ubuntu-20.04-blue?logo=ubuntu)
-   ![GitHub Actions Badge](https://img.shields.io/badge/GitHub%20Actions-green?logo=github-actions)

Ces technologies ont été soigneusement sélectionnées pour créer et déployer ce projet. Chacune d'entre elles a joué un rôle essentiel dans la conception, le développement et le déploiement de l'application.
