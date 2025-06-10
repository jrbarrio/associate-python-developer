# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('./06-working-with-dates-and-times-in-python/data/capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())