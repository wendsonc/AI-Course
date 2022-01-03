# -*- coding: utf-8 -*-
"""Correlação.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wY9bR-nW9ZxXGtum2XefJ3Dpea1ugcbq
"""

import pandas as pd
import seaborn as sn

data = pd.read_csv("winequality-red.csv")
print(data)

# Análise de correlação

correlation = data.corr()
correlation

# Plot da matriz de correlação
try:
   plot = sn.heatmap(correlation, annot = True, fmt=".1f", linewidths=.6)
   plot
except ValueError:  
    pass

from google.colab import drive
drive.mount('/content/drive')