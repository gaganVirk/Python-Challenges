'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players)

print("First three items from list")
print(players[:3])

print("Three items from the middle of the list")
print(players[1:4])

print("Print the last three items in the list.")
print(players[-3:])
'''

fav_pizzas = ['pepperoni', 'chicken', 'beef']

friend_pizzas = fav_pizzas.copy()
print("Adding new pizza to the favorite list.")
fav_pizzas.append('new pizza')
print(fav_pizzas)
print("\n")

print("Add a different pizza to the list friend_pizzas")
friend_pizzas.append('vege')
print(friend_pizzas)
print("\n")


print("My favorite pizzas are: ")
for fav_pizza in fav_pizzas:
    print(fav_pizza)

print("\nMy friend's favorite pizzas are:")
for friend in friend_pizzas:
    print(friend)






