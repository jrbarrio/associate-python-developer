# Import matplotlib
import matplotlib.pyplot as plt
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('./06-working-with-dates-and-times-in-python/data/capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])

# Show the results
plt.show()