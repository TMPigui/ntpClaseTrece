import pandas as pd

#analisar los datos descriptivos de niveles de glucosa de los sgt pacientes utilizando python
paciente1=[45,120,124,150,79]
paciente2=[120,225,122,125,119,324]

#creamos el dataFrame
dataFramePac1 = pd.DataFrame({'Niveles de glucosa ': paciente1})
dataFramePac2 = pd.DataFrame({'Nieveles de glucosa ': paciente2})

#sacamos estadisticas
estadisticasDF1 = dataFramePac1.describe()
estadisticasDF2 = dataFramePac2.describe()

# Imprimir los resultados
print("Estadísticas descriptivas de los niveles de glucosa del paciente 1:")
print(f'{estadisticasDF1}')
print("\n")
print("Estadísticas descriptivas de los niveles de glucosa del paciente 2:")
print(f'{estadisticasDF2}')
