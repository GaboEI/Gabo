#!/bin/bash

# Script para guardar automáticamente los cambios del curso en GitHub

echo "📦 Guardando todo el trabajo del día en GitHub..."

# Navegar a la carpeta del proyecto (opcional si ya estás dentro)
# cd /home/gabodev/Gabo

# Añadir todos los archivos nuevos o modificados
git add .

# Pedir mensaje de commit
read -p "📝 Escribe un mensaje para el commit: " mensaje

# Crear el commit
git commit -m "$mensaje"

# Subir al repositorio remoto
git push

echo "✅ Todo fue subido correctamente a GitHub."
