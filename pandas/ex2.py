import pandas as pd

data = pd.read_csv("clients.csv")

# print(data["nom"])
# print(data[["nom" , "age" , "ville"]])

# print(data.iloc[0:3])

# print(data[data["age"] > 30])

# print(data[data["salaire"] > 6000])

# print(data[data["ville"] == "Casablanca"])

# print(data[(data["sexe"] == "F") & (data["age"] > 30)])

# print(data[(data["ville"] == "Casablanca") | (data["ville"] == "Rabat")])

# print(data[(data["ville"].isin(["Casablanca" , "Rabat" , "Marrakech"]))])

# print(data[(data["age"].between(20,35))])

# print(data[~(data["ville"] == "Casablanca")])

# print(data.iloc[2 , 1])
