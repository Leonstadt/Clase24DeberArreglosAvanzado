palabras=["venir", "salir", "pasear", "andar", "caminar", 
          "recorrer", "venir", "escapar", "resistir", "venir"]
no_duplicado=[]
for palabra in palabras:
    if palabra not in no_duplicado:
        no_duplicado.append(palabra)
print(f"Array sin duplicados: {no_duplicado}")
