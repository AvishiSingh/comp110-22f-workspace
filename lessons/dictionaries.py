"""Notes on dictionaries"""
#Key : value we will use to look up some definition 
#associated with a value maps
#other names: map, key value store, hashmap
#the entire dictionary can be associated with a variable

# Declaring the type of a dictionary 
schools: dict[str, int]


#Initialzize to an empty dictionary 
schools = dict()

#Set a key-value pairing in the dictionary 
schools["UNC"] = 19400 
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
print(schools)

#accesing a value by its key -- lookup 
print(f"UNC has {schools['UNC']} students")

#Remove a key-value pair from a dictionary 
#by its key 
schools.pop("Duke")

#Test for exitance of a key 
is_duke_present: bool = "Duke" in schools 
print(is_duke_present)

#Update/Reassign a key value pair 
schools["UNC"] = 20000
schools["NCSU"] += 200

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

