from sys import stdin
while True:
    lectura=stdin.readline().split()
    if not lectura:
        break
    cadena=' '.join(lectura)
    newcadena=[]
    for i in range(len(cadena)):
        newcadena.append(chr(ord(cadena[i])-7))
    print ("".join(newcadena))
