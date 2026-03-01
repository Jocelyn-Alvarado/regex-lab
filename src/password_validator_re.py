import re
import os

def is_valid(password):
    # Regla 1: Longitud >= 8 [cite: 60]
    if len(password) < 8:
        return False, "longitud insuficiente"
    # Regla 2: Al menos una mayúscula [cite: 61]
    if not re.search(r"[A-Z]", password):
        return False, "no tiene mayúscula"
    # Regla 3: Al menos un dígito [cite: 62]
    if not re.search(r"\d", password):
        return False, "no tiene dígito"
    # Regla 4: Solo letras y números [cite: 63]
    if re.search(r"[^a-zA-Z0-9]", password):
        return False, "tiene caracteres inválidos"
    
    return True, "válida"

def main():
    archivo_entrada = "data/passwords_muestra.txt"
    if not os.path.exists("out"):
        os.makedirs("out")

    validas_count = 0
    invalidas_count = 0

    try:
        with open(archivo_entrada, "r") as f, \
             open("out/validas.txt", "w") as f_val, \
             open("out/invalidas.txt", "w") as f_inv:
            
            for linea in f:
                pwd = linea.strip()
                if not pwd: continue
                
                valida, motivo = is_valid(pwd)
                
                if valida:
                    f_val.write(f"{pwd}\n")
                    validas_count += 1
                else:
                    f_inv.write(f"{pwd} -> RECHAZADA: {motivo}\n")
                    invalidas_count += 1

        print(f"Total de válidas: {validas_count}")
        print(f"Total de inválidas: {invalidas_count}")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de contraseñas en data/")

if __name__ == "__main__":
    main()
