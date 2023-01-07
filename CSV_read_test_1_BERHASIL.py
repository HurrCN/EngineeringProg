import pandas as pd

url = "https://raw.githubusercontent.com/HurrCN/Numerical_Method/MyProject/Salary_1.csv"
label = ['index', 'salary']
dataset = pd.read_csv(url, names=label, sep=';')
print(dataset.head(9))