from sys import stdin
while True:
    lectura=stdin.readline().split()
    if not lectura:
        break
    cadena=' '.join(lectura)
    newcadena=[]
    for caracter in cadena:
        newcadena.append(chr(ord(caracter)-7))
    print ("".join(newcadena))
