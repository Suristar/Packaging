import pandas as pd
df = pd.read_csv("c:/users/s_baruah/desktop/data-1.csv")
df.head()

from matplotlib import pyplot as plt
plt.scatter(df['var1'], df['var2'])
plt.show()

df.describe()


#df['d1'] = ((df['var1'] - (-10))**2) + ((df['var2'] - (-4.25))**2)
#df['d2'] = ((df['var1'] - (-6.3))**2) + ((df['var2'] - (-8.6))**2)
#df['d3'] = ((df['var1'] - (-1.14))**2) + ((df['var2'] - (4.23))**2)

#df['class'] = df[['d1', 'd2', 'd3']].idxmin(axis=1)

df[1] = ((df['var1'] - (-10))**2) + ((df['var2'] - (-4.25))**2)
df[2] = ((df['var1'] - (-6.3))**2) + ((df['var2'] - (-8.6))**2)
df[3] = ((df['var1'] - (-1.14))**2) + ((df['var2'] - (4.23))**2)

df['class'] = df[[1, 2, 3]].idxmin(axis=1)
print(df.head(30))

plt.scatter(df['var1'], df['var2'], c=df['class'])
plt.show()