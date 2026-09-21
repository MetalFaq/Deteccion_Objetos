# Arquitectura

## Principio central

El dominio no depende de Ultralytics, PyTorch, ONNX Runtime ni Tesseract. Esas herramientas se conectan mediante adaptadores.

```text
CLI / aplicacion
      |
      v
InspectionPipeline
      |
      +--> Detector protocol --------> UltralyticsDetector
      |                               otro detector futuro
      |
      `--> TextRecognizer protocol --> TesseractReader
                                      otro OCR futuro
```

## Responsabilidades

- `domain.py`: cajas, detecciones y resultados normalizados.
- `ports.py`: contratos que debe cumplir cada backend.
- `pipeline.py`: filtrado, orden y despacho a reconocedores especializados.
- `backends/`: traduccion desde APIs externas hacia el dominio.
- `scripts/`: tareas operativas que no deben ejecutarse al importar el paquete.
- `configs/`: parametros declarativos, nunca secretos.

## Extension

Para agregar otro detector, implemente:

```python
class Detector:
    def detect(self, source: Path) -> Sequence[Detection]: ...
```

El pipeline y las pruebas de reglas no necesitan conocer el framework utilizado.

## Decisiones pendientes por proyecto

- clases y taxonomia;
- formato de anotacion;
- metrica principal y umbral de aceptacion;
- modelo de referencia;
- hardware objetivo;
- estrategia de versionado de datos y modelos;
- politica de revision humana;
- requisitos de privacidad, licencia y retencion.
