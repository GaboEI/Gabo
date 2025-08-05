#!/bin/bash

# Ruta base del proyecto
PROYECTO=~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION/CURSO_DE_DESARROLLO_WEB #cambiar rura si esto se modifica para otra carpeta 

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
git commit -m "$mensaje"
git push

echo "🚀 Cambios guardados y subidos correctamente a GitHub."

#chmod +x guardar_mis_clases_PRO.sh -> conseder permiso


#! CREAR ALIAS:
#-> nano ~/.bashrc #!abrre el archivo
#-> alias web='cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION/CURSO_DE_DESARROLLO_WEB && source env/bin/activate && code .' #!ESCRIBES EN LA ULTIMA LINEA

#!ACTIVACION DEL ALIAS
#->cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION/CURSO_DE_DESARROLLO_WEB #!ABRES LA CARPETA EN LINUX
#->python3 -m venv env #!CRREA ENTORNO VIRTUAL PARA LA CARPETA
#->source env/bin/activate #!ACTIVA ENTORNO VIRTUAL PARA LA CARPETA
#->code . #! ABRE VS CODE
#->source ~/.bashrc #! DA PERMISO AL ALIAS DE FUNCIONAR


#chmod +x guardar_mis_clases_PRO.sh #![LE DA PERMISO A ESTE SCRIPT]
#./guardar_mis_clases_PRO.sh #![EJECUTA ESTE ARCHIVO]