# Decisiones tecnologicas revisadas en 2026

La plantilla evita convertir una herramienta de moda en una dependencia arquitectonica. Cada componente se adopta por una responsabilidad concreta.

## Entorno y dependencias

[uv](https://docs.astral.sh/uv/concepts/projects/sync/) administra el entorno, resuelve dependencias y genera un lockfile. El lockfile debe validarse en CI con `uv lock --check`.

## Entrenamiento y baseline

- [TorchVision](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial) ofrece un camino oficial para fine-tuning y datasets personalizados.
- [Ultralytics](https://docs.ultralytics.com/models/) recomienda YOLO26 para proyectos nuevos y YOLO11 como alternativa madura en 2026.
- Ultralytics publica codigo y modelos bajo AGPL-3.0 y licencia Enterprise. La compatibilidad de licencia debe evaluarse antes de cada uso comercial.

El nombre del modelo es configuracion. No debe quedar incorporado a la logica del dominio.

## Inferencia portable

[ONNX Runtime](https://onnxruntime.ai/docs/) permite ejecutar modelos exportados en distintos sistemas y proveedores de hardware. La exportacion no se considera valida hasta comparar numericamente las salidas y medir latencia en el dispositivo objetivo.

## Datos y experimentos

- [DVC](https://dvc.org/doc/command-reference/) puede versionar datasets y artefactos grandes sin almacenarlos en el historial de Git.
- [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking) registra parametros, versiones de codigo, metricas y artefactos por ejecucion.

Ambos son opcionales: un proyecto pequeno puede comenzar con manifiestos y archivos JSON, siempre que la trazabilidad sea explicita.

## Calidad

- `pytest` para pruebas del dominio y de integracion.
- `ruff` para formato y analisis estatico rapido.
- GitHub Actions para validar cada cambio sin descargar modelos ni datos privados.
- checksums y fichas para modelos provenientes de terceros.

## Tecnologias no elegidas automaticamente

Deteccion abierta, segmentacion, tracking, modelos fundacionales y servicios administrados pueden ser utiles, pero solo deben incorporarse si las metricas y restricciones del problema los justifican.
