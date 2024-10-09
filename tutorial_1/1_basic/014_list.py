# list = used to store multiple items in a single valuable

food = ["pizza", "hamburger", "hotdog", "spaghatti", "pudding"]

food[0] = "sushi"

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(3, "cake")
food.sort()
food.clear()

for item in food:
    print(item)


# 2D lists = a list of lists
drink = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drink, dinner, dessert]

print(food[1][1])
