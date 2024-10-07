# esercizio numero 9.13 pagina 180

from random import randint
randint(1,6)

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

# Create an instance of the Die class
die = Die()

# Roll the die
roll_die = die.roll()
print(roll_die)

#esercizio numero 9.13 parte 2 (10-sided die)

from random import randint
randint(1,10)

class Die:
    def __init__(self, sides=10):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

# Create an instance of the Die class
die = Die()

# Roll the die
roll_die = die.roll()
print(roll_die)

#esercizio numero 9.14 parte 3 (20-sided die)

from random import randint
randint(1,20)

class Die:
    def __init__(self, sides=20):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

# Create an instance of the Die class
die = Die()

# Roll the die
roll_die = die.roll()
print(roll_die)


# esercizio numero 9.14

from random import randint, choice

random_number = randint(1, 10)

selected_letters = ['g', 'h', 'z', 'f', 'a']
random_letters = choice(selected_letters)

selected_elements = [random_letters, random_number]

# Print the selected elements
print("The winning ticket contains the following numbers or letters:")
print(selected_elements)

# Print the message about winning a prize
print("Any ticket matching these 2 numbers or letters wins a prize!")



# seconda versione corretta.

from random import randint, choice

# Define the list containing numbers and letters
ticket_list = list(range(1, 11)) + ['g', 'h', 'z', 'f', 'a']

# Ensure at least 4 elements are selected
selected_elements = [choice(ticket_list) for _ in range(4)]

# Print the selected elements
print("The winning ticket contains the following numbers or letters:")
print(selected_elements)

# Print the message about winning a prize
print("Any ticket matching these 4 numbers or letters wins a prize!")


# esercizio numero 9.15 

from random import randint, choice

# Define the list containing numbers and letters
ticket_list = list(range(1, 11)) + ['g', 'h', 'z', 'f', 'a']

# Initialize variables
attempts = 0
winning_ticket = ['g', 'h', 'z', 'f', 'a']
ticket = []

# Keep pulling numbers until you win
while ticket != winning_ticket:
    ticket = [choice(ticket_list) for _ in range(5)]
    attempts += 1

# Print the number of attempts
print(f"It took {attempts} attempts to get a winning ticket.")


# esercizio numero 9.16 

#python module of the week read. I will start reading and devouring every python resource that I will find
