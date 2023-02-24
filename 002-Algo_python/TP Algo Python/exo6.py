# saisir l’ordre d’une matrice carrée
# Un Menu de choix pour la position de la couleur(ADDP;EDDP;SDP;ADDS;EDDS;SDS)(en Initialiser un tableau de positions)
# Un Menu de choix ayant comme options des couleurs (en Initialiser un tableau de couleurs)
#menu de position
c=True
while c:
    ordre=int(input("Entrez l'ordre de la matrice et doit etre superieur a 4 : "))
    if ordre >4:
        c=False
a=True       
while a:
    print("Faites votre choix de position entre O et 6")
    choix_posi=["0 ADDP :au-dessus de la diagonale principale",
    "1 EDDP :au-dessus de la diagonale principale",
    "2 SDP : sur la diagonale principale",
    "3 ADDS : au-dessus de la diagonale secondaire.",
    "4 EDDS : en dessous de la diagonale secondaire",
    "5 SDS : sur la diagonale secondaire"]
    for i in choix_posi:
        print(i)
    position=int(input())  
    if position>=0 and position<=5:
        a=False    
#menu de couleur 
b=True
while b:
    print("Faite votre choic de couleur 1 ou 2")          
    choix_couleur=["vert", "rouge"]  
    for i in choix_couleur:
        print(i)  
    indice_couleur=int(input())
    couleur=choix_couleur[indice_couleur]
    if indice_couleur>=0 and indice_couleur<=2:
        b=False 

matrice = []
if position < 3:
#principal diagonal
    for i in range(ordre):
        ligne =[]
        for j in range(ordre):
            if i < j and position==0 :
                ligne.append(couleur)
            elif i > j and position == 1:
                ligne.append(couleur)
            elif i==j and position==2:
                ligne.append(couleur)
            else:
                ligne.append("blanc")
        matrice.append(ligne)
    for i in matrice:
        for e in i:
            print(e, end=" ")
        print('\n')   
else:
    a=ordre
    for i in range(ordre):
        ligne =[]
        for j in range(ordre):
            if j > a-1 and position == 3:
                ligne.append(couleur)
            elif j< a-1 and position==4:
                ligne.append(couleur)
            elif i+j==ordre-1 and position==5: 
                ligne.append(couleur)
            else:
                ligne.append("blanc")       
        matrice.append(ligne)
        a-=1
    for i in matrice:
        for e in i:
            print(e, end=" ")
        print('\n')    
        
