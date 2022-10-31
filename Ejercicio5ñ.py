frase=input("Ingrese la frase:")
print("Vocales dentro de la frase: ")
for x in "aeiou":
    if x in frase:
        print(x)