from fonc import *
from datetime import datetime 
import csv
import json
import xml.etree.ElementTree as ET
 
data = []
DATA ='Donnees_Projet_Python_DataC5.csv'
with open(DATA,newline='') as f2:
    readcsv = csv.reader(f2)
    for row in readcsv:
        data.append(row)
# print(data)
with open("data.json", "w") as f:
    json.dump(data, f)

    f.close()

root = ET.Element("liste2")

for item in data:
    element = ET.Element("item")
    element.text = str(item)
    root.append(element)

tree = ET.ElementTree(root)

with open("liste2.xml", "wb") as f:
    tree.write(f)

    f.close()

tab_invalid=[]
tab_valid=[]
# for datas in data:
#     for data1 in datas:
#         if vide(data1)==False:
#             tab_invalid.append(datas)

for i in range(len(data)):
    verify=True
    for j in range(len(data[i])):
        data[i][j]=''.join(data[i][j].split(' '))
        data[i][4]=convert_date_format(data[i][4])
        if numValid(data[i][1])==False:
            tab_invalid.append([data[i]])
            verify=False    
        elif nomValid(data[i][2])==False:
            tab_invalid.append([data[i]])
            verify=False 
        elif prenomValid(data[i][3])==False:
            tab_invalid.append([data[i]])
            verify=False
        elif classeValid(data[i][5])==False:
            data[i][5]=formatClasse(data[i][5])
            tab_invalid.append([data[i]]) 
            verify=False
        elif dateValid(data[i][4])==False:
            tab_invalid.append([data[i]])
            verify=False              
    if verify:
        data[i][6]=note1(data[i][6])
        if note2(data[i][6]):
            data[i][5]=formatClasse(data[i][5])
            data[i][6]=note3(data[i][6])
            tab_valid.append(data[i])
        else:
              tab_invalid.append([data[i]]) 

with open("tabValide.json", "w") as f:
    json.dump(tab_valid, f)
    f.close()

with open("tabInvalide.json", "w") as f:
    json.dump(tab_invalid, f)
    f.close() 
root = ET.Element("liste3")
for item in tab_valid:
    element = ET.Element("item")
    element.text = str(item)
    root.append(element)

tree = ET.ElementTree(root)

with open("liste3.xml", "wb") as f:
    tree.write(f)

    f.close()  
root = ET.Element("liste4")     
for item in tab_invalid:
    element = ET.Element("item")
    element.text = str(item)
    root.append(element)

tree = ET.ElementTree(root)

with open("liste4.xml", "wb") as f:
    tree.write(f)

    f.close()          
# # 2 CREATION DE MENU

# print("          MENU PRINCIPAL")
# print(tab_valid)

# print("         1_Afficher les informations (Valide ou invalide)")
# print("         2_Afficher une information (par son numéro)")
# print("         3_Afficher les cinq premiers")
# print("         4_Ajouter une information en vérifiant la validité des informations données")
# print("         5_Modifier une information invalide")
# choix=input("Faire votre choix :  ")
# if choix =='1':
#     choix1=input("   Affichage tableau(valide ou invalide) :  ")
#     if choix1=="valide":
#         affichage(tab_valid)
#     elif choix1=="invalide":
#         affichage(tab_invalid)
# if choix =='2':
#     num=input("entrez le numero : ")
#     tab_num=rechercheParNum(tab_valid,num,1)
#     affichageParNum(tab_num)
# if choix =='3':
#     afficahge1(tab_valid)
# if choix =='4':
#     pass
# if choix =='5':
#     pass

# #l’affichage se fera par pagination
# print("afficgage par pagination")
# pagi=input("pagination par 5 (oui ou non): ")
# if pagi=="oui":
#     paginationPar5(tab_valid)
# else:
#     a=True
#     while a:
#         print("entrez votre pagination", 0, "jusqua", len(tab_valid))
#         c=input()
#         if c.isnumeric():
#             a=False
#     c=int(c)
    #paginationPar5(tab_valid,c)


