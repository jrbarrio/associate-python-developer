squirrels_by_park = {'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None), 'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'), 'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'), 'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'), 'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'), 'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'), 'Union Square Park': ('Gray', 'Black', 'Climbing', None), 'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')}


# Remove "Madison Square Park" from squirrels_by_park
squirrels_madison = squirrels_by_park.pop("Madison Square Park")

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})

# Delete "Union Square Park" from squirrels_by_park
del squirrels_by_park["Union Square Park"]

# Print squirrels_by_park
print(squirrels_by_park)