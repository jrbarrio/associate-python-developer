# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: SpeciesDetails
SpeciesDetails = namedtuple('SpeciesDetails', ['species', 'sex', 'body_mass'])

labeled_entries = [SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5500.0), SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4300.0), SpeciesDetails(species='Adlie', sex='MALE', body_mass=3800.0), SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5800.0), SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4100.0), SpeciesDetails(species='Adlie', sex='MALE', body_mass=3975.0), SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5400.0), SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4800.0), SpeciesDetails(species='Chinstrap', sex='FEMALE', body_mass=3800.0), SpeciesDetails(species='Adlie', sex='FEMALE', body_mass=3450.0), SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=3950.0), SpeciesDetails(species='Gentoo', sex='MALE', body_mass=5250.0), SpeciesDetails(species='Gentoo', sex='FEMALE', body_mass=4300.0), SpeciesDetails(species='Gentoo', sex='MALE', body_mass=4925.0), SpeciesDetails(species='Adlie', sex='FEMALE', body_mass=3550.0), SpeciesDetails(species='Adlie', sex='MALE', body_mass=3950.0), SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=3800.0), SpeciesDetails(species='Chinstrap', sex='MALE', body_mass=4050.0), SpeciesDetails(species='Adlie', sex='MALE', body_mass=3650.0), SpeciesDetails(species='Adlie', sex='FEMALE', body_mass=3175.0)]

# Iterate over the first twenty entries in labeled_entries
for entry in labeled_entries[0:20]:
    # if the entry's species equals Chinstrap
    if entry.species == 'Chinstrap':
      # Print each entry's sex and body_mass seperated by a colon
      print(f'{entry.sex}:{entry.body_mass}')