from sys import stdin
lectura=stdin.read().splitlines()
listaimpar=[]
listapar=[]
for numeros in lectura:
    v1=True
    v2=True
    numero=numeros.split()
    i=numero[0]
    j=numero[1]
    while v1:
        if int(numero[0])==1:
            listaimpar.append(int(numero[0]))
            ciclo_lenght+=1
            break
        elif int(numero[0])%2!=0:
            numero[0]=3*int(numero[0])+1
            listaimpar.append(int(numero[0]))
            ciclo_lenght+=1
        elif int(numero[0])%2==0:
            numero[0]=int(numero[0])/2
            listapar.append()
            ciclo_lenght+=1
    while v2:
        if int(numero[1])==1:
            listaimpar.append(int(numero[1]))
            ciclo_lenght+=1
            break
        elif int(numero[1])%2!=0:
            numero[1]=3*int(numero[1])+1
            listaimpar.append(int(numero[1]))
            ciclo_lenght+=1
        elif int(int(numero[1]))%2==0:
            numero[1]=int(numero[1])/2
            listapar.append(int(numero[1]))
            ciclo_lenght+=1
    print(int(i),"",int(j),"",ciclo_lenght)
