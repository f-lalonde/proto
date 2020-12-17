```
      ___         ___           ___                       ___     
     /  /\       /  /\         /  /\          ___        /  /\    
    /  /::\     /  /::\       /  /::\        /  /\      /  /::\ *   
   /  /:/\:\   /  /:/\:\     /  /:/\:\      /  /:/     /  /:/\:\  
  /  /:/~/:/  /  /:/~/:/    /  /:/  \:\    /  /:/     /  /:/  \:\ 
 /__/:/ /:/  /__/:/ /:/___ /__/:/ \__\:\  /  /::\    /__/:/ \__\:\
 \  \:\/:/   \  \:\/:::::/ \  \:\ /  /:/ /__/:/\:\   \  \:\ /  /:/
  \  \::/     \  \::/~~~~   \  \:\  /:/  \__\/  \:\   \  \:\  /:/ 
   \  \:\      \  \:\        \  \:\/:/        \  \:\   \  \:\/:/  
    \  \:\      \  \:\        \  \::/          \__\/    \  \::/   
     \__\/       \__\/         \__\/                     \__\/    
```

Par :
Francis Lalonde - 801363  
Trystan Majumdar - 20091517

Dans le cadre du cours IFT-3913

\*(*logo généré par http://patorjk.com/software/taag/*)

## Description

Proto fait l'analyse de projet en Java. Il prend en entrée un lien vers un dépôt git contenant le projet, et retourne un fichier .csv contenant :
- l'id sous format hexadécimal du ou des commit(s) analysé(s)
- le nombre de classes dans le projet analysé
- la médiane pour les classes de la mesure BC (degré selon lequel une classe est bien commentée : BC = DC / WMC)
  - DC : densité de commentaires pour une classe : DC = CLOC / LOC
  - LOC : nombre de lignes de code d’une classe
  - CLOC : nombre de lignes de code d’une classe qui contiennent des commentaires
  - WMC : *Weighted Methods per Class*, pour chaque classe. C’est la somme pondérée des complexités des méthodes d'une classe. Si toutes les méthodes d'une classe sont de complexité 1, elle est égale au nombre de méthodes.

## Instructions :

- Exécuter "proto.bat"
- Suivre les directives à l'écran :
  - Appuyer sur 1 pour une analyse du dernier commit seulement sur un dépot de type git
  - Appuyer sur 2 pour une analyse d'un échantillon aléatoire de 10% des commits d'un dépot (peut être long!)
  - Appuyer sur 3 pour quitter, si le logiciel fut démarré par erreur. 

- Si on a appuyé sur 1 ou 2, l'utilisateur sera invité a copier le lien vers le dépôt git sur lequel il veut exécuter l'analyse.
- Une fois terminé, le programme va générer un fichier .csv contenant les données calculées. Le chemin d'accès sera également imprimé à l'écran, au besoin.

Simple comme ça!

## TROUBLESHOOTING :

Si jamais le travail a été interrompu avant la fin du traitement, il est 
possible qu'il soit nécessaire d'aller effacer le dossier .\dist\proto\temp, 
s'il existe. Sans quoi, une nouvelle exécution du logiciel va retourner une 
erreur et s'interrompre.
