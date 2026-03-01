#!/bin/bash

# El nivel lo pasamos como primer argumento (INFO, ERROR, etc.)
NIVEL=$1

# Crear la carpeta de resultados si no existe
mkdir -p out

# Expresión regular "paso a paso" para que sea fácil de explicar
# [NIVEL] seguido de fecha AAAA-MM-DD, hora HH:MM:SS y el mensaje
REGEX="^\[$NIVEL\] [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9] .+"

# Filtrar las líneas que cumplen el formato y guardarlas
grep -E "$REGEX" data/log_muestra_app.log > out/validos.txt

# Mostrar los conteos que pide el profesor
echo "--- Reporte de Logs ($NIVEL) ---"
echo "Líneas totales en el archivo:"
grep -c "." data/log_muestra_app.log
echo "Líneas que cumplen el formato exacto:"
grep -E -c "$REGEX" data/log_muestra_app.log

echo "{" > out/reporte_log.json
echo "  \"total\": $TOTAL_LINEAS," >> out/reporte_log.json
echo "  \"validas\": $VALIDAS" >> out/reporte_log.json
echo "}" >> out/reporte_log.json
