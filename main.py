

def name(nombre):
  answer= "Nombre no aceptado"
  if nombre != "Frank":
      answer = "Nombre aceptado"
  return answer

def age(edad):
  resultado = "Edad aceptada"
  if edad < 18:
    resultado = "Edad no aceptada"
  return resultado


Nombre_elegido= input("Introduce un nombre: ")

print (name(Nombre_elegido))

print()

print ("Hola")
print ("Buen dia")

print ()

Nombre_elegido= input("Introduce un nombre: ")

print (name(Nombre_elegido))

print()

print ("Estas son pruebas")

print()

Nombre_elegido= input("Introduce un nombre: ")

print(name(Nombre_elegido))

print()

Edad_elegida= input ("Introduce tu edad: ")
print(age(int(Edad_elegida)))

print ()

Edad_elegida= input ("Introduce tu edad: ")
print(age(int(Edad_elegida)))

print()

print("Fin de la prueba")



