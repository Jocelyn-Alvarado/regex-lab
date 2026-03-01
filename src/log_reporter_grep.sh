#!/bin/bash

# 1. El usuario especifica el nivel (punto 41 del PDF)
NIVEL=$1
ARCHIVO_LOG="data/log_muestra_app.log"

# Validar argumento
if [ -z "$NIVEL" ]; then
    echo "Uso: $0 <INFO|WARN|ERROR|DEBUG>"
    exit 1
fi

# 2. Carpeta out/ automática (punto 23)
mkdir -p out

# 3. RegEx del formato válido (punto 33)
# [NIVEL] AAAA-MM-DD HH:MM:SS Mensaje
REGEX="^\[(INFO|WARN|ERROR|DEBUG)\] [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} .+"

# 4. Nombre de archivo en minúsculas (punto 45)
NIVEL_MIN=$(echo "$NIVEL" | tr '[:upper:]' '[:lower:]')
OUTPUT_FILE="out/${NIVEL_MIN}_validos.txt"

# 4. Extraer líneas (punto 43)
grep -E "$REGEX" "$ARCHIVO_LOG" | grep "\[$NIVEL\]" > "$OUTPUT_FILE"

# 5. Totales en pantalla (puntos 47, 48, 49)
TOTAL_LINEAS=$(grep -c "." "$ARCHIVO_LOG")
VALIDAS=$(grep -E -c "$REGEX" "$ARCHIVO_LOG")
SOSPECHOSAS=$(grep "\[$NIVEL\]" "$ARCHIVO_LOG" | grep -E -v -c "$REGEX")

echo "Total de líneas no vacías: $TOTAL_LINEAS"
echo "Total de líneas válidas: $VALIDAS"
echo "Líneas sospechosas de $NIVEL: $SOSPECHOSAS"

# 6. Generar JSON (punto 51)
echo "{\"total\": $TOTAL_LINEAS, \"validas\": $VALIDAS, \"sospechosas\": $SOSPECHOSAS}" > out/reporte_log.json
