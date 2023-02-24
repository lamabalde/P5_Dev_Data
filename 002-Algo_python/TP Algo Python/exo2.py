chaine=input("Donnez une phrase : ")
x=len(chaine)
chaines=""
for i in range(0,x):
    if (chaine[i-1]==' ' and chaine[i]==' '):
        continue
    else:
        chaines=chaines + chaine[i]

print(chaines)           