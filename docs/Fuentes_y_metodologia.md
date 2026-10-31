# Fuentes y adaptaciones

## Archivos de entrada

- `Reto_1_Clientes_Gimnasio (4).xlsx`, proporcionado inicialmente por el estudiante, copia interna sin modificar en data/FitBalance_interna.xlsx.
- `Base_de_Datos_GymPulse_Externa (2).xlsx`, proporcionada por el estudiante, usada como estructura para la simulación. La variante calibrada final se conserva en data/GymPulse_simulada.xlsx.
- `7. Challenge Presentación Final.docx`, enunciado proporcionado por el estudiante el 31 de octubre de 2026.
- Base de supuestos de prospectiva creada para el proyecto: data/Escenarios_GEI.csv.

## Material de clase consultado

- Integración de datos COSCO: https://drive.google.com/file/d/1HbfEE8sjAXDPxsEDlhgywH3zGYIGnDCl/view
- Integración multidimensional: https://colab.research.google.com/drive/1zH0kx_NpZaK69aw9REI4EUv59j6gXJNn
- Teoría de credibilidad: https://colab.research.google.com/drive/1U3IuP4cBWEpNnnRW8wrZ-6qrtHA-wgP-
- Fuzzy Logic de clase: https://drive.google.com/file/d/1DBbbj70N-5C2Lj2TeQyGvvhIGWp2fPcj/view

Estos enlaces pueden requerir autorización de Drive del titular. El notebook de integración multidimensional fue consultado mediante la conexión de Drive para revisar las entradas y actualizaciones secuenciales. Los ejemplos de integración y Fuzzy Logic habían sido proporcionados durante el desarrollo del proyecto.

Se mantienen las variables simples de clase y la conexión directa a Drive. Se agregan escala interna para las dos entradas multidimensionales, un filtro gaussiano explícito y su sensibilidad. Los centros por promedios secuenciales no se denominan medoides. Para PAM difuso se usa una función de intercambios entre observaciones reales. Se corrigen las confusiones entre estimación, ahorro y captura física.

No se consultaron cotizaciones de carbono para fijar los parámetros: todos los valores ambientales y de contacto se declaran como supuestos, sin atribuirlos a un mercado o proveedor.
