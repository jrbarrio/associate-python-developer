# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('./06-working-with-dates-and-times-in-python/data/capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])