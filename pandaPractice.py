import pandas as pd

#cargamos datos
tabla = pd.read_csv("./data/empleados.csv")

#primeros 5 registros
print(tabla.head())
print("\n")

#ultimos 5 o si ponemos 10 los ultimos 10
print(tabla.tail(5))
print("\n")

#Estadisticas
print(tabla.describe())
print("\n")

#accedemos a la columna nom y a los primeros 5 registros
print(tabla["nombres"].head(10))
print("\n")

#accedmos a la posicion en la tabla 12 hasta una menos de la 20
print(tabla.iloc[12:20])
#Y con este accedemos solo a las posiciones 12 y 20 y a los nombres nada mas
print(tabla.loc[[12,20],["nombres"]])
print("\n") 

#Para filtar con un condicional en este caso con la edad siendo mayor a 50
print(tabla[tabla["edad"]>50])


#mostramos todos los nombres
print(tabla["nombres"].to_string())