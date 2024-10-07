# esercizio numero 9.1 pagina 162

class Restaurant:
    """a simple model to attempt two restaurant attributes"""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize restaurant name and type attributes"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        """prints this two pieces of information"""
        print(f"the restaurant is called {self.restaurant_name}.")
        print(f"This is a {self.restaurant_type}-style restaurant.")
    
    def open_restaurant(self):
        """prints that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant('Bella Italia', 'mediterranean')
restaurant.describe_restaurant()
restaurant.open_restaurant()


#esercizio numero 9.2

class Restaurant:
    """a simple model to attempt two restaurant attributes"""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize restaurant name and type attributes"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        """prints this two pieces of information"""
        print(f"the restaurant is called {self.restaurant_name}.")
        print(f"This is a {self.restaurant_type}-style restaurant.")
    
    def open_restaurant(self):
        """prints that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant('Bella Italia', 'mediterranean')
new_restaurant = Restaurant('Il mannarino', 'apulian')
mountain_restaurant = Restaurant('il crotto valtellina', 'mountain')

restaurant.describe_restaurant()
new_restaurant.describe_restaurant()
mountain_restaurant.describe_restaurant()


#esercizio numero 9.3

class User:
    
    def __init__(self, first_name, last_name, email_address, phone_number, ID_card_number):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.ID_card_number = ID_card_number
    
    def describe_user(self):
        print(f"your first name is {self.first_name}.")
        print(f"your last name is {self.last_name}.")
        print(f"your email address is {self.email_address}.")
        print(f"your phone number is {self.phone_number}.")
        print(f"your ID card number is {self.ID_card_number}.")

    def greet_user(self):
        print(f"Thank you for your time, {self.first_name}!")

user0 = User('lorenzo', 'Bradanini', 'lorenzobrada@gmail.com', '3348987454', 'CA431B0')
user1 = User('Samuele', 'Bradanini', 'samubrada@gmail.com', '3367856491', 'CH674G6')
user2 = User('Andrea', 'Celentano', 'andrecele@gmail.com', '3328976490', 'FA569D0')

user0.describe_user()
user0.greet_user()

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()