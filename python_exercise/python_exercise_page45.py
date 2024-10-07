#esercizio numero 3.8 pagina 45

places = ['iceland', 'norway', 'sweden', 'belgium', 'portugal']
print(places)


places = ['iceland', 'norway', 'sweden', 'belgium', 'portugal']
print("\nHere is the original sorted list of places:")
print(sorted(places))


places = ['iceland', 'norway', 'sweden', 'belgium', 'portugal']
print("\nHere is the original list of places, again:")
print(places)


places = ['iceland','norway', 'sweden', 'belgium', 'portugal']
places.sort(reverse=True)
print(places)

places = ['iceland', 'norway', 'sweden', 'belgium', 'portugal']
print("\nHere is the original list of places, again:")
print(places)


places = ['iceland', 'norway', 'sweden', 'belgium', 'portugal']
print(places)
places.reverse()
print(places)
places.reverse()
print(places)


places = ['iceland', 'norway', 'sweden', 'belgium', 'portugal']
places.sort()
print(places)
places.sort(reverse=True)
print(places)


#esercizio numero 3.9

dinner = ['Ilaria', 'Lorenzo']
invite = dinner.pop(0)
print(f"You are still invited to dinner, {invite.title()}.")
invite = dinner.pop(-1)
print(f"You are still invited to dinner, {invite.title()}.")

dinner = ['Ilaria', 'Lorenzo']

dinner.remove('Lorenzo')
print(dinner)
dinner.remove('Ilaria')
print(dinner)

print(len(dinner))


#esercizio numero 3.10

list = ['monte rosa', 'monte bianco', 'monte bernina', 'monte cevedale', 'monte cervino']
print(list)
print(len(list))
list.sort()
print(list)


list = ['monte rosa', 'monte bianco', 'monte bernina', 'monte cevedale', 'monte cervino']
list.reverse()
print(list)


list = ['monte rosa', 'monte bianco', 'monte bernina', 'monte cevedale', 'monte cervino']
list.sort(reverse=True)
print(list)


list = ['monte rosa', 'monte bianco', 'monte bernina', 'monte cevedale', 'monte cervino']
print("\nHere is the sorted list")
print(sorted(list))

