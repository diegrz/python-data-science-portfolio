
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2021_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates and high temperatures form this file
	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[4])
		dates.append(current_date)
		highs.append(high)

# Plot the temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red')

# Format plot
ax.set_title("Daily high temperatures - 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()