#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames

def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    dictionnaire= dict()
    for i in range(len(some_list)):
        dictionnaire[some_list[i]] = i
        #print(dictionnaire)

    return dictionnaire


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    liste = list()
    for color in colors:
        if color in cnames:
            liste.append((color, cnames[color]))
        else:
            print(f"la couleur {color} n'existe pas dans cnames")
    return liste


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    liste = [number for number in range(10000) if number < 15 or number > 350]

    return liste


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    dictionnaire = dict()
    sum = 0
    for cle, valeur in model_dict.items():
        for nbr in valeur:
            sum += (nbr[0] - nbr[1])**2
        resultat = sum /len(valeur)
        dictionnaire[cle] = resultat

    return dictionnaire


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
