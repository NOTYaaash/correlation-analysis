import pandas as pd
import numpy as np
df_x = pd.read_csv(dataset1)#put dataset path
df_y = pd.read_csv(dataset2)
if len(df_x) != len(df_y):
  print("DataFrames have diffrennt lengths.")
  exit()
column_name_x = "columnx"
column_name_y = "columny"
correlation_coefficient = np.corrcoef(df_x[column_name_x], df_y[column_name_y])[0, 1]
print(f"Correlation coefficient between {column_name_x} and {column_name_y} is: {correlation_coefficient}")
import matplotlib.pyplot as plt
#scaterplot
plt.scatter(df_x[column_name_x], df_y[column_name_y])
plt.xlabel(column_name_x)
plt.ylabel(column_name_y)
plt.title(f"Scatter Plot: {column_name_x} vs. {column_name_y}")
plt.show()
#heatmap 
correlation_matrix = df_x.corr()
plt.imshow(correlation_matrix)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()