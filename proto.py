# Francis Lalonde - 801363
# Trystan Majumdar - 20091517

import subprocess
import os
import sys
import pandas as pd
import numpy as np

options = -1

if len(sys.argv) < 2:

    print("\nBienvenu sur proto (version FL-TM). Veuillez choisir une des 3 options suivantes :\n")

    while True:
        try:
            options = int(input(
                "1. Analyser le plus récent commit d'un git\n"
                "2. Analyser un échantillon aléatoire de 10% des commits d'un git (peut être très long)\n"
                "3. Quitter le logiciel.\n"))

            if not (options == 1 or options == 2 or options == 3):
                raise Exception
            break

        except:
            print("Ceci n'est pas une option valide. Veuillez appuyez sur 1, 2 ou 3, selon votre choix :\n")

    if options == 3:
        sys.exit("Processus terminé à la demande de l'utilisateur")

    git_address = input("Veuillez copier l'adresse du git à analyser : ")

else:
    if len(sys.argv) == 3:
        options = int(sys.argv[2])
    else:
        options = 1

    git_address = sys.argv[1]

print("\nMerci. On se met au boulot! Veuillez patienter...")

name = git_address.split("/")[-1].split(".git")[0]

subprocess.run("list_commits.bat " + git_address, check=True)

file = open("./temp/commitsList.txt")
versions = file.read().split("\n")
file.close()

wd = os.getcwd()

# il y a surement quelque chose de plus sécuritaire pour monter au dossier principal...
if "dist\\proto" in wd:
    csv_dir = wd.split("dist\\proto")[0]
else:
    csv_dir = wd + "\\"

csv = open(csv_dir + name + ".csv", 'a')
csv.write("id_version, n_classes, m_c_BC\n")


def analyse(version):
    # invoque l'outil développé durant le TP 1
    subprocess.run(["java", "-jar", ".\Analyzer.jar", wd+"\\temp\\"], cwd=wd + "\\temp\\", shell=True, check=True)

    # importe les valeurs dans un DataFrame de Pandas
    data = pd.read_csv("./temp/classes.csv", header=0, names=["chemin", "classe", "LOC", "CLOC", "DC", "WMC", "BC"])

    # les données générées donnent parfois des classes "null", avec des valeurs dont on ne connait pas l'importance.
    data.BC.replace(" Infinity", np.NaN)
    data.drop_duplicates("classe", False, True)

    # calcul nombre de classe, et médiane des valeurs BC
    class_count = data.classe.count()
    BC_median = data.BC.median()

    return class_count, BC_median


# jump : saut fait entre les versions analysée
# max_loop : nombre d'analyse effectuées
# versions : tableau contenant toutes les <HEX> des versions du projet
# csv : writer sur le fichier csv contenant l'analyse des versions du projet
def analyse_loop(versions, csv):
    subprocess.run(['copy', 'Analyzer.jar', wd + "\\temp\\"], cwd=wd, shell=True, check=True)
    for i in range(len(versions)):
        version = versions[i]
        subprocess.run(["git", "show", "-s", "--format=%ci", version], cwd=wd+"\\temp\\", shell=True)
        if version == '':
            continue
        if i != 0:
            # on renomme les fichier "classes.csv et methodes.csv"
            subprocess.run(['ren', 'classes.csv', 'classes_' + str(i) + '.csv'], cwd=wd + "\\temp\\", shell=True,
                           check=True)
            subprocess.run(['ren', 'methodes.csv', 'methodes' + str(i) + '.csv'], cwd=wd + "\\temp\\", shell=True,
                           check=True)

            # on change à la prochaine version analysée
            subprocess.run(["git", "reset", "--hard", version], cwd=wd + "\\temp\\", shell=True, check=True)
        class_count, BC_median = analyse(version)
        csv.write(str(version) + "," + str(class_count) + "," + str(BC_median) + "\n")
    csv.close()

    # grand nettoyage. Il pourrait être utile de rapatrier les fichiers classes*.csv et methodes*.csv pour fin d'analyse
    subprocess.run(['rd', '/s', '/q', wd + "\\temp\\"], shell=True, check=True)


def analyse_once(versions, csv):
    version = versions[0]
    subprocess.run(['copy', 'Analyzer.jar', wd + "\\temp\\"], cwd=wd, shell=True, check=True)
    class_count, BC_median = analyse(version)
    csv.write(str(version) + "," + str(class_count) + "," + str(BC_median) + "\n")
    csv.close()
    subprocess.run(['rd', '/s', '/q', wd + "\\temp\\"], shell=True, check=True)


# Choisi un échantillon de 10% en préservant l'ordre des commits dans le temps.
def pick_sample(versions):
    temp_dict = {}
    for i in range(len(versions)):
        temp_dict[i] = versions[i]
    temp_list = list(temp_dict.keys())

    n = int(np.floor(len(versions) / 10))
    indexes = np.random.choice(temp_list, n, False)
    indexes.sort()
    returned_list = []
    for i in range(len(indexes)):
        returned_list.append(versions[indexes[i]])
    return returned_list


if options == 1:
    analyse_once(versions, csv)

elif options == 2:
    analyse_loop(pick_sample(versions), csv)

else:
    print("Option invalide, aucun travail n'a été effectué. La prochaine phrase est un mensonge.\n")

input("Travail terminé! Vous trouverez le fichier .csv contenant l'analyse à cet endroit : \n\n"
      + csv_dir + name + ".csv\n\nAppuyez sur Enter pour terminer")
