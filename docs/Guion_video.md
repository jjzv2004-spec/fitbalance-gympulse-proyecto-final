# Guion del video y presentación

Juan José Zapata y Juanita Pineda. Video de apoyo con narración sintética. Para una exposición personal pueden repartirse las diapositivas 1–6 y 7–12. Duración objetivo aproximada: 7–9 minutos, siempre menor a 10.

## Diapositiva 1: FitBalance y GymPulse

Somos Juan José Zapata y Juanita Pineda. Presentamos el proyecto final de integración de datos y prospectiva aplicado a FitBalance Gym y GymPulse. La pregunta es cómo cambia la caracterización de las pérdidas por cancelaciones al incorporar un escenario externo comparable, y qué presupuesto podría financiar captura de gases de efecto invernadero bajo diferentes niveles de gestión. Trabajamos con empresas ficticias. Desde el inicio distinguimos los registros de referencia, la base externa simulada y los supuestos de los escenarios. Esta separación es necesaria para interpretar correctamente los resultados y no confundir una simulación académica con evidencia de una operación real.

## Diapositiva 2: Dos fuentes y una base de escenarios

La base interna tiene mil doscientos registros diarios. Cada fila contiene fecha, sede, plan, motivo, frecuencia de cancelaciones y severidad en pesos colombianos por cliente. La pérdida diaria es frecuencia por severidad. GymPulse tiene la misma cantidad de registros y columnas comparables. Su severidad se construyó con un incremento del tres por ciento sobre pares internos y un orden calibrado, de modo que no es una fuente independiente. Una tercera base define niveles de gestión, horizonte, costo por contacto, proporción del presupuesto ambiental y costo por tonelada. La trazabilidad identifica qué fila interna origina cada par externo simulado.

## Diapositiva 3: Dos modelos del curso, dos criterios

Aplicamos dos modelos de integración vistos en clase. El primero reproduce la pertenencia sobre pérdida agregada, con cinco concentradores, distancia relativa, actualización secuencial y umbral superior a cero coma noventa. El segundo adapta la integración multidimensional y evalúa frecuencia y severidad por separado. Escalamos las dos variables con parámetros internos para que la moneda no domine la distancia. A ese segundo ejercicio agregamos un filtro gaussiano explícito y analizamos su sensibilidad. Los centros de estos modelos se actualizan por promedios secuenciales, por lo que no los llamamos medoides. La etapa de caracterización difusa sí utiliza PAM con observaciones reales.

## Diapositiva 4: La cobertura cambia con el criterio

El primer modelo acepta mil ciento cuarenta de los mil doscientos registros externos, equivalente al noventa y cinco por ciento. Ese valor fue un objetivo de calibración. El modelo multidimensional acepta doscientos doce, aproximadamente diecisiete coma sesenta y siete por ciento, con ancho cero coma diez. No forzamos ese segundo resultado a noventa y cinco. La sensibilidad muestra que su aceptación pasa de tres coma veinticinco a sesenta y nueve coma setenta y cinco por ciento al ampliar el ancho de cero coma cero cinco a cero coma veinte. Esto muestra que cobertura y selectividad dependen de los parámetros, y no equivalen a precisión predictiva.

## Diapositiva 5: Una media cercana no iguala las colas

Para comparar los conjuntos usamos los momentos de las observaciones sin agrupar. La media cambia cero coma cincuenta y seis por ciento con el primer modelo y cuatro coma cuarenta y cinco por ciento con el segundo. Sin embargo, el primer modelo presenta una diferencia de curtosis cercana al dieciséis por ciento. Esto impide concluir que las distribuciones sean equivalentes solo porque sus promedios son cercanos. La tabla también compara varianza, desviación y asimetría. Como GymPulse depende de la base interna, los resultados describen un escenario calibrado. No son una evaluación de generalización con datos independientes.

## Diapositiva 6: La credibilidad asigna pesos a medias

La teoría de credibilidad se incluye como contraste adicional, con la fórmula simplificada trabajada en clase. El peso de la media propia es aproximadamente veinticuatro coma cuarenta y nueve por ciento y el complemento sobre la media hipotética es setenta y cinco coma cincuenta y uno por ciento. Ese complemento no pesa directamente una auditoría de calidad de GymPulse. Tampoco significa que esa base sea verdadera en ese porcentaje. EPV y VHM son varianzas expresadas en pesos cuadrados. Además, al tratarse de fuentes dependientes por construcción, el cálculo se presenta como demostración del método y no como una aplicación actuarial independiente.

## Diapositiva 7: PAM caracteriza el riesgo interno

Para la caracterización difusa usamos únicamente la base interna. Separamos veinte días sin cancelaciones y mantenemos su pérdida en cero. Los mil ciento ochenta días con eventos forman la matriz de frecuencias. PAM produce cinco medoides observados de frecuencia: dos, tres, cuatro, cinco y ocho cancelaciones por día. También obtenemos cinco medoides de severidad. Con las funciones gaussianas de clase construimos pertenencias y una matriz de pérdidas. La matriz de impacto contiene reglas cualitativas entre uno y cinco. Estas reglas ayudan a comparar combinaciones de frecuencia y severidad, pero no son probabilidades de cancelación ni etiquetas predictivas validadas.

## Diapositiva 8: La referencia de gestión es NG = 1

La prospectiva compara cada escenario contra la misma referencia de gestión, con nivel igual a uno. La matriz de gestión modifica las celdas intermedias de impacto, siguiendo la lógica del ejercicio de clase. El horizonte es de trescientos sesenta y cinco días y supone que el promedio histórico se mantiene constante. Para la gestión incremental se usa un costo supuesto de treinta mil pesos por contacto. El ahorro bruto compara pérdidas modeladas con y sin gestión; no se calcula restando la pérdida observada a la estimación difusa. El efecto de aumentar el nivel está impuesto por la fórmula, de modo que no prueba una eficacia real de retención.

## Diapositiva 9: NG = 2 logra el mayor neto probado

Entre los cinco niveles evaluados, el nivel dos obtiene el mayor valor neto bajo los supuestos del proyecto. La reducción bruta modelada para el horizonte es de aproximadamente doscientos sesenta y seis coma cincuenta y cuatro millones de pesos. Se descuenta un costo incremental cercano a cuarenta y siete coma catorce millones, para un neto de doscientos diecinueve coma cuarenta millones. Esta cifra es una prospectiva hipotética, no un ahorro realizado. La elección depende del costo por contacto y de la forma de la matriz de gestión. Por eso proponemos un piloto que mida respuesta real antes de convertir el escenario en un presupuesto operativo.

## Diapositiva 10: 73,13 tCO₂e potencialmente financiables

El proyecto destina un diez por ciento del neto positivo a un presupuesto ambiental. En el mejor escenario, serían aproximadamente veintiún coma noventa y cuatro millones de pesos. Con un costo supuesto de trescientos mil pesos por tonelada, ese presupuesto podría financiar cerca de setenta y tres coma trece toneladas de captura. Si el costo por tonelada se duplica, la capacidad se reduce a la mitad. No afirmamos que el gimnasio haya capturado esas toneladas. Para demostrar captura física hacen falta tecnología, medición, adicionalidad y verificación ambiental. Aquí caracterizamos una capacidad financiera prospectiva y mantenemos el costo como un supuesto editable.

## Diapositiva 11: Tres decisiones para continuar

Los resultados permiten proponer tres decisiones. Primero, ejecutar un piloto de retención que mida costo de contacto, cancelaciones y resultados de gestión con una comparación temporal adecuada. Segundo, conseguir una fuente externa independiente para evaluar si las relaciones se mantienen fuera de la base calibrada. Tercero, seleccionar un proyecto ambiental con metodología verificable antes de atribuir captura de carbono. También es necesario revisar las colas de la distribución, porque la media no resume todo el riesgo. Estas decisiones convierten el ejercicio de integración y prospectiva en un plan de validación, sin presentar sus supuestos como resultados empíricos.

## Diapositiva 12: El portafolio permite reproducir el análisis

El portafolio reúne las bases, el diccionario de variables, la trazabilidad de la simulación y los supuestos de prospectiva. El notebook contiene resultados y gráficas calculados, y el script reproduce el análisis sin depender de Drive. Las pruebas verifican la correspondencia de los datos, las decisiones de aceptación y la aritmética del presupuesto ambiental. El repositorio y el enlace de Colab permiten revisar el trabajo. En conclusión, demostramos dos métodos de integración y una prospectiva financiera para GEI, manteniendo claras las limitaciones de la calibración. La narración de este video es sintética de apoyo y no corresponde a las voces de los integrantes.
