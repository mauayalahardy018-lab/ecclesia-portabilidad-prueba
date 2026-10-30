# Resultado de portabilidad — 2026-10-30

Repositorio local independiente: `ecclesia-portabilidad-prueba`. Se instaló el arnés 0.1.2 adaptando `AGENTS.md`, `docs/PROYECTO.md`, la estructura de módulo y los controles. El dominio es una lista genérica de tareas.

Se corrigió una ruta relativa del test copiado: de `./service.js` a `../src/tasks/service.js`. Esta adaptación es necesaria al ubicar pruebas en `tests/`. Se ejecutaron `npm install`, `npm run format` y `npm run check`: lint, formato, dependencias y una prueba pasaron. `rg` no encontró menciones de iglesia, misa, diezmo ni patrimonio en `src` o `tests`.

La prueba demuestra instalación **local** y adaptación del arnés; queda pendiente publicar este repositorio y grabar el video requerido por el caso.
