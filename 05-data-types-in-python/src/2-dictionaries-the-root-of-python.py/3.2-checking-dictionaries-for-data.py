squirrels_by_park = {'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None), 'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'), 'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'), 'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'), 'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'), 'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'), 'Union Square Park': ('Gray', 'Black', 'Climbing', None), 'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')}

# Check to see if Tompkins Square Park is in squirrels_by_park
if "Tompkins Square Park" in squirrels_by_park:
    # Print 'Found Tompkins Square Park'
    print('Found Tompkins Square Park')
    
# Check to see if Central Park is in squirrels_by_park
if "Central Park" in squirrels_by_park:
    # Print 'Found Central Park' if found
    print('Found Central Park')
else:
    # Print 'Central Park missing' if not found
    print('Central Park missing')