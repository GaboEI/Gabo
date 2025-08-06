# Comandos Git para crear y trabajar con ramas

## Crear una nueva rama y cambiarte a ella
```bash
git checkout -b nombre-de-la-rama
```

## Cambiar entre ramas existentes
```bash
git checkout nombre-de-la-rama
```

## Fusionar una rama con la rama principal (main o master)
```bash
git checkout main
git merge nombre-de-la-rama
```

## Eliminar una rama después de fusionarla
```bash
git branch -d nombre-de-la-rama
```

## Actualizar la rama principal con cambios remotos
```bash
git pull origin main
```

## Buenas prácticas
- Usa nombres descriptivos para las ramas.
- Trabaja en ramas pequeñas y específicas.
- Evita trabajar directamente en la rama principal (`main`).