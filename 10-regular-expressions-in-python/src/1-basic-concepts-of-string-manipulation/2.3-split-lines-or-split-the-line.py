file = """mtv films election, a high school comedy, is a current example
from there, director steven spielberg wastes no time, taking us into the water on a midnight swim"""

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(sep=",")
    print(substring_split)