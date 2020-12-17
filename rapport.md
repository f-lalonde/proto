# Description brève du travail accompli

## Tâche 1

Créer le programme proto fut relativement simple, par rapport à notre expérience personnelle.  
Les trois éléments les plus chronophages furent :

- Lire la documentation sur git-scm (par rapport à rev-list et show)
- Lire la documentation du module *subprocess* de Python
- Trouver de l'information par rapport au fonctionnement de Batch Scripting:
  - Trouver les commandes nécessaires pour notre travail (création de dossier, copie de fichier, etc.) 
  - Établir les bonnes façons d'appeler dynamiquement les commandes dans une arborescence de fichiers changeante

Le programme proto a eu deux versions différentes. La première, alors que l'on s'affairait à simplement faire fonctionner le tout, appelait une multitudes de fichiers .bat qui exécutaient chaque opération sur le système de fichier, les appels à *git* et l'appel à Java pour faire l'appel au [programme du TP1](https://github.com/TLOREM/tp1_qm_jp).  

Bien que fonctionnelle, cette version nous semblait un peu farfelue, alors nous avons approfondi notre connaissance du module subprocess et trouvé comment faire les appels directement depuis le programmes principal en Python. 

Ainsi, la version finale du programme élimine les appels aux fichiers *batch scripting*, à une exception près (qui aurait probablement pu être également importée dans le logiciel).

## Tâche 2
Cette tâche était plutôt simple! Nous faisons tout simplement l'exécution du programme du TP1 sur la version analysée du dépôt *git* voulu, puis nous importons *classes.csv* dans un *DataFrame* du module *pandas*, auquel on demande de calculer la médiane pour la colonne *Classe_BC*, et le nombre de classes, puis nous insérons ces données dans le nouveau fichier *.csv* aux côtés de l'identificateur de version. 

Seules modifications : 
- le programme du TP1 renvoyait parfois des classes "null", avec des données à 0 ou très près de 0. Cela indique que le programme du TP1 pourrait être raffiné. Pour l'instant, nous avons opté pour éliminer ces données de *classes.csv*. 
- le calcul de *classe_BC* renvoyait la valeur *Infinity* si WMC = 0 pour une classe donnée. Nous avons modifié ces valeur pour des *NaN*, qui sont automatiquement ignorées par les calculs exécutés par *pandas*. 

## Tâche 3
***Hypothèse*** : *Pour les versions de jfreechart, il existe une corrélation entre les métriques n_classes et m_c_BC. Basez votre analyse sur l’hypothèse que leurs valeurs ne sont pas normalement distribuées.*



## Bonus
