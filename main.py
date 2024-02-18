import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv("country.csv")
file2 = pd.read_csv("country2.csv")
plt.bar(file['cont'],file['AQI'])
# Adding labels and title
plt.xlabel('Country')
plt.ylabel('AQI')
plt.title('AQI Comparison between India and China')
plt.xticks(rotation=90)

plt.show()
