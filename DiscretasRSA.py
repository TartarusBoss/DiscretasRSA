import random
import string

# Solicito la cantidad de cifras para los números primos
cifras = 0
while cifras <= 0 or cifras > 4:
    cifras = int(input("Ingrese la cantidad de cifras para los números primos (máximo 4): "))
    if cifras <= 0:
        print("\033[31mEl numero debe ser mayor a 0\033[0m")
    elif cifras > 4:
        print("\033[31mEl numero debe ser menor o igual a 4\033[0m")

# Defino límites para generar números primos
#Numero de cifras
ncif = 10 ** cifras
#Limite inferior
lim_inf = 10 ** (cifras - 1) + 1
#Limite superior
lim_sup = 10 ** cifras - 1

# Generar lista de números primos de tamaño N
numeros_primos = []
for i in range(lim_inf, lim_sup + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        numeros_primos.append(i)

# Selecciono 2 números primos al azar
p = random.choice(numeros_primos)
q = random.choice(numeros_primos)

# Función para calcular el MCD de dos números algoritmo de euclides
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para generar claves pública y privada
def generar_claves(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    e = random.randint(2, fi - 1)
    while mcd(e, fi) != 1:
        e = random.randint(2, fi - 1)
#E elevado a -1 modulo fi
    d = pow(e, -1, fi)
    return (n, e), (n, d)

# Generar claves pública y privada
clave_publica, clave_privada = generar_claves(p, q)

# Definir alfabeto y caracteres permitidos
alfabeto = string.ascii_letters + string.digits + string.punctuation + 'áéíóúÁÉÍÓÚñÑüÜ '
caracteres_permitidos = set(alfabeto)

# Pedir cadena y convertirla a lista
cadena = input("Ingrese una cadena de texto: ")
lista_cadena = [c for c in cadena if c in caracteres_permitidos]

# Cifrar mensaje
mensaje_cifrado = []
for caracter in lista_cadena:
    indice_caracter = alfabeto.index(caracter)
    caracter_cifrado = pow(indice_caracter, clave_publica[1], clave_publica[0])
    mensaje_cifrado.append(caracter_cifrado)

# Descifrar mensaje
mensaje_descifrado = ""
for caracter_cifrado in mensaje_cifrado:
    indice_caracter = pow(caracter_cifrado, clave_privada[1], clave_privada[0])
    caracter_descifrado = alfabeto[indice_caracter]
    mensaje_descifrado += caracter_descifrado

# Mostrar menú de opciones
print("\n--- MENÚ DE OPCIONES ---")
print("\033[33m1. Mostrar todo")
print("2. Mostrar clave pública")
print("3. Mostrar clave privada")
print("4. Mostrar mensaje original")
print("5. Mostrar mensaje cifrado")
print("6. Mostrar mensaje descifrado")
print("7. Salir\033[0m")

# Ciclo principal del programa
while True:
    opcion = input("\nIngrese una opción del menú: ")

    if opcion == "1":
        print("\n\033[32mClave pública:\033[0m", clave_publica)
        print("\n\033[32mClave privada:\033[0m", clave_privada)
        print("\n\033[32mMensaje original:\033[0m", cadena)
        print("\n\033[32mMensaje cifrado:\033[0m", mensaje_cifrado)
        print("\n\033[32mMensaje descifrado:\033[0m", mensaje_descifrado)

    elif opcion == "2":
        print("\n\033[32mClave pública:\033[0m", clave_publica)

    elif opcion == "3":
        print("\n\033[32mClave privada:\033[0m", clave_privada)

    elif opcion == "4":
        print("\n\033[32mMensaje original:\033[0m", cadena)

    elif opcion == "5":
        print("\n\033[32mMensaje cifrado:\033[0m", mensaje_cifrado)

    elif opcion == "6":
        print("\n\033[32mMensaje descifrado:\033[0m", mensaje_descifrado)

    elif opcion == "7":
        print("\n\033[32m¡Hasta luego!\033[0m")
        break

    else:
        print("\nOpción no válida. Por favor ingrese una opción válida del menú.")