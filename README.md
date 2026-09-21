# Object Detection Project Template

Plantilla moderna y deliberadamente pequeña para iniciar proyectos de deteccion de objetos sin mezclar codigo, datos, modelos y resultados.

El repositorio nace de una retrospectiva de un prototipo de vision artificial desarrollado en 2021. No contiene codigo, fotografias, videos, modelos entrenados, marcas ni informacion interna de aquella empresa. Conserva unicamente los aprendizajes tecnicos generalizables y una arquitectura nueva para futuros proyectos.

## Objetivos

- Separar el dominio de la libreria de vision elegida.
- Poder cambiar el detector sin reescribir el pipeline.
- Mantener datos, pesos y resultados fuera del historial normal de Git.
- Hacer explicitas la evaluacion, la trazabilidad y las decisiones de despliegue.
- Servir como referencia clonable, no como una aplicacion terminada.

## Estructura

```text
.
|-- configs/                    # configuracion de ejemplo
|-- data/                       # contratos y tarjetas; sin datos reales
|-- docs/                       # arquitectura, retrospectiva y decisiones
|-- models/                     # manifiestos; sin pesos versionados
|-- outputs/                    # resultados generados, ignorados por Git
|-- scripts/                    # entrenamiento y exportacion opcionales
|-- src/object_detection_template/
|   |-- backends/               # adaptadores a herramientas concretas
|   |-- domain.py               # tipos estables del dominio
|   |-- pipeline.py             # orquestacion independiente del backend
|   `-- ports.py                # contratos Detector y TextRecognizer
`-- tests/                      # pruebas rapidas sin descargar modelos
```

## Inicio rapido

Requiere Python 3.12 y [uv](https://docs.astral.sh/uv/).

```bash
uv sync --group dev
uv run pytest
uv run ruff check .
```

Para probar el adaptador Ultralytics y OCR:

```bash
uv sync --group dev --extra ultralytics --extra ocr
uv run object-detection inspect \
  --model yolo26n.pt \
  --source path/to/image.jpg \
  --threshold 0.50
```

El primer uso de un modelo preentrenado puede descargar pesos. Revise siempre su procedencia, licencia y checksum antes de incorporarlo a un proyecto real.

## Entrenamiento y exportacion

La plantilla incluye envoltorios pequenos y reemplazables:

```bash
uv run --extra ultralytics python scripts/train.py \
  --data configs/dataset.example.yaml \
  --model yolo26n.pt \
  --epochs 50

uv run --extra ultralytics python scripts/export_onnx.py \
  --model path/to/best.pt \
  --output-format onnx
```

Los archivos de ejemplo no forman un dataset entrenable. Deben reemplazarse por rutas y clases propias.

## Flujo recomendado

1. Definir el problema, las clases y la metrica de aceptacion.
2. Crear una tarjeta del dataset y separar `train`, `validation` y `test`.
3. Entrenar un baseline reproducible antes de optimizar.
4. Registrar parametros, metricas, codigo y artefactos por ejecucion.
5. Evaluar errores por clase y por condiciones de captura.
6. Exportar solamente despues de comparar exactitud y latencia en el hardware objetivo.
7. Mantener datos y pesos en DVC, almacenamiento de objetos o un registro de modelos.

## Documentacion

- [Retrospectiva del prototipo de 2021](docs/retrospective-2021.md)
- [Arquitectura de la plantilla](docs/architecture.md)
- [Decisiones tecnologicas 2026](docs/technology-choices-2026.md)
- [Gobierno de datos y modelos](docs/data-and-model-governance.md)
- [Mapa de migracion del registro local](docs/source-inventory.md)

## Alcance

Esta plantilla no promete que un modelo sea adecuado para produccion. Las metricas, el hardware, las licencias, la privacidad, el sesgo del dataset y la supervision humana dependen de cada caso de uso.

La eleccion de licencia del repositorio queda pendiente. Antes de hacerlo publico, seleccione una licencia compatible con los backends y modelos que vaya a utilizar.
