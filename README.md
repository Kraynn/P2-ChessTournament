__________________________
SWISS CHESS TOURNAMENT - Projet #2
--------------------------

Le programme a pour objet la création d'un environnement de gestion de tournois d'échecs comprenant:

- La création de joueurs et leur enregistrement en base.
- La création de tournois et leur enregistrement en base.
- Le lancement et la reprise de tournois selon le système Suisse.
- La mise à jour du classement des joueurs.
- La génération de différents rapports.

______________
HOW TO INSTALL
--------------

Importation des scripts:
---------------------------

Téléchargez et extaire le contenu du repertoire https://github.com/Kraynn/P2-ChessTournament dans le répertoire local. 



Ou cloner le répertoire via github en utilisant la commande:
> git clone https://github.com/Kraynn/P2-ChessTournament
> 
Puis déplacer le contenu dans le repertoire local voulu.

__________________________________________________________
Création de l'environnement virtuel:
------------------------------------
Exectuer les commandes suivantes dans l'invité de commande au sein du répertoire local voulu:
>
>python -m venv chess_env

>chess_env\Scripts\activate.bat

>pip install -r requirements.txt

___________________________________________________



Execution des scripts:
----------------------
Excuter la commande suivante pour lancer le programme:
>
>python main.py

Executer la commande suivantte pour générer le rapport:
>
> flake8 --filename=*.py --format=html --htmldir=flake-report --exclude test\lib --ignore=E501

*(Nous choisissons d'ignorer l'erreur 501 relatif à la longueur d'une ligne du fait de la nature de certaines variables que  l'on ne peut déclarer autrement)*

***************************








