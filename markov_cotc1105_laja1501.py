#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Ce fichier contient la classe markov, à utiliser pour solutionner la problématique.
    C'est un gabarit pour l'application de traitement des fréquences de mots dans les oeuvres d'auteurs divers.

    Les méthodes aparaissant dans ce fichier définissent une API qui est utilisée par l'application
    de test testmarkov.py
    Les paramètres d'entrée et de sortie (Application Programming Interface, API) sont définis,
    mais le code est à écrire au complet.
    Vous pouvez ajouter toutes les méthodes et toutes les variables nécessaires au bon fonctionnement du système

    La classe markov est invoquée par la classe testmarkov (contenue dans testmarkov.py):

        - Tous les arguments requis sont présents et accessibles dans args (dans le fichier testmarkov.py)
        - Note: vous pouvez tester votre code en utilisant les commandes:
            + "python testmarkov.py"
            + "python testmarkov.py -h" (donne la liste des arguments possibles)
            + "python testmarkov.py -v" (mode "verbose", qui indique les valeurs de tous les arguments)

    Copyright 2018-2022, F. Mailhot et Université de Sherbrooke
"""

import os
import glob
import ntpath
import argparse


class markov:
    """Classe à utiliser pour coder la solution à la problématique:

        - Contient certaines fonctions de base pour faciliter le travail (recherche des auteurs).
        - Les interfaces du code à développer sont présentes, mais tout le code est à écrire
        - En particulier, il faut compléter les fonctions suivantes:
            - find_author(oeuvre)
            - gen_text(auteur, taille, textname)
            - get_nth_element(auteur, n)
            - analyze()

    Copyright 2018-2022, F. Mailhot et Université de Sherbrooke
    """

    # Le code qui suit est fourni pour vous faciliter la vie. Il n'a pas à être modifié
    # Signes de ponctuation à retirer
    PONC = ["!", "?", ",", ".", ":", ";", "(", ")", "-", "_", "'"]

    def set_ponc(self, value):
        """Détermine si les signes de ponctuation sont conservés (True) ou éliminés (False)

        Args:
            value (boolean) : Conserve la ponctuation (Vrai) ou élimine la ponctuation (Faux)

        Returns:
            void : ne fait qu'assigner la valeur du champs keep_ponc
        """
        self.keep_ponc = value

    def print_ponc(self):
        print("Signes de ponctuation à retirer: ", self.PONC)

    def set_auteurs(self):
        """Obtient la liste des auteurs, à partir du répertoire qui les contient tous

        Note: le champs self.rep_aut doit être prédéfini:
            - Par défaut, il contient le répertoire d'exécution du script
            - Peut être redéfini par la méthode set_aut_dir

        Returns:
            void : ne fait qu'obtenir la liste des répertoires d'auteurs et modifier la liste self.auteurs
        """
        files = self.rep_aut + "/*"
        full_path_auteurs = glob.glob(files)
        for auteur in full_path_auteurs:
            self.auteurs.append(ntpath.basename(auteur))
        return

    def get_aut_files(self, auteur):
        """Obtient la liste des fichiers (avec le chemin complet) des oeuvres d'un auteur

        Args:
            auteur (string): le nom de l'auteur dont on veut obtenir la liste des oeuvres

        Returns:
            oeuvres (Liste[string]): liste des oeuvres (avec le chemin complet pour y accéder)
        """
        auteur_dir = self.rep_aut + "/" + auteur + "/*"
        oeuvres = glob.glob(auteur_dir)
        return oeuvres

    def set_aut_dir(self, aut_dir):
        """Définit le nom du répertoire qui contient l'ensemble des répertoires d'auteurs

        Note: L'appel à cette méthode extrait la liste des répertoires d'auteurs et les ajoute à self.auteurs

        Args (string) : Nom du répertoire en question (peut être absolu ou bien relatif au répertoire d'exécution)

        Returns:
            void : ne fait que définir le nom du répertoire qui contient les répertoires d'auteurs
        """
        cwd = os.getcwd()
        if os.path.isabs(aut_dir):
            self.rep_aut = aut_dir
        else:
            self.rep_aut = os.path.join(cwd, aut_dir)

        self.rep_aut = os.path.normpath(self.rep_aut)
        self.set_auteurs()
        return

    def set_ngram(self, ngram):
        """Indique que l'analyse et la génération de texte se fera avec des n-grammes de taille ngram

        Args:
            ngram (int) : Indique la taille des n-grammes (1, 2, 3, ...)

        Returns:
            void : ne fait que mettre à jour le champs ngram
        """
        self.ngram = ngram

    def __init__(self):
        """Initialize l'objet de type markov lorsqu'il est créé

        Returns:
            void : ne fait qu'initialiser l'objet de type markov
        """

        # Initialisation des champs nécessaires aux fonctions fournies
        self.keep_ponc = True
        self.rep_aut = os.getcwd()
        self.auteurs = []
        self.ngram = 1
        self.folders = []
        self.dict = dict()

        return

    # Ajouter les structures de données et les fonctions nécessaires à l'analyse des textes,
    #   la production de textes aléatoires, la détection d'oeuvres inconnues,
    #   l'identification des n-ièmes mots les plus fréquents
    #
    # If faut coder les fonctions find_author(), gen_text(), get_nth_element() et analyse()
    # La fonction analyse() est appelée en premier par testmarkov.py
    # Ensuite, selon ce qui est demandé, les fonctions find_author(), gen_text() ou get_nth_element() sont appelées

    def find_author(self, oeuvre):
        """Après analyse des textes d'auteurs connus, retourner la liste d'auteurs
            et le niveau de proximité (un nombre entre 0 et 1) de l'oeuvre inconnue avec les écrits de
            chacun d'entre eux

        Args:
            oeuvre (string): Nom du fichier contenant l'oeuvre d'un auteur inconnu

        Returns:
            resultats (Liste[(string,float)]) : Liste de tuples (auteurs, niveau de proximité), où la proximité est
                                                un nombre entre 0 et 1)
        """

        resultats = [("balzac", 0.1234), ("voltaire", 0.1123)]   # Exemple du format des sorties

        # Ajouter votre code pour déterminer la proximité du fichier passé en paramètre avec chacun des auteurs
        # Retourner la liste des auteurs, chacun avec sa proximité au fichier inconnu
        # Plus la proximité est grande, plus proche l'oeuvre inconnue est des autres écrits d'un auteur
        #   Le produit scalaire entre le vecteur représentant les oeuvres d'un auteur
        #       et celui associé au texte inconnu pourrait s'avérer intéressant...
        #   Le produit scalaire devrait être normalisé avec la taille du vecteur associé au texte inconnu:
        #   proximité = (A . B) / (|A| |B|)   où A est le vecteur du texte inconnu et B est celui d'un auteur,
        #           . est le produit scalaire, et |X| est la norme (longueur) du vecteur X

        return resultats

    def gen_text(self, auteur, taille, textname):
        """Après analyse des textes d'auteurs connus, produire un texte selon des statistiques d'un auteur

        Args:
            auteur (string): Nom de l'auteur à utiliser
            taille (int): Taille du texte à générer
            textname (string): Nom du fichier texte à générer.

        Returns:
            void : ne retourne rien, le texte produit doit être écrit dans le fichier "textname"
        """

        return

    def get_nth_element(self, auteur, n):
        """Après analyse des textes d'auteurs connus, retourner le n-ième plus fréquent n-gramme de l'auteur indiqué

        Args:
            auteur (string): Nom de l'auteur à utiliser
            n (int): Indice du n-gramme à retourner

        Returns:
            ngram (List[Liste[string]]) : Liste de liste de mots composant le n-gramme recherché (il est possible qu'il
                                          y ait plus d'un n-gramme au même rang)
        """
        ngram = [['un', 'roman']]   # Exemple du format de sortie d'un bigramme
        sorted_table = sorted(self.auteurs[auteur].items(), key=lambda item: item[1], reverse=True)
        return sorted_table[n]

    def analyze(self):
        """Fait l'analyse des textes fournis, en traitant chaque oeuvre de chaque auteur

        Returns:
            void : ne retourne rien, toute l'information extraite est conservée dans des strutures internes
        """

        # pour le/les auteurs
        for subfolder in self.folders:
            self.dict[subfolder] = dict()
            # pour chaque texte
            for filename in os.listdir(self.rep_aut + '/' + subfolder):
                with open(os.path.join(self.rep_aut + '/' + subfolder + '/', filename), 'r', encoding="utf-8") as file:
                    word = ""
                    word_arr = []
                    ngram = 0
                    for line in file:
                        line = line.lower()
                        for char in line:
                            if char == '\n' or char == '\xa0' or char in self.PONC:
                                char = ' '
                            if char != ' ':
                                word += char
                            # si le mot est trop petit, mot suivant
                            elif len(word) < 3 and word != [0-99]:
                                word = ""
                            elif word != "":
                                ngram += 1
                                if ngram == self.ngram:
                                    if self.ngram == 1:
                                        if word in self.dict[subfolder]:
                                            self.dict[subfolder][word] += 1
                                        else:
                                            self.dict[subfolder][word] = 1
                                    else:
                                        word_arr.append(word)
                                        if tuple(word_arr) in self.dict[subfolder]:
                                            self.dict[subfolder][tuple(word_arr)] += 1
                                        else:
                                            self.dict[subfolder][tuple(word_arr)] = 1
                                    word = ""
                                    word_arr.pop(0)
                                    ngram -= 1
                                else:
                                    word_arr.append(word)
                                    word = ""
            print(subfolder + " : " + str(self.dict[subfolder]["comme", "moi"]))

        return


# Main
# Arguments de la ligne de commande
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', required=True, help="répertoire dans lequel se trouvent les textes des auteurs")
    parser.add_argument('-a', help="auteur sur lequel portera l'analyse")
    parser.add_argument('-A',action='store_true' , help="effectuer l'analyse sur tous les auteurs")
    parser.add_argument('-f', help="fichier de texte à comparer avec les fréquences des fichiers de l’auteur choisi")
    parser.add_argument('-m', required=True, help="taille des n-grammes")
    parser.add_argument('-F', help="afficher le n-ieme n-gramme le plus fréquent")
    parser.add_argument('-G', help="générer un ou plusieurs textes aléatoires selon les paramètres entrés")
    args = parser.parse_args()

    m = markov()

    if args.d:
        m.set_aut_dir(args.d)
    if args.a:
        m.folders = [args.a]
    if args.A:
        m.folders = os.listdir(m.rep_aut)
    if args.m:
        m.set_ngram(int(args.m))
    else:
        args.m = False
    if not(bool(args.a) ^ bool(args.A)):
        parser.error("Erreur d'attribut. Ajouter l'un des deux paramètres suivants : -a, -A")

    m.analyze()
