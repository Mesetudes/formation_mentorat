def calculer_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme += note
    return somme / len(liste_notes)
etudiant = {
    "prenom": "Serigne Thierno",
    "nom": "BOUSSO",
    "notes": [12.5, 15, 8.5, 10, 14]
}
moyenne_etudiant = calculer_moyenne(etudiant["notes"])
print(f"La moyenne des notes de {etudiant['prenom']} {etudiant['nom']} est : {moyenne_etudiant}")