# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('./06-working-with-dates-and-times-in-python/data/capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.day_name()

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())