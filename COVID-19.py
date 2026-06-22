import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("covid_19_clean_complete.csv")

print(df.head())

df['Date'] = pd.to_datetime(df['Date'])

daily_data = df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum()

print("\nDaily Data:")
print(daily_data.head())

plt.figure(figsize=(12,6))
plt.plot(daily_data.index, daily_data['Confirmed'])
plt.title("COVID-19 Confirmed Cases")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,6))
plt.plot(daily_data.index, daily_data['Deaths'])
plt.title("COVID-19 Death Cases")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,6))
plt.plot(daily_data.index, daily_data['Recovered'])
plt.title("COVID-19 Recovery Cases")
plt.xlabel("Date")
plt.ylabel("Recovered Cases")
plt.xticks(rotation=45)
plt.show()