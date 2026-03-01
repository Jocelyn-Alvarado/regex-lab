import re

# Función para validar según las reglas de la práctica
def is_valid(password):
    # 1. ¿Mide 8 o más?
    if len(password) < 8:
        return False
    
    # 2. ¿Tiene al menos una mayúscula?
    if not re.search("[A-Z]", password):
        return False
        
    # 3. ¿Tiene al menos un número?
    if not re.search("[0-9]", password):
        return False
        
    # 4. ¿Solo tiene letras y números? (Si encuentra algo que NO sea eso, es falsa)
    if re.search("[^a-zA-Z0-9]", password):
        return False
        
    return True

# Abrimos los archivos (entrada y los dos de salida)
archivo_entrada = open("data/passwords_muestra.txt", "r")
archivo_validas = open("out/validas.txt", "w")
archivo_invalidas = open("out/invalidas.txt", "w")

# Leemos línea por línea
for linea in archivo_entrada:
    password = linea.strip() # Limpiamos espacios o saltos de línea
    
    if password == "":
        continue # Saltamos líneas vacías
        
    if is_valid(password):
        archivo_validas.write(password + "\n")
    else:
        archivo_invalidas.write(password + "\n")

print("Proceso terminado. Archivos generados en la carpeta out.")

# Siempre cerramos lo que abrimos
archivo_entrada.close()
archivo_validas.close()
archivo_invalidas.close()
