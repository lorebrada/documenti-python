# esercizio numero 9.6 pagina 173

class Restaurant:
    """A simple model to represent restaurant attributes."""

    def __init__(self, restaurant_name):
        """Initialize restaurant name and type attributes."""
        self.restaurant_name = restaurant_name

    def describe_restaurant(self):
        """Prints the restaurant name and type."""
        print(f"The restaurant is called {self.restaurant_name}.")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.restaurant_name}"
        return long_name.title()

    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to ice cream."""

    def __init__(self, restaurant_name):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to the ice cream stand."""
        super().__init__(restaurant_name)
        self.flavors_list = ['chocolate', 'vanilla', 'nutella', 'almond', 'strawberry']

    def display_flavors(self):
        """Print a statement describing ice cream flavors."""
        print(f"{self.restaurant_name} offers the following ice cream flavors:")
        for flavor in self.flavors_list:
            print(f"- {flavor.title()}")

# Create an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand('sweet scoops')

# Display the descriptive name and available flavors
print(my_ice_cream_stand.get_descriptive_name())
my_ice_cream_stand.display_flavors()


# esercizio numero 9.7 pagina 173

class User:
    
    def __init__(self, first_name, last_name):
        
        self.first_name = first_name
        self.last_name = last_name
    
    def get_descriptive_name(self):
        long_name = f"{self.first_name} {self.last_name}"
    
    def describe_user(self):
        print(f"your first name is {self.first_name}.")
        print(f"your last name is {self.last_name}.")

    def greet_user(self):
        print(f"Thank you for your time, {self.first_name}!")

class Admin(User):
    """Represent a special kind of user"""

    def __init__(self, first_name, last_name):
        """Initialize attribiutes of the parent class.
        Then initialize attributes specific to the Admin class"""
        super().__init__(first_name, last_name)
       
        self.privileges_list = ['Can add posts', 'can remove user', 'can delete posts', 'can close chat']

    def show_privileges(self):
        """Print a statement defining all Admin privileges"""
        print(f"{self.first_name} {self.last_name} has the following privileges: ")
        for privilege in self.privileges_list:
            print(f"- {privilege.title()}")

# create an instance for Admin 
My_great_user = Admin('Lorenzo', 'bradanini')

# display the descriptive name and available privileges
print(My_great_user.get_descriptive_name()) 
My_great_user.show_privileges()


#esercizio numero 9.8

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_descriptive_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def describe_user(self):
        print(f"Your first name is {self.first_name}.")
        print(f"Your last name is {self.last_name}.")

    def greet_user(self):
        print(f"Thank you for your time, {self.first_name}!")

class Privileges:
    def __init__(self, privileges):
        self.privileges_list = privileges
    
    def show_privileges(self):
        print("User has the following privileges:")
        for privilege in self.privileges_list:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        print(f"{self.get_descriptive_name()} has the following privileges:")
        self.privileges.show_privileges()

# create an instance for Admin 
my_great_user = Admin('Lorenzo', 'Bradanini', ['can remove people', 'can promote posts', 'can limitate user access'])

# display the descriptive name and available privileges
print(my_great_user.get_descriptive_name()) 
my_great_user.show_privileges()




# esercizio numero 9.9 

class Car: 
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
    

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

            print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery capacity to 65 KWh if it's not already."""
        
        if self.battery_size <= 65:
            print("Upgrading the battery capacity to 65 KWh.")
            self.battery_size == 65
            self.get_range()  
        else:
            print("The battery capacity is already 65 KWh.")



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

# Create an instance of ElectricCar
my_leaf = ElectricCar('Nissan', 'Leaf', 2024)

# Display the descriptive name of the electric car
print(my_leaf.get_descriptive_name())

# Describe the battery of the electric car
my_leaf.battery.describe_battery()

# Display the range of the electric car
my_battery = Battery(65)
my_battery.describe_battery()  
my_battery.upgrade_battery()

