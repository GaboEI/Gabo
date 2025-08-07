
# 🛠️ Script `guardar_git.sh`

Este script automatiza el flujo de trabajo con Git para guardar cambios locales en un repositorio remoto (GitHub).

## ✅ ¿Qué hace?

1. Se asegura de que estés en la carpeta correcta (`~/Gabo`)
2. Hace `git pull` para traer cambios remotos antes de guardar los locales
3. Detecta archivos:
   - Nuevos (no rastreados)
   - Eliminados (borrados localmente)
4. Te pregunta si deseas agregar estos archivos automáticamente al commit
5. Si decides continuar:
   - Pregunta por mensaje de commit (puede ser automático si lo dejas vacío)
   - Ejecuta `git add -A`, `git commit`, y `git push origin main`
6. Muestra el estado final del repositorio con `git status`

## 🧠 Alias sugerido

Agrega este alias a tu archivo `~/.zshrc` o `~/.mis_aliases.sh`:

```bash
alias guardar='bash ~/Gabo/scripts/guardar_git.sh'
```

Así podrás ejecutar el guardado completo escribiendo simplemente:

```bash
guardar
```
