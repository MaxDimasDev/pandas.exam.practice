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

#3. Limpiar datos donde no hay datos en ambas filas de ciertas columnas
#df = df.dropna() se usa para eliminar filas donde hay valores nulos
#...(subset = ["nombre de las columna"],) al usar subset le especificamos que se fije en ciertas columnas unicamente
#...(,how = "all") le especificamos que se elimine la filas solo si los valores de ambas columnas especificadas son nulos
df = df.dropna(subset=["sales", "discount"], how="all")
print(df)

#4. Filtering, buscar filas en donde 2 columnas tienen valores especificos
#df[(...)]le especificamos de donde queremos buscar los valores
#(df["region"] == "west") & (df["sales"].isna()) aqui le damos nuestras condicionales, en este caso que la region sea west y que la columna de sales tenga valores nulos
df[(df["region"] == "west") & (df["sales"].isna())]
print(df)

#5. filling, reemplazar valores faltantes de discount con la media
#df["discount"] le decimos que de la columna de discount
#... = df["discount"].fillna(df["discount"].mean()) saque la media de los datos en discount y los espacios vacios los llene con la media
df["discount"] = df["discount"].fillna(df["discount"].mean())
print(df)

#6. new columns, calcular net_sales solo si sales y discount no son NaN
#df.loc[...] usamos para seleccionar filas y columnas específicas
#...[df["sales"].notna() & df["discount"].notna()] condición: que AMBAS columnas NO tengan valores nulos
#..., "net_sales"] especificamos que queremos crear/actualizar esta columna
#... = df["sales"] * (1 - df["discount"]/100) fórmula para calcular el valor neto (sales - descuento)
df.loc[df["sales"].notna() & df["discount"].notna(), "net_sales"] = df["sales"] * (1 - df["discount"]/100)
print(df)

#7. filtering, filtrar: sales ≥ 200 y discount ≤ 10
#df[(...)] filtramos el dataframe completo
#...(df["sales"] >= 200) primera condición: ventas mayores o iguales a 200
#... & operador AND para combinar condiciones
#...(df["discount"] <= 10) segunda condición: descuentos menores o iguales a 10%
df[(df["sales"] >= 200) & (df["discount"] <= 10)]
print(df)

#8. dates and sorting, filtrar por sales no nulo y ordenar por order_date descendente
#df[df["sales"].notna()] primero filtramos solo filas donde sales NO es nulo
#....sort_values("order_date", ascending=False) luego ordenamos por fecha descendente (más reciente primero)
df[df["sales"].notna()].sort_values("order_date", ascending=False)
print(df)

#9. value conversion, convertir fecha a datetime y extraer el nombre del día
#df["order_date"] = pd.to_datetime(df["order_date"]) convierte la columna a tipo datetime
#df["weekday"] = df["order_date"].dt.day_name() crea nueva columna con nombre del día (lunes, martes...)
df["order_date"] = pd.to_datetime(df["order_date"])
df["weekday"] = df["order_date"].dt.day_name()
print(df)

#10. dropping, eliminar columnas con todos los valores faltantes
#df = df.dropna(axis=1, how="all") 
#...axis=1 indica que trabajamos con COLUMNAS (no filas)
#...how="all" solo elimina columnas donde TODOS los valores son nulos
df = df.dropna(axis=1, how="all")
print(df)