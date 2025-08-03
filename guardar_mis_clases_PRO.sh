#!/bin/bash

# Ruta base del proyecto
PROYECTO=~/Gabo

# Cambiar a la carpeta del proyecto
cd "$PROYECTO" || {
    echo "❌ No se encontró la carpeta $PROYECTO. Abortando..."
    exit 1
}

# Verifica si hay cambios
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ No hay cambios para guardar. El repositorio está actualizado."
    exit 0
fi

# Preguntar por mensaje de commit
echo "✏️ Escribe un mensaje para el commit (o pulsa Enter para usar uno automático):"
read mensaje

# Si está vacío, generar uno automático con fecha y hora
if [ -z "$mensaje" ]; then
    mensaje="Actualización automática: 2025-08-03 02:51:27"
fi

# Añadir, hacer commit y subir
git add .
git commit -m "Backup automático - $(date +'%d-%m-%Y %H:%M')"
git push

echo "🚀 Cambios guardados y subidos correctamente a GitHub."
#./guardar_mis_clases_PRO.sh
#cd ~/Gabo && git pull
