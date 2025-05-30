girl_names = ['Jada', 'Emily', 'Ava', 'Serenity', 'Claire', 'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 'Zoe', 'Leah', 'Hailey', 'Ava', 'Olivia', 'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Chloe', 'Fatoumata']
boy_names = ['Josiah', 'Ethan', 'David', 'Jayden', 'Mason', 'Ryan', 'Christian', 'Isaiah', 'Jayden', 'Michael', 'Noah', 'Samuel', 'Sebastian', 'Noah', 'Dylan', 'Lucas', 'Joshua', 'Angel', 'Jacob', 'Matthew', 'Josiah', 'Jacob', 'Muhammad', 'Alexander', 'Jason']

# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')