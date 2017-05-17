n=int(input())
lista=[]
lista.append(n)
bandera=True
while n!=1:
    if n%2!=0:
        n=3*n+1
        lista.append(n)
    else:
        n=n/2
        lista.append(n)
print(lista)
print(len(lista))
