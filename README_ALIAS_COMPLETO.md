
# ⚙️ Alias personalizados de Gabo

Este archivo documenta todos los alias que Gabo ha configurado en su entorno de desarrollo para Linux + Zsh + Powerlevel10k.

---

## 🔌 Activación de entornos de desarrollo

```bash
alias 9807='cd ~/Gabo && source env/bin/activate && code .'
alias 0722='cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION && source env_local/bin/activate && code .'
alias web='cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION/CURSO_DE_DESARROLLO_WEB && source env_local/bin/activate && code .'
```

---

## 🧠 Git – Flujo rápido

```bash
alias guardar="bash ~/Gabo/scripts/guardar_git.sh"
alias estado='git status'
alias añadir='git add -A'
alias mensaje='git commit -m'
alias subir='git push origin main'
alias historial='git log --oneline --graph --all --decorate'
```

---

## 🧹 Limpieza de archivos ignorados o sucios

```bash
alias gitclean='git status --ignored --untracked-files=all | grep -E "^\s+[^ ]" || echo -e "\n✅ \033[1;32mTodo limpio. No hay archivos sucios.\033[0m"'
```

---

## 🔍 Búsqueda rápida en proyectos

```bash
alias buscar='grep -RiIl'
alias buscar_python='grep -RiIl --include="*.py"'
```

---

## 📁 Archivos y navegación de carpetas

```bash
alias abrir='xdg-open'
alias limpiar='clear'
alias arriba='cd ..'
alias escritorio='cd ~/Escritorio'
alias proyectos='cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION'
alias listar='ls -lah --color'
```

---

## 📦 Compresión y respaldos

```bash
alias comprimir='tar -czvf'
alias descomprimir='tar -xzvf'
alias respaldo='bash ~/Gabo/scripts/respaldo_config.sh'
```

---

## ⏱️ Utilidades varias

```bash
alias fecha='date "+%Y-%m-%d %H:%M:%S"'
alias reloj='watch -n 1 date'
alias cls='clear'
alias salir='exit'
```

---

## 🔄 Recargar configuración del entorno

```bash
alias recargar_alias='source ~/.mis_aliases.sh && echo "✅ Alias recargados correctamente."'
alias recargar_todo='source ~/.zshrc && echo "✅ Zsh recargado correctamente."'
```

---

## 📌 Instrucciones de activación

1. Asegúrate de que todos tus alias estén en el archivo:

```.
~/.mis_aliases.sh
```

Y que esté incluido en tu `~/.zshrc` así:

```bash
source ~/.mis_aliases.sh
```

Luego recarga todo con:

```bash
recargar_todo
```

✅ Tu terminal estará lista con todas tus herramientas personalizadas activas.

---

## ⚙️ Guía rápida de alias, entornos virtuales y permisos

Este documento resume cómo configurar alias personalizados, entornos virtuales y scripts ejecutables para automatizar tu entorno de desarrollo en Linux.

---

## 🧪 Crear alias personalizados

1. Abre tu archivo de alias:

```bash
nano ~/.mis_aliases.sh
```

 Agrega un alias. Ejemplo para desarrollo web:

```bash
alias web='cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION/CURSO_DE_DESARROLLO_WEB && source env/bin/activate && code .'
```

1. Guarda y cierra (Ctrl + O, Enter, Ctrl + X)

2. Recarga los alias:

```bash
source ~/.mis_aliases.sh
```

---

## 🔄 Asegurar carga automática de alias

1. Edita tu `.zshrc`:

```bash
nano ~/.zshrc
```

Asegúrate de incluir esta línea al final:

```bash
source ~/.mis_aliases.sh
```

1. Recarga Zsh:

```bash
source ~/.zshrc
```

---

## 🧠 Activar entorno virtual en una carpeta

1. Entra en la carpeta del proyecto:

```bash
cd ~/Gabo/PROYECTOS_DE_CURSOS_PROGRAMACION/CURSO_DE_DESARROLLO_WEB
```

Crea el entorno virtual:

```bash
python3 -m venv env
```

1. Actívalo:

```bash
source env/bin/activate
```

Abre el proyecto en VS Code:

```bash
code .
```

---

## 🛠️ Dar permisos y ejecutar scripts

1. Da permisos de ejecución:

```bash
chmod +x guardar_mis_clases_PRO.sh
```

Ejecuta el script:

```bash
./guardar_mis_clases_PRO.sh
```

---

✅ Listo. Con esta guía de referencia rápida tendrás tu entorno profesional siempre configurado correctamente.