#!/bin/bash

ARCHIVO="data/passwords_muestra.txt"
mkdir -p out

# Limpiar archivos previos
> out/validas.txt
> out/invalidas.txt

VALIDAS=0
INVALIDAS=0

while IFS= read -r pass || [ -n "$pass" ]; do
    # Eliminar espacios en blanco
    pass=$(echo "$pass" | xargs)
    [ -z "$pass" ] && continue

    MOTIVOS=""

    # Regla 1: Longitud >= 8
    if [[ ! ${#pass} -ge 8 ]]; then
        MOTIVOS+="longitud insuficiente, "
    fi
    # Regla 2: Al menos una mayúscula
    if [[ ! "$pass" =~ [A-Z] ]]; then
        MOTIVOS+="no tiene mayúscula, "
    fi
    # Regla 3: Al menos un dígito
    if [[ ! "$pass" =~ [0-9] ]]; then
        MOTIVOS+="no tiene dígito, "
    fi
    # Regla 4: Solo letras y números
    if [[ "$pass" =~ [^a-zA-Z0-9] ]]; then
        MOTIVOS+="tiene caracteres inválidos, "
    fi

    if [ -z "$MOTIVOS" ]; then
        echo "$pass" >> out/validas.txt
        ((VALIDAS++))
    else
        echo "$pass -> RECHAZADA: ${MOTIVOS%, }" >> out/invalidas.txt
        ((INVALIDAS++))
    fi
done < "$ARCHIVO"

echo "Total de válidas: $VALIDAS"
echo "Total de inválidas: $INVALIDAS"
