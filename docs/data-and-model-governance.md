# Gobierno de datos y modelos

## Datos

Cada dataset debe tener una tarjeta en `data/` que documente:

- origen y autorizacion de uso;
- fecha y version;
- clases y reglas de anotacion;
- cantidad de imagenes e instancias por particion;
- transformaciones aplicadas;
- casos excluidos;
- riesgos de privacidad y sesgo;
- checksum o identificador remoto.

Los conjuntos `train`, `validation` y `test` deben separarse por unidad independiente del problema. Dividir cuadros contiguos de un mismo video entre particiones puede producir fuga de informacion.

## Modelos

Cada peso debe tener una ficha con:

- arquitectura y checkpoint base;
- commit y entorno de entrenamiento;
- version exacta del dataset;
- hiperparametros;
- metricas por clase;
- hardware y duracion del entrenamiento;
- formatos exportados;
- licencia y restricciones;
- SHA-256 del artefacto.

Los checkpoints serializados pueden ejecutar codigo al cargarse. Utilice solamente artefactos confiables y prefiera formatos de inferencia que reduzcan esa superficie cuando sea apropiado.

## Git

Git conserva codigo, configuracion, contratos, tarjetas y resultados pequenos. Los datos, pesos y salidas voluminosas deben ir a almacenamiento de artefactos, DVC, Git LFS o un registro de modelos segun el caso.
