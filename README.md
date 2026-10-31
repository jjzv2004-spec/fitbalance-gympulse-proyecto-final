# FitBalance y GymPulse: integración de datos y prospectiva

**Juan José Zapata y Juanita Pineda**  
Proyecto final de Integración de Datos y Prospectiva.

## Entrega

- [Abrir el notebook en Google Colab](https://colab.research.google.com/github/jjzv2004-spec/fitbalance-gympulse-proyecto-final/blob/main/notebooks/Proyecto_Final_FitBalance_GymPulse.ipynb).
- [Notebook con resultados y gráficas](notebooks/Proyecto_Final_FitBalance_GymPulse.ipynb).
- [Presentación editable](presentacion/Proyecto_Final_FitBalance_GymPulse.pptx).
- [Video de apoyo con narración sintética en español](video/Presentacion_FitBalance_GymPulse.mp4).
- [Guion y reparto sugerido de la exposición](docs/Guion_video.md).
- [Informe de resultados](docs/Informe_resultados.md).
- [Diccionario de variables](docs/Diccionario_variables.md) y [supuestos](docs/Supuestos_y_limitaciones.md).

El video usa narración sintética de apoyo y no reproduce las voces de los integrantes. El requisito de asistencia presencial se debe cumplir personalmente.

## Pregunta del proyecto

¿Cómo cambia la caracterización de pérdidas por cancelaciones al incorporar registros externos comparables, y qué presupuesto podría financiar captura de GEI bajo niveles de gestión propuestos?

Las empresas son ficticias. GymPulse reproduce pares internos con severidad incrementada 3% y un orden calibrado. No es una fuente independiente ni demuestra generalización. El enunciado permite bases generadas con LLM; aquí se documentan sus transformaciones, en vez de presentarlas como observaciones de una empresa real.

## Resultados calculados

| Indicador | Resultado |
|---|---:|
| Registros por fuente | 1.200 |
| Integración por pérdida agregada | 1140 aceptados (95%) |
| Integración multidimensional, h=0,10 | 212 aceptados (17.67%) |
| Diferencia de media integrada, modelo 1 | 0.56% |
| Diferencia de media integrada, modelo 2 | 4.45% |
| Mejor NG entre los probados | 2.0 |
| Neto hipotético, 365 días | COP 219,402,412.69 |
| Captura potencial financiable, supuestos base | 73.13 tCO₂e |

La diferencia de curtosis integrada del modelo 1 es mayor que la de su media; consultar todas las medidas en `resultados/04_discrepancias.csv`. Una media cercana no demuestra equivalencia de las colas. Las toneladas se calculan sobre un presupuesto supuesto y no son captura física medida o certificada.

## Dos modelos de integración del curso

1. **Pérdida agregada:** distancia relativa a cinco concentradores y VP>0,90, adaptado de integración COSCO. Se conservan semilla 42 y el orden del escenario.
2. **Multidimensional:** centros secuenciales sobre frecuencia y severidad escaladas con la interna, adaptado de integración multidimensional. El filtro gaussiano con h=0,10 es una extensión declarada; se incluye sensibilidad h=0,05/0,10/0,20.

Credibilidad es un contraste adicional. PAM con medoides reales y lógica difusa se usan para caracterizar y evaluar la gestión interna. No se llama K-Medoids a la actualización secuencial por promedios de los dos modelos de integración.

## Ejecutar

### Google Colab

Abre el enlace de Colab. Guarda `FitBalance_interna.xlsx`, `GymPulse_simulada.xlsx` y `Escenarios_GEI.csv` en `Mi unidad/Integracion de datos/Proyecto_Final_FitBalance_GymPulse/`. Ejecuta todas las celdas. La conexión usa `from google.colab import drive` y una ruta escrita directamente, como en clase.

### Local

Desde la raíz del repositorio, con Python 3.12:

```bash
python -m pip install -r requirements.txt
python src/analisis.py
python -m unittest discover -s tests -v
```

El script reproduce los cálculos del notebook y escribe tablas y figuras en `resultados/`. No necesita tokens, contraseñas, APIs pagadas ni la conexión de Drive. La prueba de CI se define en `.github/workflows/validacion.yml`.

## Estructura

```text
data/          Bases originales y simuladas, supuestos y trazabilidad
notebooks/     Documento de trabajo para Colab con salidas ejecutadas
src/           Análisis reproducible
resultados/    Decisiones por registro, tablas y figuras
docs/          Informe, diccionario, metodología, guion y verificación del reto
presentacion/  Presentación editable
video/         Video de apoyo narrado
tests/         Pruebas numéricas y de integridad
```

## Integridad

`data/Trazabilidad_simulacion.csv` registra el origen de los pares simulados y `docs/Manifiesto_archivos.json` guarda los hashes de las tres bases. No se fusionan registros por fecha ni se atribuye una identidad cliente común. No se inventan relaciones causales entre las categorías externas y los pares numéricos reasignados.

## Referencias

Enunciado “7. Challenge Presentación Final.docx” proporcionado por el estudiante. Ejercicios del curso: integración COSCO, integración multidimensional, teoría de credibilidad y Fuzzy Logic. Los enlaces y adaptaciones se detallan en [Fuentes_y_metodologia.md](docs/Fuentes_y_metodologia.md). No se presentan precios ambientales de mercado: los costos por contacto y por tonelada son supuestos editables.
