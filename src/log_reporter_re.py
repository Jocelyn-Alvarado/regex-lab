import re
import sys
import os
import json

def run_reporter():
    # 1. Obtener el nivel del argumento (INFO, WARN, etc.)
    if len(sys.argv) < 2:
        print("Uso: python3 src/log_reporter_re.py <NIVEL>")
        sys.exit(1)
    
    nivel_buscado = sys.argv[1].upper()
    archivo_entrada = "data/log_muestra_app.log"
    
    # 2. Crear carpeta out si no existe
    if not os.path.exists("out"):
        os.makedirs("out")

    # 3. Expresión Regular (RegEx) - Mismo patrón que en Bash
    # [NIVEL] AAAA-MM-DD HH:MM:SS Mensaje
    regex_valida = r"^\[(INFO|WARN|ERROR|DEBUG)\] \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} .+"

    lineas_validas_nivel = []
    total_no_vacias = 0
    total_validas = 0
    total_sospechosas = 0

    # 4. Leer el archivo y procesar
    try:
        with open(archivo_entrada, "r") as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue # Ignorar vacías
                
                total_no_vacias += 1
                
                # ¿Cumple el formato general?
                es_valida = re.match(regex_valida, linea)
                
                if es_valida:
                    total_validas += 1
                    # Si es del nivel que queremos, la guardamos
                    if f"[{nivel_buscado}]" in linea:
                        lineas_validas_nivel.append(linea)
                else:
                    # ¿Es sospechosa? (Tiene el nivel pero no el formato)
                    if f"[{nivel_buscado}]" in linea:
                        total_sospechosas += 1

        # 5. Guardar resultados en el archivo .txt
        nombre_salida = f"out/{nivel_buscado.lower()}_validos.txt"
        with open(nombre_salida, "w") as f_out:
            for l in lineas_validas_nivel:
                f_out.write(l + "\n")

        # 6. Mostrar en pantalla y generar JSON
        print(f"Total de líneas no vacías: {total_no_vacias}")
        print(f"Total de líneas válidas: {total_validas}")
        print(f"Líneas sospechosas de {nivel_buscado}: {total_sospechosas}")

        reporte = {
            "total": total_no_vacias,
            "validas": total_validas,
            "sospechosas": total_sospechosas
        }
        with open("out/reporte_log.json", "w") as f_json:
            json.dump(reporte, f_json)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_entrada}")

if __name__ == "__main__":
    run_reporter()
