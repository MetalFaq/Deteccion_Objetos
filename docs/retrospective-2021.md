# Retrospectiva de un prototipo de vision artificial de 2021

## Contexto

Este repositorio fue inspirado por una experiencia de aprendizaje en una empresa durante 2021. El trabajo original exploraba deteccion de objetos, reconocimiento de caracteres y OCR sobre imagenes de equipamiento industrial.

El material original pertenecia a la empresa y no se publica aqui. Esta retrospectiva conserva exclusivamente conceptos generales, decisiones tecnicas y lecciones aprendidas.

## Flujo investigado

```text
imagen o camara
      |
      v
detector de regiones de interes
      |-------------------|
      v                   v
region con display    region con etiqueta
      |                   |
      v                   v
detector de caracteres    OCR
      |                   |
      `--------> reglas de validacion
```

El prototipo separaba el problema en dos etapas:

1. Detectar las regiones de interes en la imagen completa.
2. Aplicar un reconocedor especializado sobre cada region.

Esta composicion sigue siendo util: reduce el espacio de busqueda y permite evaluar por separado deteccion, lectura y reglas de negocio.

## Lo que resulto valioso

- Transfer learning con un detector preentrenado.
- Uso de bounding boxes para aislar regiones relevantes.
- Separacion entre OCR convencional y deteccion de caracteres visuales.
- Construccion de herramientas de etiquetado asistido.
- Pruebas con imagenes, videos y captura de camara.
- Comprension practica del impacto de iluminacion, perspectiva, resolucion y umbral de confianza.

## Limitaciones del registro original

- El entorno virtual se habia copiado entre equipos y no era reproducible.
- Los pesos no tenian ficha de modelo, metricas ni procedencia documentada.
- El dataset local era una muestra parcial y no permitia reproducir el entrenamiento.
- Las anotaciones no seguian de forma consistente el contrato numerico de YOLO.
- El codigo cargaba una rama remota de YOLO mediante `torch.hub` sin fijar commit.
- Las rutas de modelos, entradas y Tesseract estaban incorporadas al codigo.
- Los scripts ejecutaban efectos laterales al importarse.
- No habia pruebas automatizadas ni separacion entre datos, codigo y resultados.
- La comparacion final de resultados estaba descrita, pero no terminada.

## Que cambia en esta plantilla

| 2021 | Plantilla actual |
|---|---|
| Entorno virtual copiado | Entorno reconstruible desde `pyproject.toml` y `uv.lock` |
| Backend acoplado a `torch.hub` | Puerto `Detector` y adaptadores reemplazables |
| Rutas en el codigo | Configuracion externa y argumentos de CLI |
| Pesos sin trazabilidad | Manifiesto, checksum, licencia y metricas por modelo |
| Datos mezclados con codigo | Directorios y politicas separados |
| Salidas manuales | Resultado de dominio normalizado y testeable |
| Pruebas visuales aisladas | Pruebas unitarias y CI sin descargar modelos |

## Leccion principal

El modelo es solo una parte del sistema. Para que un proyecto de vision sea mantenible, tambien deben ser reproducibles el dataset, las transformaciones, las metricas, el entorno, la configuracion y el despliegue.
