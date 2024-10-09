# set = collection which is unordered, unindexed. No duplicated values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("spoon")
utensils.clear()

# union two sets
dishes.update(utensils)
dinner_table = utensils.union(dishes)

# difference
print(utensils.difference(dishes))
print(dishes.difference(utensils))

# intersection
print(utensils.intersection(dishes))
print(dishes.intersection(utensils))

for x in utensils:
    print(x)
