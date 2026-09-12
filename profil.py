prenom = "Serigne Thierno BOUSSO"
age = 20
moyenne = 15.5
etudiant = True

print(f"Bonjour, je m'appelle {prenom}, j'ai {age} ans, ma moyenne est de {moyenne} et je suis étudiant: {etudiant}")
if moyenne >= 16:
    print("Mention : Très Bien")
elif moyenne >= 14:
    print("Mention : Bien")
elif moyenne >= 10:
    print("Mention : Passable")
else:
    print("L'année est à reprendre")