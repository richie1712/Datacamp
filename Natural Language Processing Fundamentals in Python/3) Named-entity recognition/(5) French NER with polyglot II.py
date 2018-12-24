# Create the list of tuples: entities

entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]



# Print the entities

print(entities)