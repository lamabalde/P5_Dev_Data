def controleNote(note):
    if note>20 and note<0:
        return False
    else :
        return True

def verifyNum(c):
    if len(c)!=9:
        return False
    elif c[0]=='7' and (c[1]=='8' or c[1]=='7' or c[1]=='5' or c[1]=='0' or c[1]=='6'):
        return True
    else:
        return False

                #AFFICHAGE
def Affichage(tab_g):
    tab=["Prenom","Nom","Telephone","Classe","Dev","proj","exam", "moyen"]
    for i in range(130):
        print("-", end="")
    print()    
    for i in tab:
        print ( i ,end=(15-len(i))*' '+ '|')
    print()  
    for i in range(130):
        print("-", end="")
    print()      
    for j in tab_g:
            for k in j:
                print(k ,end=(15-len(k))*' '+'|')
            print("\n")         
    print()      
    for i in range(130):
            print("-", end="")
    print()    

          #MODIFICATION DE NOte
def modification(tab,c):
    h=0         
    for i in range (len(tab)):
        for j in tab[i]:
            if j == c:
                h=i
                break
    return h        
   # ALGORITHME DE TRI
def triMoy(tab):
    for i in range(len(tab)-1):
        for j in range(i+1, len(tab)):
            if tab[i][7] < tab[j][7]:
                tab[i],tab[j]=tab[j],tab[i]
    return tab 


def recherche(tableau,nom,i):
    for sous_liste in tableau:
        if sous_liste[i] == nom:
            print(sous_liste)          