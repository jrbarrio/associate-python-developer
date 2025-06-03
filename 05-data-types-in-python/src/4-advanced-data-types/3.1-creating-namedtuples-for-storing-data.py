weight_log = [('Chinstrap', 'FEMALE', 3800.0), ('Adlie', 'FEMALE', 3450.0), ('Gentoo', 'FEMALE', 4300.0), ('Adlie', 'FEMALE', 3550.0), ('Adlie', 'FEMALE', 3175.0)]

# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: SpeciesDetails
SpeciesDetails = namedtuple('SpeciesDetails', ['species', 'sex', 'body_mass'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Append a new SpeciesDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(SpeciesDetails(species, sex, body_mass))
    
print(labeled_entries[:5])