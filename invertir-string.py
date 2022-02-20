#Definir una función inversa() que calcule la inversión de una cadena


# Invertir la cadena por posiciones
def inversa(cadena):
  longitud = -(len(cadena)-1)
  nuevaCadena = str()
  for n in range(longitud, 1):
    n = abs(n)
    nuevaCadena += cadena[n]
  return nuevaCadena


# Invertir por Slices
def invertirCadena(cadena):
  return cadena[::-1]


# Invertir cadena manualmente
def invertirCadenaManual(cadena):
  cadenaInvertida = str()
  for letra in cadena:
    cadenaInvertida = letra + cadenaInvertida
  return cadenaInvertida


print('Método 1. Convencional: ', inversa('cristo'))
print('Método 2. Reducido: ', invertirCadenaManual('cristo'))
print('Método 3. Python Slices: ', invertirCadena('cristo'))