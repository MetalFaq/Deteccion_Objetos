# Inventario del registro local de 2021

Este documento conserva la relacion estructural sin publicar los archivos originales.

## Codigo identificado

| Rol historico | Destino conceptual actual |
|---|---|
| Orquestador de camara e inferencia | `pipeline.py` y una aplicacion concreta |
| Detector de caracteres | Adaptador especializado de deteccion |
| OCR de etiqueta | Implementacion de `TextRecognizer` |
| Generador de recortes | Script de preparacion del dataset |
| Etiquetado asistido | Herramienta separada de anotacion |
| Pruebas de camara | Diagnostico de hardware |

## Artefactos encontrados

- siete checkpoints YOLO; dos eran duplicados exactos;
- fotografias originales y recortes derivados;
- un dataset experimental de dos pares imagen/anotacion;
- seis videos de prueba;
- resultados intermedios no vinculados por el codigo conservado;
- un entorno virtual de aproximadamente 1.96 GB que apuntaba a un Python inexistente.

## Decision de preservacion

No se trasladan al repositorio remoto:

- datos, videos o numeros de serie de la empresa;
- logotipos o documentacion interna;
- pesos entrenados;
- el entorno virtual;
- codigo original potencialmente sujeto a propiedad intelectual empresarial.

Se preservan en forma nueva y generalizada:

- la arquitectura por etapas;
- los contratos entre deteccion, OCR y reglas;
- las lecciones de reproducibilidad;
- la separacion entre codigo, datos, modelos y resultados;
- una base verificable para futuros experimentos.
