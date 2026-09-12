notes = [12.5, 15, 8.5, 10, 14]
somme = 0
for note in notes:
    somme += note
moyenne = somme / len(notes)
print(f"La moyenne des notes est : {moyenne}")