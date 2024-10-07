# Esercizio numero 6.7 pagina 111

person_0 = {'first name': 'samuele', 'last name': 'bradanini', 'age': '19 years old', 'city': 'villa guardia'}
person_1 = {'first name': 'lorenzo', 'last name': 'bradanini', 'age': '23 years old', 'city': 'villa guardia'}
person_2 = {'first name' : 'davide', 'last name': 'ciavarella', 'age': '23 years old', 'city': 'villa guardia'}

people = [person_0, person_1, person_2]

for person in people:
    print(person)


# esercizio numero 6.8
    
pet_0 = {'animal name': 'cat', 'name of the owner': 'matilde'}
pet_1 = {'animal name': 'dog', 'name of the owner': 'luca'}
pet_2 = {'animal name': 'rabbit', 'name of the owner': 'andrea'}
pet_3 = {'animal name': 'guinea pig', 'name of the owner': 'lucia'}
pet_4 = {'animal name': 'fish', 'name of the owner': 'giacomo'}

pets= [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(pet)


# esercizio numero 6.9
    
favorite_places = {
    'anna': ['santorini', 'sicily', 'milan'],
    'giovanni': ['new york', 'switzerland', 'istambul'],
    'luca': ['venezuela', 'london', 'shanghai'],
    'alessia': ['pisa', 'china', 'stockholm'],
    'silvia': ['berlin', 'barcelona', 'los angeles'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")


# esercizio numero 6.10
        
favorite_numbers = {
    'lorenzo': ['1', '2', '44', '3566'],
    'Sara': ['24', '454', '363', '25'],
    'Andrea': ['36', '56363', '15', '19'],
    'Giovanni': ['4', '78', '64', '18'],
    'Davide': ['89', '28', '46', '965'],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number.title()}")


# esercizio numero 6.11
        
cities = {
    'Milan':{
        'country': 'Italy',
        'population': '1.38 million people',
        'fact': 'second most populous italian city',
    },
    
    'Como':{
        'country': 'Italy',
        'population': '87 thousand people',
        'fact': ' located on the shores of the most beautiful lake in the world',
    },

    'Rome':{
        'country': 'iItaly',
        'population': '4.31 million people',
        'fact': 'Capital of Italy',
    },
}

for city, country_world in cities.items():
    print(f"\nCity: {city}")
    country = f"{country_world['country']}"
    population = f"{country_world['population']}"
    fact = country_world['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")


# Esercizio numero 6.12 
    
users = {
    'aeinstein': {
        'first': 'albert',
        'second': 'einstein',
        'location': 'princeton',
        'country of origin': 'germany',
        'death': '1955',
    },
    'mcurie': {
        'first': 'marie', 
        'second': 'curie',
        'location': 'paris',
        'country of origin': 'france',
        'death': '1934',
    },
    'Inewton': {
        'first': 'isaac',
        'second': 'newton',
        'location': 'london',
        'country of origin': 'england',
        'death': '1727',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    first_name = f"{user_info['first']}"
    second_name = f"{user_info['second']}"
    full_name = f"{user_info['first']} {user_info['second']}"
    location = f"{user_info['location']}"
    country_of_origin = user_info['country of origin']
    year_of_death = user_info['death']

    print(f"\tFirst name: {first_name.title()}")
    print(f"\tSecond name: {second_name.title()}")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tCountry of origin: {country_of_origin.title()}")
    print(f"\tYear of death: {year_of_death.title()}")