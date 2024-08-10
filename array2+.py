palabras=["venir", "salir", "pasear", "andar", "caminar", 
          "recorrer", "venir", "escapar", "resistir", "venir"]
objetivo="venir"
contador=0
for numero in palabras:
    if numero == objetivo:
        contador+=1
print(f"La palabra {objetivo} aparece {contador} veces en el arreglo")
