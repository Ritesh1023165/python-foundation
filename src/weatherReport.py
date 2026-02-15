import requests
import pandas as pd
import matplotlib.pyplot as plt
from utils import getPastDateFromDays
from config import OUTPUT_DATA_DIR


# Calculate dates
start_date = getPastDateFromDays(7)
end_date = getPastDateFromDays(0)

latitude=15.849695
longitude=74.497673

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Belgaum Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot  
plt.savefig(OUTPUT_DATA_DIR/'weather_chart.png')
plt.show()

# ----------------------------------------



# Save to CSV
df.to_csv(OUTPUT_DATA_DIR/'Belgaum_weather.csv', index=False)
print("Data saved to data/Belgaum_weather.csv")