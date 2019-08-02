from sys import stdin

num = stdin.readline()

def fibo(num):
    listanum=[1,1]
    for i in range(num):
        aux=listanum[i+1]+listanum[i]
        listanum.append(aux)
    return listanum

numerosfibo=fibo(int(num))
#print(numerosfibo)
print(sum(numerosfibo[0:int(num)]))