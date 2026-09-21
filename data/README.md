# Data contract

No almacene datasets reales directamente en este repositorio.

Estructura sugerida para un proyecto derivado:

```text
data/
|-- raw/          # originales inmutables
|-- interim/      # recortes y transformaciones reproducibles
`-- processed/    # dataset versionado listo para entrenamiento
```

Agregue una tarjeta de dataset siguiendo `docs/data-and-model-governance.md` y use DVC, almacenamiento de objetos o un mecanismo equivalente para los binarios.
