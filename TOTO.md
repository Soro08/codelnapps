# TEST Codeln:

Partir d'une structure de projet Django vierge

-   Création d'utilisateurs
-   un model Model3d() qui représente un modèle 3d (image)
-   Implémenter une fonctionnalité de 'badges':

    -   il existe plusieurs types de badge, chacun étant décerné pour une action ou série d'action effectuée par l'utilisateur sur le site

-   La liste des badges qu'un user a obtenu doit être accessible via l'api

-   Le backend doit "décerner" les badges aux users (ie: détecter quand une action a été réalisée et donner le badge au user)

-   Ecrire les tests unitaires

Exemples de badges:

-   Star: le modèle d'un user a plus de 1k views
-   Collector: un user a uploadé plus de 5 modèles
-   Pionneer: le user est inscrit depuis plus de 1 an sur le site

## TODO

1. [x] Création du projet django codeln3d
2. [x] Création d'une application clnapp
3. [x] Création des models:
    - Model3D (définir les models 3d)
    - Badge ( définir les badges)
    - UserBage (stoket les badges des utilisateur)
4. [x] Migrations des models
5. [ ] Mettre en place la logique du projet

    1. [x] Mettre en place le hooks: ajout du badge `collector` si l'utilisateur atteint les 5 model2d
    2. [x] Ajouter et configurer celery pour gérer les taches en arrière plan:

        - [x] Une tache qui s'exécute toutes les 10 secondes et vérifie si l'un des model3d de l'utilisateur a atteint les 1000 veus et lui attribut le badge `Star`
        - [x] Une tache qui s'exécute toutes les jours à 00h00 et vérifie si l'utilisateur a atteint les les 1 and d'ancienneté et lui attribut le badge `Pionneer`

6. Ecriture des tests

7. Configurer docker et docker-compose
8. Ajouter les github actions
