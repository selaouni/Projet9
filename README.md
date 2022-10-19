# Openclassrooms / Projet9 - parcours "Developpeur d'application python"

Date: Septembre 2022 


## Titre du projet:  
Développez une application Web en utilisant Django

## Mentor:
Idriss Benjeloun

## Description:   
Ce projet concerne le  developpement d'une application  qui permet de faire des critiques de livres
l'objectif principal est de commercialiser un produit MVP(Produit minimum viable) permettant à une 
communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

les fonctionnalités du projet sont comme suit:

- Inscription et de connexion de l'utilisateur;
- consulter un flux contenant les derniers tickets et les commentaires des 
  utilisateurs qu'il suit, classés par ordre chronologique
- demander des critiques de livres ou d’articles, en créant un ticket ; 
- Créer de nouveaux tickets pour demander une critique sur un livre/article;
- créer des critiques en réponse à des tickets ;
- créer des critiques qui ne sont pas en réponse à un ticket;
- publier des critiques de livres ou d’articles
- Voir, modifier et supprimer ses propres tickets et commentaires ; 
- Un utilisateur peut suivre d'autres utilisateurs.
- Un utilisateur peut voir ses abonnements et ses abonnées dans une liste avec
  option de désabonnement.

Les models de la la base de données sont:
- Ticket
- Review
- UserFollows

Technologie utilisés:
- framework Django ;
- SQLite comme base de données de développement locale,


## Exécution du programme
    - installer la derniere version de django (https://docs.djangoproject.com/en/4.1/topics/install/)
    - Créer un dossier projet sur votre machine comme repository local
    - Clonner le repo distant dans votre repository local
    - Se positionner dans le  répertoire "P9" avec:
        >> cd P9
    - Créer l'environnement virtuel avec:
        >> env python -m venv env
    - Activer l'environnement virtuel avec :
        >> source env/bin/activate
    - Installez les modules necessaires à l'aide du fichier requirement.txt avec:   
        >> pip install -r requirements.txt  
    - Exécuter la migration de la base de données (les modèles) avec: 
        >> python manage.py migrate
    - Lancer le serveur (en fonction de votre version de python) avec :
        >>python manage.py runserver ou python3 manage.py runserver
    - Lancer la page web à partir du l'URL :  http://127.0.0.1:8000/

Remarque: assurez-vous que votre version de Python est l'une de celles prises 
en charge par la dernière version de Django :
https://docs.djangoproject.com/en/4.1/faq/install/#faq-python-version-support

Nota , versions appliquées pour ce projet: 
    
    - python : 3.10.5
    - Django : 4.1.1
    - IDE utilisé: pycharm V2022.2.1 (Community Edition)



## Historique des Versions:    

 *Principales versions sous Github*

 - PEP8 verification date 19/10/2022
 - site design and CSS code - 17/10/2022 
 - Model update(resize photo) - 17/10/2022 
 - Ticket snippet code - 17/10/2022 
 - Review/ticket delete & update(view and HTML) - 14/10/2022 
 - Suscribe and unsuscribe - 14/10/2022 
 - Review in response to a ticket - 14/10/2022
 - feed page + page layout - 12/10/2022 
 - Signup code - 29/09/2022
 - first version of ticket creation - 28/09/2022
 - First version with authentication - 24/09/2022 


## Acknowledgments (code inspiration): 
- Discord DA python
- https://openclassrooms.com/fr/courses/7192426-allez-plus-loin-avec-le-framework-django
- https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django
- https://www.moonbooks.org/Articles/Comment-supprimer-une-table-dans-une-base-de-donnees-avec-le-framework-web-django-/
- https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
- https://prograide.com/pregunta/61054/comment-inclure-des-fichiers-image-dans-les-modeles-django
- https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Home_page
- https://iancarpenter.dev/2021/09/19/django-object-has-no-attribute-save/
- https://www.youtube.com/watch?v=YyShrxl-Juo
- https://www.youtube.com/watch?v=lG0TGOVT0-o
- https://riptutorial.com/django/example/32472/use-of----extends---------include----and----blocks---
- https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#include
- https://stackoverflow.com/questions/63298721/how-to-update-imagefield-in-django
- https://www.csestack.org/add-css-static-files-django/#:~:text=%E2%94%80%E2%94%80registration-,Including%20CSS%20in%20Django%20Template,HTML
