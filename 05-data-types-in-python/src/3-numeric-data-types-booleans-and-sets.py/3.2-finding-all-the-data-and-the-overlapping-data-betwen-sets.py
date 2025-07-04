female_penguin_species = {'Chinstrap', 'Gentoo', 'Adlie'}
male_penguin_species = {'Gentoo', 'Adlie'}

# Find the union: all_species
all_species = female_penguin_species.union(male_penguin_species)

# Print the count of names in all_species
print(len(all_species))

# Find the intersection: overlapping_species
overlapping_species = female_penguin_species.intersection(male_penguin_species)

# Print the count of species in overlapping_species
print(len(overlapping_species))