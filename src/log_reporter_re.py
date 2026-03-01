import re
import sys

# Recibimos el nivel (INFO, ERROR, etc.)
nivel = sys.argv[1]
archivo_log = open("data/log_muestra_app.log", "r")
archivo_salida = open("out/validos_python.txt", "w")

# Contadores básicos
total = 0
validas = 0

for linea in archivo_log:
    linea = linea.strip()
    if not linea: continue
    
    total = total + 1
    # RegEx: [NIVEL] AAAA-MM-DD HH:MM:SS Mensaje
    regex = r"^\[" + nivel + r"\] [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} .+"
    
    if re.match(regex, linea):
        validas = validas + 1
        archivo_salida.write(linea + "\n")

# Requisito 51: Generar el JSON de forma manual y simple
archivo_json = open("out/reporte_log.json", "w")
archivo_json.write("{\n")
archivo_json.write(f'  "total": {total},\n')
archivo_json.write(f'  "validas": {validas}\n')
archivo_json.write("}\n")

print(f"Proceso completado. Se generó out/reporte_log.json con {validas} líneas.")

archivo_log.close()
archivo_salida.close()
archivo_json.close()
