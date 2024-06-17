import random

def gllistaaleatoria():
    l=[]
    for e in range(3):
        l.append(random.randint(1,9))
    return l
    
def llegir_llista():
    l=[]
    for e in range(3):
        a=int(input("Introdueix el número: "))
        l.append(a)
    return l

def comparar (l,m):
    a=[0,0,0]
    for i in range(3):
        if l[i]==m[i]:
            a[i]=10
    if a[0]==10 and a[1]==10 and a[2]==10:
        print("Enhorabona, ho has encertat tot! ")
        return 0
    for i in range(3):
        if a[i]==0:
            if m[i] in l:
                a[i]=5
    for i in range(3):
        if a[i]==10:
            print("L'element {} és correcte".format(m[i]))
        elif a[i]==5:
            print("L'element {} és correcte, però no és el mateix".format(m[i]))
        else:
            print("L'element {} no és correcte".format(m[i]))

def pex1():
    op=1
    l=gllistaaleatoria()
    while op!=0:
        m = llegir_llista()
        op = comparar(l,m)


