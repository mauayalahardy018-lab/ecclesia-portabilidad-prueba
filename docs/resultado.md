# Resultado de portabilidad — 2026-10-30

Repositorio local independiente: `ecclesia-portabilidad-prueba`. Se instaló el arnés 0.1.2 adaptando `AGENTS.md`, `docs/PROYECTO.md`, la estructura de módulo y los controles. El dominio es una lista genérica de tareas.

Se corrigió una ruta relativa del test copiado: de `./service.js` a `../src/tasks/service.js`. Esta adaptación es necesaria al ubicar pruebas en `tests/`. Se ejecutaron `npm install`, `npm run format` y `npm run check`: lint, formato, dependencias y una prueba pasaron. `rg` no encontró menciones de iglesia, misa, diezmo ni patrimonio en `src` o `tests`.

La prueba demuestra instalación **local** y adaptación del arnés. Al 30 de octubre estaban pendientes el video y la publicación remota; la actualización del 1 de noviembre registra el video explicativo generado. La grabación personal del alumno sigue pendiente.

## Actualización a arnés 0.1.4 — 2026-11-01

Se copió `ecclesia-arnes/hooks/pre-commit` a `.githooks/pre-commit`, se configuró `core.hooksPath=.githooks` y se ejecutó `git hook run pre-commit`. Pasaron lint, formato, revisión de dependencias y la prueba del servicio de tareas. La corrección de la ruta relativa del test sigue registrada arriba; el código del módulo no importa Ecclesia.

La instalación y esta ejecución se muestran en `docs/Video_portabilidad_arnes_0.1.4.mp4`, incluido en el repositorio de portabilidad. Es una demostración visual de la prueba local con salidas reales; la grabación personal del estudiante se entrega por separado si la evaluación la exige.
