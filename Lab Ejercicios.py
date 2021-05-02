#Ejercicio1 / Programa para comprobar: si es positivo o negativo un número
num = int(input("Ingrese el número para comprobar si es positivo o negativo: "))
if num  > 0:
    print("Es un número positivo")
else:
    print("Es un número negativo")
#Ejercicio2 Programa para: Hallarle el cuadrado a cualquier número
num = int(input("Ingrese un número para hallarle el cuadrado"))
cuadro = (num**2)
print("El cuadrado del número digitado es: ", cuadro)
#Ejercicio3 Programa para: Hallar el valor del precio añadido al iva de un articulo.
precio = int(input("Ingrese el valor de venta: "))
iva = precio * 0.19
print("El valor de la venta es", precio, "El valor del IVA es", iva,
      "El valor de la venta mas IVA es", precio + (precio * 0.19))
#Ejercicio4 Programa para: Hallar el area y el perimetro de un circulo a partir del radio.
r = float(input("Ingrese el radio del círculo: "))
print("El area del círculo es", math.pi * (r**2), "El perimetro del círculo es", 2 * math.pi * r)
#Ejercicio5 Programa para: Pasar de segundos a horas
segs = int(input("Ingrese los segundos a transformar: "))
print(segs, "segundos equivalen a", segs / 3600, "horas")
#Ejercicio6 Programa para: Pasar de segundos a minutos
segundos = int(input("Ingrese los segundos a transformar: "))
print(segundos, "segundos equivalen a", segundos / 60, "minutos")
#Ejercicio7 Programa para: hallar diferentes variantes de tiempo a partir de segundos
segz = int(input("Ingrese un tiempo en segundos: "))
hora = segz / 3600
segundos = segz % 3600
minutos = segundos / 60
segundos2 = segz % 60
print("la hora es:", int(hora), int(minutos), segundos2)
#Ejercicio8 Programa para: pasar de numero entero a decimal
num = int(input("Ingrese un número entero: "))
print("El número ingresado es", float(num), "en decimal.")
#Ejercicio9 Programa para: Hallar el promedio de un estudiante.
p1 = 0.15
p2 = 0.15
p3 = 0.20
p4 = 0.20
p5 = 0.30
count = 1
while True:
    i = 0
    if count == 1:
        NOTA1 = float(input("Digite la primera nota: "))
        i = NOTA1
    if count == 2:
        NOTA2 = float(input("Digite la segunda nota: "))
        i = NOTA2
    if count == 3:
        NOTA3 = float(input("Digite la tercera nota: "))
        i = NOTA3
    if count == 4:
        NOTA4 = float(input("Digite la cuarta nota: "))
        i = NOTA4
    if count == 5:
        NOTA5 = float(input("Digite la quinta nota: "))
        i = NOTA5
    if i > 0 and i <= 5:
        count = count + 1
    if count == 6:
        break
total = (NOTA1 * p1) + (NOTA2 * p2) + (NOTA3 * p3) + (NOTA4 * p4) + (NOTA5 * p5)
print("La nota final es: ", total)
if total>=3:
    print("Aprobo")
else:
    print("Reprobo")
#Ejericicio10 Programa para: Hallar la cantidad de numeros digitados, la suma total y el promedio total.
numero= 0
total= 0
print("Digite un valor númerico (Digite 0 para dar el resultado final): ")
datos = int(input())
while datos != 0:
    numero = numero + datos
    total = total + 1
    print("Digite un valor númerico (Digite 0 para dar el resultado final): ")
    datos = int(input())

suma = int(numero)
promedio= float(suma/total)
print("La cantidad de valores numericos digitados fue: ", total)
print("La suma total de los valores numeros digitados es: ", suma)
print("El promedio total es =", promedio)
#Ejercicio11 Programa para: Otra forma de realizar el Ejercicio9
n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))
n4 = float(input("Ingrese la nota 4: "))
n5 = float(input("Ingrese la nota 5: "))
print("La nota final es: ", n1 * 0.15 + n2 * 0.20 + n3 * 0.15 + n4 * 0.30 + n5 * 0.20)
#Ejercicio12 Programa para: Mostrar la tablas de multiplicar de un numero pedido.
num = int(input("Ingrese un número entero: "))
def imprimir_tabla(numero):
    LIMITE = 10
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1
imprimir_tabla(num)
#Ejercicio13 Programa para: Encontrar el numero mayor y el menor en un listado.
mayor= -float("inf")
menor = float("inf")
while True:
    n = float(input("Digite un valor númerico (0 para imprimir el resultado: "))
    if n == 0:
        break

    mayor = max(n, mayor)
    menor = min(n, menor)

print("Mayor valor númerico: ", mayor)
print("Menor valor númerico: ", menor)
#Ejercicio14 Programa para: Hallar el area de un hexágono.
P = float(input("Ingrese el perimetro de su hexágono: "))
A= float(input("Ingrese el apotema de su hexágono: "))
print("El área de su hexágono es: ",(P*A)/2)
#Ejercicio15 Programa para: Conseguir el promedio de 3 numeros ingresados.
n1= float(input("Ingrese el primer número: "))
n2= float(input("Ingrese el segundo número: "))
n3= float(input("Ingrese el tercer número: "))
print("El promedio de los tres número es: ",(n1+n2+n3)/3)
#Ejercicio16 Programa para: un sistema numerico.
decimal= int(input("Ingrese el valor decimal a convertir: "))
# DECIMAL TO ...
# binario
numbin = str(bin(decimal))
print("binario = " + numbin)
# octal
numocta = str(oct(decimal))
print("octal = " + numocta)
# hexadecimal
numhexa = str(hex(decimal))
print("hexadecimal = " + numhexa)
#HEX TO DECIMAL
num= int(numhexa, 16)
print(num)
#OCT TO DECIMAL
num= int(numocta, 8)
print(num)
#BIN TO DECIMAL
num= int(numbin, 2)
print(num)
#Ejercicio17 Programa para: Potenciar libremente un número
num = int(input("Ingrese un número"))
num1 = int(input("Ingrese a que quiere potenciar el número"))
Cuad = (num**num1)
print("El cuadrado del número dado es: ", Cuad)
#Ejercicio18 Programa para: Decidir si es par o impar un número
numero= int(input("Ingrese el número:"))
if numero % 2 == 0:
    if numero>10:
        print("El número es par y > 10")
    else:
        print("El número es par y <=10")
else:
    print("El número es impar")
#Ejercicio19 Programa para: verificar si los numeros ingresados disminuyen o aumentan.
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))
if num2 > num1 and num3 > num2:
    print("Los números se incrementan.")
elif num2 < num1 and num3 < num2:
    print("Los números disminuyen.")
else:
    print("Los números no se incrementan ni se disminuyen")
#Ejercicio20 Programa para: Hallar la suma y el promedio de 5 numeros digitados
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese otro número: "))
n4 = int(input("Ingrese otro número: "))
n5 = int(input("Ingrese otro número: "))
print("La suma de los números ingresados es:", n1 + n2 + n3 + n4 + n5)
print("El promedio de los números ingresados es:", (n1 + n2 + n3 + n4 + n5) / 5)
#Ejercicio21 Programa para: Comparar si es menor o mayor el resultado de la suma.
N1 = int(input("Ingrese un número entero: "))
N2 = int(input("Ingrese otro número: "))
N3 = int(input("Ingrese otro número: "))
suma = N1 + N2
if suma > N3:
    print("La suma de los dos primeros números es mayor que el tercer número ingresado.")
else:
    print("La suma de los dos primeros números es menor que el tercer número ingresado.")
#Ejercicio22 Programa para: Calcular el precio atraves de los km recorridos
dist = int(input("Ingrese la distancia a recorrer (en kilómetros): "))
dias = int(input("Ingrese los días de estancia: "))
pasaje = 5000 * dist
if dist > 1000 and dias > 7:
    print(pasaje - (pasaje * 0.15))
else:
    print("El precio del pasaje es", pasaje)
#Ejercicio23 Programa para:
nume = int(input("Ingrese un número: "))
if nume >= 10:
    print("La tercera parte del número:", nume * 3)
else:
    print("La cuarta parte del número:", nume * 4)
#Ejercicio24 Programa para: replica de un inicio de sesion (inspirado de don google)
user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if user.startswith("admin") and password.startswith("12345678"):
    print("Inicio de sesión completado")
else:
    print("Inicio de sesión fallido (usuario o contraseña incorrectos).")
#Ejercicio25 Programa para: demostrar si un número es positivo o negativo.
def positivo_negativo(numero):
    negativo = "-"
    for n in numero:
        if n == negativo:
            return True
num = str(input("Ingresar un número positivo o negativo: "))
if positivo_negativo(num):
    print("El número es negativo.")
else:
    print("El número es positivo.")
#Ejercicio26 Programa para: dar salida a numeros pares.
print("Los diez primeros números naturales pares son igual a:")
for x in range(0, 11):
    if x % 2 == 0:
        print(x, "", end="")
#Ejercicio27 Programa para: Aplicar un descuento a partir de un precio mayor a $250.000 (inspirado de don google)
compra = float(input("Ingrese el valor de su compra, si es mayor a $250.000, se le aplica un descuento del 5%: "))
iva = compra*0.19
total = compra+iva
if compra > 250000:
    desc = total*0.5
    total = total-desc
    print("El valor total de su compra con descuento, sumado el IVA es:{}".format(total))
else:
    print("El valor total de su compra sin descuento, sumado el IVA, es:{}".format(total))
#Ejercicio28 Programa para: definir si un año es bisiesto (inspirado de https://www.codigopiton.com/como-saber-si-un-ano-es-bisiesto-en-python/)
year = int(input("Ingrese un año: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

#Ejercicio29 Programa para: Calcular si es negativo o positivo y si es par o impar.
num = int(input("Escriba un numero para determinar si es positivo o negativo  al igual si es par o impar: "))
if num  > 0 and num %2 == 0:
    print("Es un número par-positivo")
elif num < 0 and num%2 == 0:
    print("Es un número par-negativo")
elif num > 0 and num %2 != 0:
    print("Es un número impar-positivo")
elif num < 0 and num%2 != 0:
    print("Es un número impar-negativo")
#Ejercicio30 Programa para: Calcular le energia de un objeto.
m = float(input("Ingrese la masa del objeto (en kilogramos): "))
c = 299792458000
print("La energía es de", m * c**2, "Jul")