# admin_privileges.py

from user_page179 import User

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("Available privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This user has no privileges.")

class Admin(User):
    def __init__(self, first_name, last_name, privileges=[]):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()
