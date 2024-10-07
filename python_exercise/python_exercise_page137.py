# esercizio numero 8.4 pagina 137

def make_shirts(shirt_size='large', shirt_message='I love python'):
    """Display information about size and text of a shirt"""
    print(f"\nMy shirt's size is {shirt_size}, and the text written on it says: {shirt_message.title()}")

make_shirts(shirt_size='Large', shirt_message='I love python')

def make_shirts(shirt_size, shirt_message='I love python'):
    print(f"\nMy shirt's size is {shirt_size}, and the text written on it says: {shirt_message.title()}")

make_shirts(shirt_size='medium')

def make_shirts(shirt_size='small', shirt_message= 'I love Rust'):
    print(f"\nMy shirt's size is {shirt_size}, and the text written on it says: {shirt_message.title()}")

make_shirts(shirt_size='small', shirt_message='I love Rust')

# esercizio numero 8.5 

def describe_city(city_name, city_country='Italy'):
    """Display information about the city name and country"""
    print(f"\n{city_name} is in {city_country.title()}.")

describe_city(city_name='Perugia')
describe_city(city_name='Como')

def describe_city(city_name, city_country='Italy'):
    """Display information about the city name and country"""
    print(f"\n{city_name} is in {city_country.title()}.")

describe_city(city_name='Como')

def describe_city(city_name= 'New York', city_country= 'United States'):
    """Display information about the city name and country"""
    print(f"\n{city_name} is in the {city_country.title()}.")

describe_city(city_name='New York', city_country='United States')