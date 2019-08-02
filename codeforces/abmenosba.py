from sys import stdin
numbers=stdin.readline().split()
numbers=[int(x) for x in numbers]
print((numbers[0]**numbers[1])-(numbers[1]**numbers[0]))