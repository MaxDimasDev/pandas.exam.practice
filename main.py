import pandas as pd
#importamos el archivo csv con pandas
df = pd.read_csv("unit1_practice_data.csv")

#1. missing values, crear nueva columna en donde cambiamos valores nulos de cierta columna por 0
#df["nombre de la nueva columna"] = df["nombre de la columna que queremos usar de referencia"].fillna(valor que queremos darle a los valores nulos)
df["sales_filled"] = df["sales"].fillna(0)
print(df)