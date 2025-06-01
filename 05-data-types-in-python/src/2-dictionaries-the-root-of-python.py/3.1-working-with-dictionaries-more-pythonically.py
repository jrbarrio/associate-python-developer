squirrels_by_park = {'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None), 'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'), 'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'), 'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'), 'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'), 'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'), 'Union Square Park': ('Gray', 'Black', 'Climbing', None), 'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')}


# Iterate over the first squirrel entry in the Madison Square Park list
for field, value in squirrels_by_park["Madison Square Park"][0].items():
    # Print field and value
    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Union Square Park list
for field, value in squirrels_by_park["Union Square Park"][1].items():
    # Print field and value
    print(field, value)