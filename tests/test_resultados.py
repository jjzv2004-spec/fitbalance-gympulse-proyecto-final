import unittest
import numpy as np
import pandas as pd
from pathlib import Path

class TestPortafolio(unittest.TestCase):
    def test_fuentes(self):
        a=pd.read_excel('data/FitBalance_interna.xlsx',sheet_name='Datos')
        b=pd.read_excel('data/GymPulse_simulada.xlsx')
        t=pd.read_csv('data/Trazabilidad_simulacion.csv')
        self.assertEqual(len(a),1200);self.assertEqual(len(b),1200)
        self.assertTrue(np.allclose(a.Frecuencia*a.Severidad,a.LDA))
        orig=a.iloc[t.Fila_interna_origen.to_numpy()-1]
        self.assertTrue(np.array_equal(b.Frecuencia_Cancelaciones_Dia,orig.Frecuencia))
        self.assertTrue(np.allclose(b.Severidad_COP_Cliente,np.round(orig.Severidad.to_numpy()*1.03,2)))
    def test_integracion(self):
        d=pd.read_csv('resultados/06_decisiones_integracion.csv')
        self.assertEqual(len(d),1200)
        self.assertEqual(int(d.Aceptado_modelo_1.sum()),1140)
        self.assertEqual(int(d.Aceptado_modelo_2.sum()),212)
        for n in [1,2]:
            vp=d[f'Pertenencia_modelo_{n}']
            self.assertTrue(vp.between(0,1).all())
            self.assertTrue(np.array_equal(vp>.90,d[f'Aceptado_modelo_{n}']))
    def test_prospectiva(self):
        p=pd.read_csv('resultados/07_prospectiva.csv')
        self.assertTrue(np.isfinite(p.to_numpy()).all())
        self.assertAlmostEqual(float(p.iloc[0].Neto_horizonte_COP),0)
        self.assertAlmostEqual(float(p.iloc[0].Captura_financiable_tCO2e),0)
        self.assertTrue((np.diff(p.Media_modelada_COP)<=0).all())
        self.assertTrue(np.allclose(p.Neto_horizonte_COP,p.Bruto_horizonte_COP-p.Costo_gestion_COP))
        self.assertTrue(np.allclose(p.Presupuesto_GEI_COP,np.maximum(p.Neto_horizonte_COP,0)*.1))
        self.assertTrue(np.allclose(p.Captura_financiable_tCO2e,p.Presupuesto_GEI_COP/300000))

if __name__=='__main__': unittest.main()
