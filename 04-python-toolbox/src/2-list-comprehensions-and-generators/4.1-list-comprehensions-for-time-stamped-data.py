import pandas as pd

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [time[11:19] for time in tweet_time]

# Print the extracted times
print(tweet_clock_time)