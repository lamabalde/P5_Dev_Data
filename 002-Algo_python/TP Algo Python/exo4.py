def verifyNum(c):
    if len(c)!=9:
        return False
    elif c[0]=='7' and (c[1]=='8' or c[1]=='7' or c[1]=='5' or c[1]=='0' or c[1]=='6'):
        return True
    else:
        return False

def operateur(c):
    a=0
    b=0
    c=0
    if c[1]=='8' or c[1]=='7':
        a+=1
    elif c[1]=='6':
        b+=1
    elif c[1]=='5':
        c+=1
    print(a, "Orange(s)")
    print(b,"Free(s)")
    print(c, "Pro mobile(s)")                
# num=input("Entrez N numero chaque numero doit etre separer par / ")
num="23124354#776612045#23323445#34335678765446#765543432#755512312#704320099#785554433"
list_tab=[]
x=len(num)
ph=""
list_num=['1','2','2','3','4','5','6','7','8', '9', '0',' ']
i=0
a=True
while a==True:
    while num[i] in list_num:
        ph=ph + num[i]
        i+=1
        if i==x-1:
           a=False
           break
    if len(ph)>0:       
        list_tab.append(ph)
    i+=1
    ph=""
    if i==x-1:
           a=False
print(list_tab)
valid=[]
No_valid=[]
print("================")
for e in list_tab:
    if verifyNum(e)==True:
        valid.append(e)
    else:
        No_valid.append(e)

tab_G=[valid,No_valid]
print(tab_G)