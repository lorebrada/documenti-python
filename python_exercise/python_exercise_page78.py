# esercizio numero 5.2 pagina 78

car = 'audi'
print(car == 'Audi')

car = 'maserati'
print(car == 'maserati')

car = 'Audi'
print(car.lower() == 'audi')


lorenzo = 'software developer'
print(lorenzo == 'software developer')

lorenzo = 'Software developer'
print(lorenzo == 'software developer')
print(lorenzo.lower() == 'software developer')


requested_fruits = 'pineapple'
if requested_fruits != 'ananas':
    print('Hold the ananas!')

age = 23
if age != 22:
    print('you are too young to do this! try again one year later.')

number = 15
if number >= 14:
    print(' you won!')
if number <= 14:
    print('you lost! try again.')
if number >= 31 and number <=35:
    print('you are a genius!')


number_0 = 14
number_1 = 33

print(number_0 >= 13 and number_1 <= 33)


age_0 = 23
age_1 = 45
print(age_0 >= 21 or age_1 <= 45)

age_2 = 34
age_3 = 76
print(age_2 <= 21 or age_3 >= 77)


name_of_people_in_party = ('giovanna', 'luciano', 'andrea', 'luca', 'elisa', 'giacomo')
print('antonio' in name_of_people_in_party)
print('giovanna' in name_of_people_in_party)

banned_people_from_party = ('filippo', 'lorenzo', 'stefano', 'lucia', 'marco', 'michele')
person = 'maria'
if person not in banned_people_from_party:
    print(f"{person.title()}, you are welcome at the party!")