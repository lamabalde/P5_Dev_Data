from fonc import *
#Enregistrement de l'etudiant
tab=[]
prenom=[]
a= True
while a:
    p=input("Entrez le prenom : ")
    prenom.append(p)

    n=input("Entrez le nom : ")
    prenom.append(n)

    c=input("Entrez le classe : ")
    prenom.append(c)

    t=input("Entrez le telephone : ")
    prenom.append(t)
    dev=True
    while dev:
        d=input("Entrez le devoir : ")
        a=int(d)
        if controleNote(a)==False:
            dev=False
    prenom.append(d)
    dev=True
    while dev:
        p=input("Entrez le projet : ")
        b=int(p)
        if controleNote(a)==False:
            dev=False
    prenom.append(p)
    dev=True
    while dev:
        e=input("Entrez la note d'exam : ")
        c=int(e)
        if controleNote(c)==False:
            dev=False
    prenom.append(e)
    d=(a+b+c)/3
    prenom.append(d)
    tab.append(prenom)
    prenom=[]
    print("Voulez vous enregistrer un autre etudiant ")
    ch=input(" Si oui taper 1 ")
    if ch!='1':
        a=False
Affichage(tab)      

#MENU DE CHOIX
# tab=[
#     ["mamdou","balde","775544335","licence","12","15","17","12"],
#     ["mamdou","balde","775544335","licence","12","15","17","13"],
#     ["mamdou","balde","775544335","licence","12","15","17","14"],
#     ["mamdou","ba","775544335","licence","12","15","17","15"]
# ]

a =True
while(a):
    print("          MENU PRINCIPAL")

    print("   ====================================")
    print("         1_AFFICHER TOUT          ")
    print("   ====================================")
    print("         2_Trier et afficher")
    print("   ====================================")
    print("         3_Rechercher selon un critère")
    print("   ====================================")
    print("         4_Modification de note ")
    print("   ====================================")
    print("         5_Sortir")
    print("   ====================================")
    choix=input("Choisir un numero : ")
    if choix== '1':
        Affichage(tab)
    elif choix=='2':
        tab1=triMoy(tab)
        Affichage(tab1)
    elif choix=='3':
         print("1_recherche par prenom")
         print("2_recherche par nom")
         print("3_recherche par classe")
         print("4_recherche par telephone")
         ret=input("faite votre choix : ")
         if ret=='1':
            i=0
         elif ret=='2':
            i=1
         elif ret=='3':
            i=2
         elif ret=='4':
            i=3 
         ret2=input(" ")       
         recherche(tab,ret2,i)            
    elif choix=='4':
        c=input("Entrez le notre de telephone")
        a=modification(tab,c)
        tab[c][4]=input("entrez la note dev")
        tab[c][5]=input("entrez la note proj")
        tab[c][6]=input("entrez la note exam")
        tab[c][7]=(int(tab[c][4])+int(tab[c][5])+int(tab[c][6]))/3
    elif choix=='5':
        print("MERCI a la prochaine")
        a=False       
        exit()

