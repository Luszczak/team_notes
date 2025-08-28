# Informe de V1.0.0

## **Issue #1 – Setup base + notes.json (chore)**

Acciones realizadas:

Se creó la estructura de carpetas: app/, data/, tests/.

Se agregó el archivo data/notes.json con un array vacío [].

Se elaboró un README mínimo con la descripción inicial del proyecto.

Estado: Cerrado

## **Issue #2 – Crear nota (feat)**

Acciones realizadas:

Se implementó la función add_note(title, body) que guarda notas con los campos {id, title, body, created_at}.

Se añadió compatibilidad con CLI:

python -m app.cli add "Título" "Cuerpo"

Estado: Cerrado

## **Issue #3 – Listar y buscar (feat)**

Acciones realizadas:

Se implementó la funcionalidad para listar todas las notas existentes.

Se agregó la búsqueda por parámetros, permitiendo filtrar resultados según título o contenido.

Estado: Cerrado

## **Issue #4 – Eliminar nota (feat)**

Acciones realizadas:

Se desarrolló la función delete_note para eliminar notas a partir de su id.

Integración con CLI para ejecutar la eliminación desde consola.

Estado: Cerrado

## **Issue #5 – Pruebas unitarias básicas (test)**

Acciones realizadas:

Se escribieron pruebas unitarias con pytest para validar las funciones principales:

add_note

list_notes

delete_note

Se comprobó la correcta creación, listado y eliminación de notas.

Estado: Cerrado

## **Issue #6 – Lanzamiento v1.0.0 (release)**

Acciones realizadas:

Se consolidaron todas las funcionalidades implementadas.

Se cerró la versión v1.0.0 como primer release estable.

Estado: Cerrado
