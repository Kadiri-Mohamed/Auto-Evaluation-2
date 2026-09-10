import pandas as pd 

data = pd.read_csv('clients.csv')

# print(data)
# print(type(data))
# print(data.head(2))
# print(data.tail(1))
# print(data.shape)
# print(data.columns)
# print(data.index)
# print(data.dtypes)
# print(data.info())
# print(data.describe())
# print(data["ville"].unique())
# print(data.select_dtypes(include='number'))
# print(data.select_dtypes(include='number').columns)
# print(data.select_dtypes(include='str').columns)
# print(len(data["ville"].unique()))
# print(data["ville"].nunique())

# print(data.groupby("ville")["client_id"].count())
# print(data.groupby("ville")["client_id"].count())

# print(data.isnull().sum())
# print(data.isnull().sum()[data.isnull().sum() > 0])
