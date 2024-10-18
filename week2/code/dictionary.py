#!/usr/bin/env python3

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a python script to populate a dictionary called taxa_dic derived from
# taxa so that it maps order names to sets of taxa and prints it to screen.
# 
# An example output is:
#  
# 'Chiroptera' : set(['Myotis lucifugus']) ... etc. 
# OR, 
# 'Chiroptera': {'Myotis  lucifugus'} ... etc

#### Your solution here #### 
# Create an empty dictionary 
taxa_dic = {}

# Populate the dictionary
for species, order in taxa:
    if order not in taxa_dic:
        taxa_dic[order] = set()  # Create an empty set if the order is not yet a key
    taxa_dic[order].add(species)  # Add the species to the set for the corresponding order

# Print the resulting dictionary
for order, species_set in taxa_dic.items():
    print(f"'{order}': {species_set}")

# Now write a list comprehension that does the same (including the printing after the dictionary has been created)  
 
#### Your solution here #### 

# Create the dictionary using a list comprehension
taxa_dic = {order: {species for species, ord_name in taxa if ord_name == order} for _, order in taxa}

# Print the resulting dictionary
for order, species_set in taxa_dic.items():
    print(f"'{order}': {species_set}")


