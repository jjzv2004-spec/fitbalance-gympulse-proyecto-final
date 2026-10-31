"""Reproduce el análisis y las figuras del proyecto final desde la raíz del repositorio."""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
ruta = "data/"
os.makedirs("resultados", exist_ok=True)
df = pd.read_excel(ruta + "FitBalance_interna.xlsx", sheet_name="Datos")
GymPulse = pd.read_excel(ruta + "GymPulse_simulada.xlsx", sheet_name=0)
escenarios = pd.read_csv(ruta + "Escenarios_GEI.csv")

Freq = df["Frecuencia"].to_numpy(dtype=float)
Sev = df["Severidad"].to_numpy(dtype=float)
LDA = Freq * Sev
Freqe = GymPulse["Frecuencia_Cancelaciones_Dia"].to_numpy(dtype=float)
Seve = GymPulse["Severidad_COP_Cliente"].to_numpy(dtype=float)
LDAe = Freqe * Seve

print("Interna:", df.shape, "Externa simulada:", GymPulse.shape)
print("Rango interno:", df["Fecha"].min(), "a", df["Fecha"].max())
print("Media interna:", round(LDA.mean(), 2), "COP/día")
print("Media externa:", round(LDAe.mean(), 2), "COP/día")
print(escenarios.to_string(index=False))


resumen_fuentes = pd.DataFrame({
    "Fuente": ["FitBalance", "GymPulse simulada"],
    "Registros": [len(LDA), len(LDAe)],
    "Media_COP": [LDA.mean(), LDAe.mean()],
    "Desviacion_COP": [LDA.std(), LDAe.std()],
    "Dias_sin_cancelaciones": [np.sum(Freq == 0), np.sum(Freqe == 0)]
})
print(resumen_fuentes.round(2).to_string(index=False))
resumen_fuentes.to_csv("resultados/01_fuentes.csv", index=False)

limites = np.histogram_bin_edges(np.r_[LDA, LDAe], bins=25)
plt.figure(figsize=(9, 4))
plt.hist(LDA, bins=limites, density=True, histtype="step", label="FitBalance")
plt.hist(LDAe, bins=limites, density=True, histtype="step", label="GymPulse simulada")
plt.xlabel("Pérdida diaria (COP)")
plt.ylabel("Densidad")
plt.title("Distribución interna y escenario externo")
plt.legend()
plt.tight_layout()
plt.savefig("resultados/01_distribuciones.png", dpi=150)
plt.show()


random.seed(42)
XC_int = np.sort(np.array(random.choices(list(LDA), k=5), dtype=float))
Boxes_int = [[] for j in range(5)]
for valor in LDA:
    distancia = np.abs(XC_int - valor) / np.maximum(np.abs(XC_int), 1e-12)
    nc = int(np.argmin(distancia))
    XC_int[nc] = (XC_int[nc] + valor) / 2
    Boxes_int[nc].append(valor)

XC_integrado = XC_int.copy()
Boxes_integradas = [list(caja) for caja in Boxes_int]
aceptados_1 = []
vp_1 = []
for valor in LDAe:
    VP = np.exp(-0.5 * ((XC_integrado - valor) / np.maximum(np.abs(XC_integrado), 1e-12))**2)
    nc = int(np.argmax(VP))
    aceptado = bool(VP[nc] > 0.90)
    aceptados_1.append(aceptado)
    vp_1.append(VP[nc])
    if aceptado:
        Boxes_integradas[nc].append(valor)
        XC_integrado[nc] = (XC_integrado[nc] + valor) / 2

aceptados_1 = np.array(aceptados_1)
m1 = int(aceptados_1.sum())
print("Datos externos aceptados:", m1, "de", len(LDAe))
print("Tasa de integración:", round(100 * aceptados_1.mean(), 2), "%")
LDA_integrada_1 = np.r_[LDA, LDAe[aceptados_1]]


XD = np.column_stack([Freq, Sev])
XDe = np.column_stack([Freqe, Seve])
minimos = XD.min(axis=0)
rangos = XD.max(axis=0) - minimos
XD_escalado = (XD - minimos) / rangos
XDe_escalado = (XDe - minimos) / rangos

XC = XD_escalado[:5].copy()
for fila in XD_escalado:
    distancias = np.sqrt(np.sum((XC - fila)**2, axis=1))
    nc = int(np.argmin(distancias))
    XC[nc] = (XC[nc] + fila) / 2

aceptados_2 = []
vp_2 = []
XC_multi = XC.copy()
h = 0.10
for fila in XDe_escalado:
    distancias = np.sqrt(np.sum((XC_multi - fila)**2, axis=1))
    VP = np.exp(-0.5 * (distancias / h)**2)
    nc = int(np.argmax(VP))
    aceptado = bool(VP[nc] > 0.90)
    aceptados_2.append(aceptado)
    vp_2.append(VP[nc])
    if aceptado:
        XC_multi[nc] = (XC_multi[nc] + fila) / 2

aceptados_2 = np.array(aceptados_2)
LDA_integrada_2 = np.r_[LDA, LDAe[aceptados_2]]
print("Aceptados por dos variables:", aceptados_2.sum(), "de", len(LDAe))
print("Tasa de integración:", round(100 * aceptados_2.mean(), 2), "%")

sensibilidad_multi = []
for ancho in [0.05, 0.10, 0.20]:
    centros = XC.copy()
    cantidad = 0
    for fila in XDe_escalado:
        distancia = np.sqrt(np.sum((centros - fila)**2, axis=1))
        nc = int(np.argmin(distancia))
        if np.exp(-0.5 * (distancia[nc] / ancho)**2) > 0.90:
            cantidad += 1
            centros[nc] = (centros[nc] + fila) / 2
    sensibilidad_multi.append({"h": ancho, "Aceptados": cantidad, "Porcentaje": cantidad / len(LDAe) * 100})
sensibilidad_multi = pd.DataFrame(sensibilidad_multi)
print(sensibilidad_multi.round(2).to_string(index=False))
sensibilidad_multi.to_csv("resultados/02_sensibilidad_multidimensional.csv", index=False)


def medidas(Xi):
    media = np.mean(Xi)
    varianza = np.var(Xi)
    desviacion = np.sqrt(varianza)
    return [media, varianza, desviacion,
            np.mean((Xi - media)**3) / desviacion**3,
            np.mean((Xi - media)**4) / desviacion**4]

comparacion = pd.DataFrame({
    "Interna": medidas(LDA),
    "Modelo_1": medidas(LDA_integrada_1),
    "Modelo_2": medidas(LDA_integrada_2)
}, index=["Media", "Varianza", "Desviacion", "Asimetria", "Curtosis_Pearson"])
errores = comparacion[["Modelo_1", "Modelo_2"]].sub(comparacion["Interna"], axis=0).abs().div(comparacion["Interna"].abs(), axis=0) * 100
print(comparacion.round(4).to_string())
print("Diferencias porcentuales frente a la interna:")
print(errores.round(2).to_string())
comparacion.to_csv("resultados/03_momentos.csv")
errores.to_csv("resultados/04_discrepancias.csv")

aceptacion = pd.DataFrame({
    "Modelo": ["Pérdida agregada", "Multidimensional"],
    "Aceptados": [m1, int(aceptados_2.sum())],
    "Porcentaje": [100 * aceptados_1.mean(), 100 * aceptados_2.mean()]
})
aceptacion.to_csv("resultados/05_aceptacion.csv", index=False)
plt.figure(figsize=(8, 4))
plt.bar(aceptacion["Modelo"], aceptacion["Porcentaje"], color=["#0d9488", "#1e3a5f"])
plt.ylabel("Registros externos aceptados (%)")
plt.ylim(0, 105)
plt.title("Cada modelo aplica un criterio diferente")
plt.tight_layout()
plt.savefig("resultados/02_aceptacion.png", dpi=150)
plt.show()

trazabilidad = pd.DataFrame({"ID": ["GP_" + str(i + 1) for i in range(len(GymPulse))],
    "Pertenencia_modelo_1": vp_1, "Aceptado_modelo_1": aceptados_1,
    "Pertenencia_modelo_2": vp_2, "Aceptado_modelo_2": aceptados_2})
trazabilidad.to_csv("resultados/06_decisiones_integracion.csv", index=False)


ND = len(LDA)
NDe = len(LDAe)
uo = np.mean(LDA)
ue = np.mean(LDAe)
EPV = (ND * np.var(LDA) + NDe * np.var(LDAe)) / (ND + NDe)
uh = (ND * uo + NDe * ue) / (ND + NDe)
VHM = (ND * (uo - uh)**2 + NDe * (ue - uh)**2) / (ND + NDe)
Cr = ND / (ND + EPV / VHM) if VHM > 0 else 0.0
u_cred = Cr * uo + (1 - Cr) * uh
print("EPV (COP²):", EPV)
print("VHM (COP²):", VHM)
print("Peso de la media propia:", round(Cr * 100, 2), "%")
print("Complemento sobre la media hipotética:", round((1 - Cr) * 100, 2), "%")
print("Media ajustada:", round(u_cred, 2), "COP")


def clusterizacion(Xi):
    # Cinco semillas tomadas de los valores observados.
    valores = np.unique(Xi)
    posiciones = np.linspace(0, len(valores) - 1, 5).astype(int)
    XC = valores[posiciones].copy()
    distancias = np.abs(Xi[:, None] - valores)

    # Intercambiar medoides mientras se reduzca el costo.
    while True:
        costo = np.abs(Xi[:, None] - XC).min(axis=1).sum()
        mejor_costo = costo
        mejores_centros = XC.copy()

        for j in range(5):
            otros = np.delete(XC, j)
            distancia_otros = np.abs(Xi[:, None] - otros).min(axis=1)
            costos = np.minimum(distancias, distancia_otros[:, None]).sum(axis=0)
            candidato = int(np.argmin(costos))

            if costos[candidato] < mejor_costo - 0.000001:
                mejor_costo = costos[candidato]
                mejores_centros = XC.copy()
                mejores_centros[j] = valores[candidato]

        if mejor_costo >= costo - 0.000001:
            break
        XC = mejores_centros

    XC = np.sort(XC)
    nc = np.abs(Xi[:, None] - XC).argmin(axis=1)
    return XC, nc


con_evento = Freq > 0
Xf = Freq[con_evento]
Xs = Sev[con_evento]
XCf, ncf = clusterizacion(Xf)
XCs, ncs = clusterizacion(Xs)
lbf = ["Muy baja", "Baja", "Media", "Alta", "Muy alta"]
lbs = ["Muy baja", "Baja", "Media", "Alta", "Muy alta"]
sigmaf = np.array([np.sqrt(np.sum((XCf - v)**2) / 4) for v in XCf])
sigmas = np.array([np.sqrt(np.sum((XCs - v)**2) / 4) for v in XCs])
MP = np.outer(XCf, XCs)
ME = np.zeros((5, 5), dtype=int)
for k in range(len(Xf)):
    ME[int(ncf[k]), int(ncs[k])] += 1
MI = np.array([[1,1,1,2,2], [1,2,2,3,3], [1,2,3,3,4], [2,3,3,4,4], [2,3,4,4,5]])
print("Medoides de frecuencia:", XCf)
print("Medoides de severidad:", XCs)
print("Días con eventos en ME:", ME.sum())
plt.figure(figsize=(8, 4))
sns.heatmap(ME[::-1], annot=True, fmt="d", cmap="Blues", xticklabels=lbs, yticklabels=lbf[::-1])
plt.title("Días por grupo de frecuencia y severidad")
plt.tight_layout()
plt.savefig("resultados/03_matriz_eventos.png", dpi=150)
plt.show()


pesos = []
for k in range(len(Xf)):
    VPf = np.exp(-0.5 * ((XCf - Xf[k]) / sigmaf)**2)
    VPs = np.exp(-0.5 * ((XCs - Xs[k]) / sigmas)**2)
    pesos.append(np.outer(VPf, VPs) * ME)
pesos = np.array(pesos)
numerador = np.sum(pesos * MI * MP, axis=(1, 2))
LDAm0ref = np.zeros(len(Freq))
LDAm0ref[con_evento] = numerador / np.sum(pesos * MI, axis=(1, 2))
prospectiva = []
for escenario in escenarios.itertuples():
    NG = escenario.NG
    MG = MI.copy().astype(float)
    MG[(MG > 1) & (MG < 5)] *= NG
    LDAm5 = np.zeros(len(Freq))
    LDAm5[con_evento] = numerador / np.sum(pesos * MG, axis=(1, 2))
    bruto = max(0, (LDAm0ref.mean() - LDAm5.mean()) * escenario.Horizonte_dias)
    costo = Freq.mean() * escenario.Horizonte_dias * escenario.Costo_contacto_COP * (NG - 1)
    neto = bruto - costo
    presupuesto_gei = max(0, neto) * escenario.Fraccion_para_GEI
    TC = presupuesto_gei / escenario.Costo_tCO2e_COP
    prospectiva.append({"NG": NG, "Media_modelada_COP": LDAm5.mean(), "Bruto_horizonte_COP": bruto,
        "Costo_gestion_COP": costo, "Neto_horizonte_COP": neto,
        "Presupuesto_GEI_COP": presupuesto_gei, "Captura_financiable_tCO2e": TC,
        "Exposicion_indice": np.mean(MI / MG)})
prospectiva = pd.DataFrame(prospectiva)
print(prospectiva.round(2).to_string(index=False))
prospectiva.to_csv("resultados/07_prospectiva.csv", index=False)
mejor = prospectiva.loc[prospectiva["Neto_horizonte_COP"].idxmax()]
print("Mejor NG entre los probados, bajo estos supuestos:", mejor["NG"])

plt.figure(figsize=(8, 4))
plt.plot(prospectiva["NG"], prospectiva["Neto_horizonte_COP"] / 1e6, marker="o", color="#0d9488")
plt.xlabel("Nivel de gestión supuesto")
plt.ylabel("Neto en el horizonte (millones de COP)")
plt.title("Prospectiva con horizonte de 365 días")
plt.tight_layout()
plt.savefig("resultados/04_neto.png", dpi=150)
plt.show()


sensibilidad_gei = pd.DataFrame({"Costo_COP_tCO2e": [150000, 300000, 600000]})
sensibilidad_gei["Captura_financiable_tCO2e"] = mejor["Presupuesto_GEI_COP"] / sensibilidad_gei["Costo_COP_tCO2e"]
print(sensibilidad_gei.round(2).to_string(index=False))
sensibilidad_gei.to_csv("resultados/08_sensibilidad_GEI.csv", index=False)
contactos = Freq.mean() * 365 * (mejor["NG"] - 1)
punto_equilibrio = mejor["Bruto_horizonte_COP"] / contactos if contactos > 0 else np.nan
print("Costo de contacto de equilibrio para ese NG:", round(punto_equilibrio, 2), "COP")
plt.figure(figsize=(8, 4))
plt.bar(sensibilidad_gei["Costo_COP_tCO2e"].astype(str), sensibilidad_gei["Captura_financiable_tCO2e"], color="#1e3a5f")
plt.xlabel("Costo supuesto por tCO₂e (COP)")
plt.ylabel("Toneladas potencialmente financiables")
plt.title("Sensibilidad del presupuesto de captura")
plt.tight_layout()
plt.savefig("resultados/05_sensibilidad_GEI.png", dpi=150)
plt.show()


print("ANÁLISIS FINAL")
print(f"Las dos fuentes contienen {len(LDA)} y {len(LDAe)} registros. La diferencia de sus medias es {(ue / uo - 1) * 100:.2f}% por construcción de la simulación.")
print(f"El modelo de pérdida agregada admite {m1} registros ({aceptados_1.mean():.2%}); el multidimensional admite {aceptados_2.sum()} ({aceptados_2.mean():.2%}).")
print("La diferencia de aceptación confirma que frecuencia y severidad por separado aportan un criterio distinto del producto agregado.")
print(f"La media del conjunto integrado cambia {errores.loc['Media', 'Modelo_1']:.2f}% con el modelo 1 y {errores.loc['Media', 'Modelo_2']:.2f}% con el modelo 2.")
print(f"En credibilidad, Cr es {Cr:.2%} y el complemento sobre la media hipotética es {1-Cr:.2%}. Estos pesos no evalúan veracidad de las bases.")
print(f"En la prospectiva, NG={mejor['NG']:.1f} obtiene el mayor neto entre los escenarios: COP {mejor['Neto_horizonte_COP']:,.2f} en 365 días.")
print(f"Destinar el 10% del neto positivo a captura, a COP 300.000 por tonelada, permitiría financiar {mejor['Captura_financiable_tCO2e']:,.2f} tCO2e en el escenario.")
print("Se recomienda validar costos de contacto y respuesta real de retención en un piloto temporal antes de ampliar la gestión.")
print("Se debe medir por separado la captura física y completar el diseño de un proyecto ambiental verificable.")
print("La similitud de las fuentes responde a su calibración. Se necesita una fuente externa independiente para evaluar generalización.")
