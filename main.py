import pandas as pd
#importamos el archivo csv con pandas
df = pd.read_csv("unit1_practice_data.csv")

#1. missing values, crear nueva columna en donde cambiamos valores nulos de cierta columna por 0
#df["nombre de la nueva columna"] = df["nombre de la columna que queremos usar de referencia"].fillna(valor que queremos darle a los valores nulos)
df["sales_filled"] = df["sales"].fillna(0)
print(df)

#2. Cleaning, remplazar valores negativos en cierta columna por NaN
#df.loc para acceder a una fila o columna especifica
#...[df["columna"] en donde el valor sea < 0 por ejemplo, "unicamente cambie el valor de la columna"]
#...] = pd.NA esto para que le asigne un valor nulo a los valores que cumplan la condicion
df.loc[df["discount"] <0, "discount"] = pd.NA 
print(df)

