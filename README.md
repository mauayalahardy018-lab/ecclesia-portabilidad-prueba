# Prueba local de portabilidad del arnés

Se instalaron reglas adaptadas, estructura ruta→servicio→repositorio, formato, lint, revisión de dependencias y prueba del dominio. Ejecutar `npm ci && npm run check`. La evidencia de la ejecución se registra en `docs/resultado.md`. Este repositorio es local hasta que se elija un remoto.

La versión 0.1.4 del arnés añade `.githooks/pre-commit`. Ejecutar `git config core.hooksPath .githooks` una vez y verificarlo con `git hook run pre-commit`.
