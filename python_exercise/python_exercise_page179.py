# esercizio numero 9.10 pagina 179
from python_exercise_page175 import Restaurant

restaurant = Restaurant('Bella Italia', 'mediterranean')
new_restaurant = Restaurant('Il mannarino', 'apulian')
mountain_restaurant = Restaurant('il crotto valtellina', 'mountain')

restaurant.describe_restaurant()
new_restaurant.describe_restaurant()
mountain_restaurant.describe_restaurant()


#esercizio numero 9.11 

from python_exercise_page176 import User, Privileges, Admin

my_admin = Admin('Lorenzo', 'Bradanini', ['can remove people', 'can promote posts', 'can limitate user access'])

# display the descriptive name and available privileges
print(my_admin.get_descriptive_name()) 
my_admin.show_privileges()


#esercizio numero 9.12

# admin_instance.py

from my_admin_privileges_page179 import Admin

# Create an Admin instance
my_admin = Admin('John', 'Doe', ['can delete users', 'can ban users', 'can edit posts'])

# Display the descriptive name and available privileges
print(my_admin.get_descriptive_name()) 
my_admin.show_privileges()

