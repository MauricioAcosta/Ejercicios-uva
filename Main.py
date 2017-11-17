from sys import stdin
import math

def logic(N):
    S = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if N % i == 0 and N % j == 0:
                    S+=math.gcd(i,j)
        
    return S


n = int(stdin.readline())

keys = []
values = []

for i in range(n):
    N = int(stdin.readline())
    keys.append(N)
    values.append(logic(N))

for i in range(n):
    print("Case")

for i in range(n):
    print(str(keys[i]) + ":" + str(values[i]))
