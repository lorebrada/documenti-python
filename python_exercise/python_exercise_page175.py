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