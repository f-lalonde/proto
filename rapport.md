# Rapport

## Description brève du travail accompli

### Tâche 1

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

### Tâche 2
Cette tâche était plutôt simple! Nous faisons tout simplement l'exécution du programme du TP1 sur la version analysée du dépôt *git* voulu, puis nous importons *classes.csv* dans un *DataFrame* du module *pandas*, auquel on demande de calculer la médiane pour la colonne *Classe_BC*, et le nombre de classes, puis nous insérons ces données dans le nouveau fichier *.csv* aux côtés de l'identificateur de version. 

Seules modifications : 
- le programme du TP1 renvoyait parfois des classes "null", avec des données à 0 ou très près de 0. Cela indique que le programme du TP1 pourrait être raffiné. Pour l'instant, nous avons opté pour éliminer ces données de *classes.csv*. 
- le calcul de *classe_BC* renvoyait la valeur *Infinity* si WMC = 0 pour une classe donnée. Nous avons modifié ces valeur pour des *NaN*, qui sont automatiquement ignorées par les calculs exécutés par *pandas*. 

### Tâche 3

Une fois le nouveau fichier csv calculé (environ 2 heures pour 10% aléatoire de jFreeChart), on a importé les données dans un *DataFrame* de *pandas*.  

Nous avons tout d'abord tracé un graphique sur lequel on comparait l'évolution de *n_classe* et *m_c_bc* par rapport au même axe des x, représentant les dates des commits. Nous avons pu observer ceci :  
![graphique à deux axes y : n_classe par rapport au temps ; m_c_bc par rapport au temps](https://github.com/f-lalonde/proto/blob/main/analyses/classe%20n%20vs%20bc.png)


Nous avons ensuite utilisés les outils à notre disposition pour faire l'évaluation de l'hypothèse, dans la prochaine section.

### Bonus


## Évaluation de l'hypothèse (Tâche 3)

***Hypothèse*** : *Pour les versions de jfreechart, il existe une corrélation entre les métriques n_classes et m_c_BC. Basez votre analyse sur l’hypothèse que leurs valeurs ne sont pas normalement distribuées.*

Tout d'abord, aveuglément, on pourrait conclure à un faible correlation en exécutant la méthode de Spearman sur l'ensemble des données :
```
print(data.corr(method = 'spearman')):      print(data.corr(method = 'pearson')):
            n_classe   m_c_bc                           n_classe   m_c_bc
  n_classe   1.00000 -0.35712                 n_classe  1.000000 -0.563265
  m_c_bc    -0.35712  1.00000                 m_c_bc   -0.563265  1.000000
```

Par contre, en observant le graphique généré plus haut, on peut voir qu'il y a trois, voire quatre grande périodes sur lesquel jfreechart a été développé, séparés par des grands moments sans *commits*. Nous avons séparé ces trois zones (la quatrième zone n'ayant que très peu de points de données, nous l'avons laissée avec la 3e) :

- Zone 1 : 237 points de données, allant de 2007-07-06 à 2010-07-14
- Zone 2 : 90 points de données, allant de 2011-10-06 à 2015-09-09
- Zone 3 : 75 points de données, allant de 2016-01-16 à 2020-10-31

Une fois ces trois zones séparées, voici les données que nous trouvons : 

**Spearman**                                              **Pearson**
```
Zone 1 : 
           n_classe    m_c_bc                         n_classe    m_c_bc               
n_classe  1.000000 -0.917197                n_classe  1.000000 -0.799509
m_c_bc   -0.917197  1.000000                m_c_bc   -0.799509  1.000000 

Zone 2 : 
           n_classe    m_c_bc                         n_classe    m_c_bc
n_classe  1.000000  0.045932                n_classe  1.000000 -0.089756
m_c_bc    0.045932  1.000000                m_c_bc   -0.089756  1.000000 

Zone 3 : 
           n_classe    m_c_bc                         n_classe    m_c_bc
n_classe  1.000000  0.808461                n_classe  1.000000  0.901997
m_c_bc    0.808461  1.000000                m_c_bc    0.901997  1.000000 
```

C'est à dire que l'on semble avoir une très forte correlation entre les valeurs de n_classe et m_c_bc, mis à part durant les commits se trouvant en zone 2.  
Il serait avantageux de vérifier ce qu'il s'est passé entre ces dates dans le cycle de vie du logiciel, ou encore s'ils s'agissent de *commits* provenant d'un développeur en particulier. 
