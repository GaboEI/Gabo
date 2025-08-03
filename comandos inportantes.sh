# Crear contenido del archivo .py con comandos básicos de Linux
comandos_linux = """
# 🧰 COMANDOS BÁSICOS DE LINUX – Nivel esencial

# pwd => Muestra la ruta exacta donde estás ubicado
# ls => Lista los archivos y carpetas en el directorio actual
# ls -l => Muestra lista con detalles (tamaño, permisos, fecha)
# ls -a => Incluye archivos ocultos (.git, .env, etc.)
# cd nombre => Entra a la carpeta "nombre"
# cd .. => Sube un nivel (a la carpeta anterior)
# cd ~ => Te lleva a tu carpeta de usuario (/home/usuario)
# mkdir nombre => Crea una nueva carpeta
# touch archivo.py => Crea un archivo vacío
# rm archivo => Borra un archivo específico
# rm -r carpeta/ => Borra una carpeta y su contenido
# mv origen destino => Mueve o renombra archivos/carpetas
# cp origen destino/ => Copia un archivo a otra carpeta
# clear => Limpia la pantalla del terminal
# exit => Cierra la terminal actual

# 🐍 Comandos útiles para Python y programación

# python3 => Abre el intérprete interactivo de Python
# python3 archivo.py => Ejecuta un archivo de Python
# python3 -m venv env => Crea un entorno virtual llamado env
# source env/bin/activate => Activa el entorno virtual
# deactivate => Sale del entorno virtual
# pip install nombre => Instala un paquete
# pip list => Lista paquetes instalados

# 🧠 Comandos de Git y GitHub

# git status => Muestra el estado del repositorio local
# git add . => Añade todos los archivos modificados al staging
# git commit -m "mensaje" => Crea un commit
# git push => Sube los cambios a GitHub
# git pull => Descarga cambios nuevos
# git log => Muestra el historial de commits

# 💬 Extra: Utilidades

# nano archivo.txt => Editor de texto en terminal
# cat archivo.txt => Muestra contenido de un archivo
# history => Muestra comandos anteriores
# sudo apt update => Actualiza la lista de paquetes
# sudo apt install ... => Instala herramientas o apps
"""

# Ruta donde guardar el archivo
#ruta_archivo = Path("/mnt/data/00_comandos_basicos_linux.py")

# Escribir el contenido en el archivo
#ruta_archivo.write_text(comandos_linux)

# Devolver la ruta para que Gabo lo descargue
#ruta_archivo.name


git add .
git commit -m "comandos importantes actualizados"
git push origin mai