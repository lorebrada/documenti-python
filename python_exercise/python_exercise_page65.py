# esercizio numero 4.10 pagina 65

favorite_food = ['pasta', 'pizza', 'lasagne', 'pizzocheri', 'gelato']
print(favorite_food)

print("The first three items in the list are:")
print(favorite_food[0:3])

print("Three items from the middle of the list are:")
print(favorite_food[1:4])

print("The last three items from the list are:")
print(favorite_food[-3:])


# esercizio numero 4.11 

my_pizzas = ['margherita', 'prosciutto e funghi', 'diavola', 'porcini']
friend_pizzas = my_pizzas[:]

print("My favorite pizzas are:")
print(my_pizzas)

friend_pizzas.append('marinara')

print("\nMy favorite friend's pizzas are:")
print(friend_pizzas)

for pizza in my_pizzas[0:]:
    print(pizza)

for pizza in friend_pizzas[0:]:
    print(pizza)


# esercizio numero 4.12
    
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods[0:]:
    print(food)

for foods in friend_foods[0:]:
    print(foods)



# ulteriore variante dell' esercizio numero 4.12

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods[0:]:
    print(food)

for foods in friend_foods[0:]:
    print(foods)