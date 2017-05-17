n=int(input())
lista=[]
lista.append(n)
bandera=True
while bandera:
    if n==1:
        bandera=False
    elif n%2!=0:
        n=3*n+1
        lista.append(n)
    elif n%2==0:
        n=n/2
        lista.append(n)
print(lista)
print(len(lista))
