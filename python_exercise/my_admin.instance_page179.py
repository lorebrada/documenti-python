from python_exercise_page173 import Admin

my_admin = Admin('Lorenzo', 'Bradanini', ['can remove people', 'can promote posts', 'can limitate user access'])

# display the descriptive name and available privileges
print(my_admin.get_descriptive_name()) 
my_admin.show_privileges()