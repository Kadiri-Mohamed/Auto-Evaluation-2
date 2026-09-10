import pandas as pd

data = pd.read_csv("clients.csv")

# print(data.info())
# print(data.head())
# print(data.describe())

# print(data.isnull().sum() > 0)
# print(data.duplicated().sum() > 0)

# print(data.isnull().sum()[data.isnull().sum() > 0])

# print(data[data.duplicated()])

# data = data.drop_duplicates()

# print(data)


# data["name"] = data["name"].str.strip()

# data["ville"] = data["ville"].str.strip()

# data["ville"] = data["ville"].str.strip().str.title()

# print(data)

# data = data.replace("N/A", pd.NA)

# print(data)

# data["age"] = pd.to_numeric(data["age"], errors="coerce")

# data["salaire"] = data["salaire"].astype(str)
# data["salaire"] = data["salaire"].str.strip()

# data["salaire"] = data["salaire"].str.replace("DH", "")

# print(data[data["salaire"] < 0])


# data.loc[data["salaire"] < 0, "salaire"] = pd.NA