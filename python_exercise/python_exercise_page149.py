# esercizio numero 8.12 pagina 149

def make_sandwitch(*items):
    """print the list of items a person want on a sandwitch"""
    print(items)

make_sandwitch('pepperoni')
make_sandwitch('mushrooms', 'pepperoni', 'extra salad')

#variazione esercizio numero 8.12 

def make_sandwitch(*items):
    """summarize the sandwitch we are about to make"""
    print("\nMaking a sandwitch with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwitch('pepperoni')
make_sandwitch('mushrooms', 'pepperoni', 'extra salad')


# esercizio numero 8.13

def build_profile(first, last, height, weight, favourite_sport, **user_info):
    """Build a dictionary containing 5 fariables that describe myself"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['current_height'] = height
    user_info['current_weight'] = weight
    user_info['actual_favourite_sport'] = favourite_sport
    return user_info

user_profile = build_profile('lorenzo', 'bradanini',
                             height='189',
                             weight='64kg',
                             favourite_sport='mountain biking')
print(user_profile)


# esercizio numero 8.14 

def make_car(brand, model, color, tow_package, **car_info):
    """Build a function containing informations about a car"""
    car_info['brand_name'] = brand
    car_info['car_model'] = model
    car_info['car_color'] = color
    car_info['tow_packages'] = tow_package
    return car_info

car_profile = make_car('subaru', 'outback', 
                       color='blue',
                       tow_package=True)
print(car_profile)
