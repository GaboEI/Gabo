#!/bin/bash

# Ruta base del proyecto
PROYECTO=~/Gabo

# Cambiar a la carpeta del proyecto
cd "$PROYECTO" || {
    echo "❌ No se encontró la carpeta $PROYECTO. Abortando..."
    exit 1
}

# 🔄 Sincronizar primero con la rama remota
echo "📥 Verificando cambios remotos en GitHub..."
git pull origin main || {
    echo "⚠️ No se pudo hacer pull. Verifica tu conexión o conflictos."
    exit 1
}

# 📋 Verifica si hay cambios locales
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ No hay cambios locales para guardar. El repositorio está actualizado."
    exit 0
fi

# 📝 Preguntar por mensaje de commit
echo -e "\n✏️ Escribe un mensaje para el commit (o pulsa Enter para usar uno automático):"
read -r mensaje

# ⏰ Si está vacío, generar mensaje automático con fecha y hora simpática
if [ -z "$mensaje" ]; then
    fecha_actual=$(date "+%Y-%m-%d %H:%M:%S")
    mensaje="🤖 Guardado automático el $fecha_actual"
fi

# ✅ Agregar, hacer commit y subir
git add .
git commit -m "$mensaje"
git push origin main

# 📊 Mostrar estado final
echo -e "\n✅ Cambios guardados correctamente. Estado del repositorio:"
git status
