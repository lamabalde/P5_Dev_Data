import re
from datetime import datetime 
def numValid(numero):
    for caractere in numero :
        if not ((caractere>='A' and caractere<='Z') or (caractere in ['0','1','2','3','4','5','6','7','8','9'])):
            return False
        elif len(numero)!=7:
            return False    
    return True 
def vide(vides):
    if vides=='':
        return False
    return True

def prenomValid(prenom):
    if not ((prenom[0]>='A' and prenom[0]<='Z') or (prenom[0]>='a' and prenom[0]<='z')):
        return False
    a=0    
    for i in prenom:
        if (i>='A' and i>='Z') or (i>'a' and i<'z'):
              a+=1
    if a<3:
        return False            
    return True 

def nomValid(nom):
    if len(nom)<3:
        return False
    if not ((nom[0]>='A' and nom[0]<='Z') or (nom[0]>='a' and nom[0]<='z')):
        return False
              
    return True 

def classeValid(classe):
    if not (classe[0]>='3' and classe[0]<='6'):
        return False
    if classe[-1]!='A' and classe[-1]!='B' and classe[-1]!='a' and classe[-1]!='b':
         return False
    return True 

def formatClasse(classe):
    return classe[0]+classe[-1]

def convert_date_format(date_string):
    date1=""
    for i in date_string:
        if i in [' ','-',':',';','.']:
            date1+='/'
            continue
        date1+=i
    return date1 

def dateValid(k):
    try:
        k=datetime.strptime(k, "%d/%m/%y").date()
        return True
    except ValueError:
        return False     
def note1(note):
    #tab="Math[18|17:10]#Francais[5|13|9:14]#Anglais[12,5|10:14]#PC[17:9]#SVT[12|19|15|11:12]#HG[16:18]" 
    note=note.replace(',', '.')
    note1=note.split('#')
    tables=[]
    pat=re.compile(r'\w+')
    for j in note1:
        mat=re.findall(pat,j)
        tables.append(mat)
    return tables
def note2(tab):
    for tab1 in tab:
        if len(tab1)<2:
            return False
    return True  
def note3(tables):               
    b=0
    c=0
    for i in range(len(tables)):
        for j in range(len(tables[i])-1):
            if tables[i][j]!=tables[i][0]:
                b+=float(tables[i][j])
                c+=1
        moy=((b/2)+2*float(tables[i][-1]))/3 
        moy=format(moy, '.2f')       
        tables[i].append(moy)
        b=0 
        c=0  
    return tables 

def affichage(tab):
    for tab1 in tab :
        for tab2 in tab1:
            print(tab2, end="  ")
        print()
def affichagePar5(tab):
    for j in range(5) :
        for tab1 in tab[j]:
            print(tab1, end="  ")
        print()

def rechercheParNum(tableau,num,i):
    for sous_liste in tableau:
        if sous_liste[i] == num:
            return sous_liste 
def affichageParNum(tab):
    for tab1 in tab:
        print(tab1, end="  ")
    print()
def paginationPar5(tab,i=5):
    # for i in range(0,len(tab),i):
    #     for tab1 in tab[i]:
    #         print(tab1, end=" ") 
    #     print('\n')
    print ({tab[i:i+5] for i in range(0, len(tab), 4)})