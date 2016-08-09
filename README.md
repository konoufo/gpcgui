# gpcgui
###Présentation
Ceci est le code source de ce qui deviendra l'interface utilisateur de GPC.
L'idée est de développer une interface style-web. 
Le programme comprend donc un serveur Python qui exécute le code GPC et qui interagit avec l'utilisateur par des requêtes HTTP
comme avec une application web. Sauf que tout ceci se passe localement.

###Installation
Dans un dossier au choix, à l'aide du terminal Windows (dans Pycharm ou CMD):
`git clone https://github.com/konoufo/gpcgui.git`
`bin\gpcgui\Scripts\pip install -r source\requirements.txt`

###Utilisation
Toujours dans le même dossier:
`bin\gpcgui\Scripts\python source\run.py` (démarrage du serveur)
Puis ouvrir un navigateur et aller à [http://localhost:5000](http://localhost:5000).

###TODOs
- Relier à GPC et en faire un repositoire unique.
- Intégrer un "navigateur" léger dans le programme pour pouvoir opérer dans une fenêtre complètement indépendante.
- Développer un thème pour les différentes plateformes, pour un rendu plus "natif" !
