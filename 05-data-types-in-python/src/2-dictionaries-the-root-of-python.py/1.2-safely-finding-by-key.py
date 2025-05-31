squirrels_by_park = {'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None), 'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'), 'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'), 'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'), 'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'), 'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'), 'Union Square Park': ('Gray', 'Black', 'Climbing', None), 'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')}

# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get('Union Square Park'))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get('Fort Tryon Park')))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get('Central Park', 'Not Found'))