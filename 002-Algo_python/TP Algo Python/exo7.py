dic= { 'a': '2','b': '22','c': '222','d': '3','e': '33','f': '333','g': '4',
'h': '44','i': '444','j': '5','k': '55','l': '555','m': '6','n': '66','o': '666',
'p': '7','q': '77','r': '777','s': '7777','t': '8','u': '88','v': '888','w': '9',
'x': '99','y': '999','z': '9999','0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'j', 
'7':'h', '8':'i', '9':'j', ' ' : '00','A': '2','B': '22','C': '222','D': '3','E': '33','F': '333','G': '4',
'H': '44','I': '444','J': '5','K': '55','L': '555','M': '6','N': '66','O': '666',
'P': '7','Q': '77','R': '777','S': '7777','T': '8','U': '88','V': '888','W': '9',
'X': '99','Y': '999','Z': '9999'}
phrase=input("Entrez la phrase : ")
tab=[]
for i in phrase:
    for j in dic:
        if j==i:
            tab.append(dic[i])
        elif i not in dic:
              tab.append(i)
              break         
tab1=[]
for i in range(1,len(tab)):
    a=tab[i]
    b=tab[i-1]
    if a[-1]==b[0]:
        tab1.append(tab[i-1])
        tab1.append('0')
    else:
        tab1.append(tab[i-1]) 
tab1.append(tab[len(tab)-1])           
for i in tab1:
    print(i, end="")
print()           

    
