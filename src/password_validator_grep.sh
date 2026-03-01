#!/bin/bash

# Creamos la carpeta de resultados
mkdir -p out

# Archivo con las contraseñas
ARCHIVO="data/passwords_muestra.txt"

echo "Validando contraseñas..."

# 1. Filtrar las que miden 8 o más (el punto . representa cualquier carácter)
# Buscamos las que tengan al menos 8 puntos
grep -E ".{8,}" $ARCHIVO > out/temporal_largo.txt

# 2. De esas, filtrar las que tengan una mayúscula [A-Z]
grep -E "[A-Z]" out/temporal_largo.txt > out/temporal_mayus.txt

# 3. De esas, filtrar las que tengan un número [0-9]
grep -E "[0-9]" out/temporal_mayus.txt > out/temporal_num.txt

# 4. Finalmente, quitar las que tengan símbolos raros
# Buscamos las que SOLO tengan letras y números de inicio a fin
grep -E "^[a-zA-Z0-9]+$" out/temporal_num.txt > out/validas.txt

# Limpiamos los archivos temporales que usamos
rm out/temporal_*.txt

echo "Proceso terminado. Las contraseñas válidas están en out/validas.txt"
