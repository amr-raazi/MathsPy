from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

working_hours = {"Australia": 1712.0, "Austria": 1501.0, "Belgium": 1583.0, "Canada": 1670.0, "Chile": 1914.4,
                 "Costa Rica": 2059.6, "Czech Republic": 1788.0, "Denmark": 1380.0, "Estonia": 1711.0,
                 "Finland": 1540.0, "France": 1505.0, "Germany": 1386.1, "Greece": 1949.0, "Hungary": 1725.2,
                 "Iceland": 1454.0, "Ireland": 1772.0, "Israel": 1898.1, "Italy": 1717.8, "Japan": 1644.0,
                 "South Korea": 1967.0, "Latvia": 1661.0, "Lithuania": 1635.0, "Luxembourg": 1506.0, "Mexico": 2137.0,
                 "Netherlands": 1434.0, "New Zealand": 1779.0, "Norway": 1384.0, "Poland": 1806.0,
                 "Portugal": 1719.0, "Russia": 1965.0, "Slovakia": 1695.0, "Slovenia": 1592.9,
                 "Spain": 1686.0, "Sweden": 1452.0, "Switzerland": 1556.9, "United Kingdom": 1538.0,
                 "United States": 1779.0}
happiness = pd.read_csv("Happiness data.csv").set_index("Country")

y = list(working_hours.values())
x = [happiness.loc[a, "Score"] for a in working_hours.keys()]
n = working_hours.keys()

plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "b--")
plt.title(f"Happiness to working hours for OECD countries, Pearson coefficient={str(np.corrcoef(x, y)[0][1])[:7]}")
plt.xlabel("Happiness Score")
plt.ylabel("Hours worked")
for i, txt in enumerate(n):
    if not i % 9:
        plt.annotate(txt, (x[i], y[i]))

plt.savefig("plot.jpg")
plt.show()
