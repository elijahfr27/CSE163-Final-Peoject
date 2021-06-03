import pandas as pd
import matplotlib.pyplot as plt
import os
from IPython.display import display


datasets = dict()

for filename in os.listdir('data'):
    path = os.path.join('data', filename)
    with open(path) as f:
        data = pd.read_csv(f)
        datasets[filename[:-4]] = data


for key, value in datasets.items():
    print(key)


df = datasets['14-15_grad']
print(df.columns)