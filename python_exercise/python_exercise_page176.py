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