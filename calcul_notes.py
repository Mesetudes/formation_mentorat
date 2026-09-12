# 1. Définition des fonctions en haut
def calculer_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme += note
    return somme / len(liste_notes)

# 2. Code principal en bas
mes_notes = [12.5, 15, 8.5, 10, 14]
resultat_moyenne = calculer_moyenne(mes_notes)
print(f"La moyenne des notes est : {resultat_moyenne}")