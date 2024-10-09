# dictionary    = a changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

capital = {
    'USA': "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# update
capital["Germany"] = "Berlin"
capital.update({"Germany": 'Berlin'})

# remove
capital.pop('China')

# remove all
capital.clear()

print(capital['Germany'])
print(capital.get('Germany'))
print(capital.keys())
print(capital.values())
print(capital.items())

for key, value in capital.items():
    print(key, ":", value)
