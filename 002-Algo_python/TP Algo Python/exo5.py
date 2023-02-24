a=True
while a:
    ordre=int(input("Entrez l'ordre de la matrice et doit etre superieur a 5 : "))
    if ordre >5:
        a=False
print("Menu de couleur") 
print(" Bleu") 
print(" Rouge") 
couleur=""
c=True
while c==True:
    couleur=input("saisissez une couleur : ")
    if couleur=="Bleu" or couleur=="Rouge":
        c=False
position=""
print("Menu de position")       
print("Haut") 
print("Bas") 
d=True
while d==True:
    position=input("Choississez une position : ")
    if position=="Haut" or position=="Bas":
        d=False
matrice = []
for i in range(ordre):
    ligne =[]
    for j in range(ordre):
        if i < j and position == "Haut":
            ligne.append(couleur)
        elif i > j and position == "Bas":
             ligne.append(couleur)
        else:
              ligne.append("blanc")
    matrice.append(ligne)
for i in matrice:
    for e in i:
        print(e, end=" ")
    print('\n')    
