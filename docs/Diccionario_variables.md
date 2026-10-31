# Diccionario de bases y variables

## FitBalance_interna.xlsx — hoja Datos

Una fila representa un registro diario de la empresa ficticia. Son 1.200 filas. La copia conserva las hojas y valores del archivo proporcionado.

| Campo | Tipo / unidad | Definición y uso |
|---|---|---|
| Día | Entero identificador | Posición del día. Identificar con prefijo FB, no cruzar directamente con otra empresa. |
| Fecha | Fecha | Período de referencia. No es llave cliente. |
| Sede | Categoría | Sede que describe el registro diario. |
| Plan | Categoría | Plan indicado en el registro. |
| Motivo | Categoría | Motivo consignado, sin inferencia causal. |
| Frecuencia | Entero, cancelaciones/día | Número de cancelaciones del registro. Entrada del modelo multidimensional. |
| Severidad | Continua, COP/cliente | Pérdida por cliente que cancela. Los días sin cancelaciones tienen cero convencional. |
| LDA | Continua, COP/día | Producto frecuencia × severidad. Entrada de integración unidimensional. |

## GymPulse_simulada.xlsx — Sheet1

Una fila representa un día-empresa del escenario externo. Son 1.200 filas. El escenario es dependiente de la referencia interna.

| Campo | Tipo / unidad | Correspondencia |
|---|---|---|
| Dia | Entero identificador | Día, con prefijo GP para conservar procedencia. |
| Fecha | Fecha | Misma ventana de referencia; se conserva de la fuente externa inicial. |
| Sede | Categoría | No supone que las sedes sean entidades iguales entre empresas. |
| Plan_Dominante | Categoría | Correspondencia de vocabulario con Plan; no usada en las distancias numéricas. |
| Motivo_Cancelacion_Dominante | Categoría | Contexto conservado de la base externa inicial. |
| Frecuencia_Cancelaciones_Dia | Entero, cancelaciones/día | Copia de un valor interno según trazabilidad. |
| Severidad_COP_Cliente | Continua, COP/cliente | Severidad interna ×1,03, redondeada a centavos. |

LDA externa se calcula con el producto. Las categorías conservadas no se calibraron conjuntamente con los valores numéricos, por lo que no se validan análisis de riesgo por categorías sobre esta simulación.

## Escenarios_GEI.csv — base de prospectiva

| Campo | Unidad | Valor base / función |
|---|---|---|
| NG | Factor adimensional | 1; 1,1; 1,2; 1,5; 2. Multiplica celdas intermedias de MG. |
| Horizonte_dias | Días | 365. Promedio histórico supuesto constante. |
| Costo_contacto_COP | COP/contacto | 30.000, supuesto de gestión incremental. |
| Fraccion_para_GEI | Proporción 0–1 | 0,10 del neto positivo. |
| Costo_tCO2e_COP | COP/tCO₂e | 300.000, supuesto de financiación de captura. |

## Variables derivadas

VP: pertenencia gaussiana, no probabilidad calibrada. h: ancho del filtro multidimensional en unidades escaladas. Cr: peso de la media propia en la fórmula simplificada de credibilidad. MP: pérdidas por combinación de medoides. ME: conteo de días con eventos. MI: regla ordinal de impacto. MG: matriz de gestión propuesta. Captura_financiable_tCO2e: presupuesto positivo dividido por costo supuesto por tonelada. No mide emisiones reales ni certificados.
