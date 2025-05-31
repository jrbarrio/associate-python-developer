squirrels = [('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)), ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')), ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')), ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')), ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')), ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')), ('Union Square Park', ('Gray', 'Black', 'Climbing', None)), ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]

# Create an empty dictionary: squirrels_by_park
squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrel_details
    
# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park and its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')