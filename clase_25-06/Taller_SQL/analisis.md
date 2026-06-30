# Análisis de Resultados - Industria 4.0
**Estudiante:** Ginna Esmeralda Paez Lancheros , Julian Rojas.

### 1. ¿Por qué la limpieza y filtrado de datos en SQL es el paso previo indispensable antes de entrenar un modelo de Machine Learning en Python?
Porque la calidad de las predicciones depende de la pureza de los datos de entrada. Realizar la limpieza en SQL permite descartar ruidos, valores nulos o registros irrelevantes directamente en el motor de base de datos, optimizando el uso de memoria RAM en Python y garantizando que el modelo aprenda de patrones reales.

### 2. En un escenario de producción industrial con millones de filas de telemetría vehicular, ¿qué impacto tiene mapear correctamente las llaves primarias y limitar las consultas con LIMIT en lugar de traer siempre todos los datos?
El mapeo de llaves primarias genera índices que aceleran la recuperación de información sin recorrer toda la tabla. El uso de `LIMIT` es una práctica de optimización crítica que evita el desbordamiento de memoria y reduce la latencia de red, permitiendo que el sistema de analítica sea escalable y eficiente.

### 3. ¿En qué caso específico se justificaría usar un TRUNCATE con la instrucción IMMEDIATE en lugar de un DELETE tradicional?
Se justifica en procesos de carga masiva o tablas de "staging" (tránsito). Si se recibe telemetría en tiempo real que solo debe procesarse y borrarse para la siguiente ráfaga, `TRUNCATE IMMEDIATE` es superior porque libera el espacio en disco al instante y no sobrecarga el log de transacciones, a diferencia de un `DELETE` fila por fila.