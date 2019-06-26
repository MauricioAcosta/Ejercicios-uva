from sys import stdin

num=int(input())
count=0
for _ in range(num):
    x=input()
    if x=='X++' or x=='++X' or x=='+X+':
        count+=1
    else:
        count-=1
print(count)
