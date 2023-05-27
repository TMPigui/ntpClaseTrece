#De esta manera importamos los arreglos que estan en data
from data.apartamentos import apartamento1,apartamento2
import pandas as pd
from helpers.crearTablasHTML import crearTabla

#crear dataFrame
tabla1 = pd.DataFrame(apartamento1, columns=['edades'])
tabla2 = pd.DataFrame(apartamento2, columns=['edades'])
tabla3 = pd.read_csv("./data/empleados.csv")

#efectuando filtros con python 

#1 Definir una condicion logica
empleadosJovenes = tabla3.query('edad<30 and cargo=="analista1"' )
empleadosSalariosBajo = tabla3.query('salario < 5000000 and cargo == "analista2"')
empleadosAdDespedir = tabla3.query('edad >= 50')

# 2Creamos la tabla html con el dataframe del filtro
crearTabla(empleadosJovenes, "tablaJoves")
crearTabla(empleadosSalariosBajo, "salarosBajos")
crearTabla(empleadosAdDespedir, "empleadosADespedir")
