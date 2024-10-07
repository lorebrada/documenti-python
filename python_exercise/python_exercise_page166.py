# esercizio numero 9.4 pagina 166

class User:
    
    def __init__(self, first_name, last_name, email_address, phone_number, ID_card_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.ID_card_number = ID_card_number
        self.user_attempts = 0  # Initialize login_attempts to 0
    
    def describe_user(self):
        print(f"Your first name is {self.first_name}.")
        print(f"Your last name is {self.last_name}.")
        print(f"Your email address is {self.email_address}.")
        print(f"Your phone number is {self.phone_number}.")
        print(f"Your ID card number is {self.ID_card_number}.")
    
    def greet_user(self):
        print(f"Thank you for your time, {self.first_name}!")
    
    def increment_login_attempts(self):
        self.user_attempts += 1
    
    def reset_login_attempts(self):
        self.user_attempts = 0

# Creating an instance of the User class
user = User('John', 'Doe', 'john.doe@example.com', '1234567890', 'AB123456')

# Incrementing login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Printing the value of login_attempts
print("Login attempts:", user.user_attempts)

# Resetting login attempts
user.reset_login_attempts()

# Printing the value of login_attempts after reset
print("Login attempts after reset:", user.user_attempts)






