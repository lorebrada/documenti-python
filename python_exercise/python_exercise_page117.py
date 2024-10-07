# esercizio numero 7.1 pagina 117

rent = input("Hello, which kind of rental car do you like?: ")
print(rent)
print(f"\nLet me see if I can find you a {rent}")

# esercizio numero 7.2

restaurant = input("How many people are in the dinner group?: ")
restaurant = int(restaurant)

if restaurant >= 8:
    print("\nYou'll have to wait a few minutes for the table.")
else:
    print("\nYour table is ready!")

 # esercizio numero 7.3
    
number = input("Enter a number, and I'll find if it is a multiple of 10 or not:")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number you chose {number} is a multiple of 10!")
else:
    print(f"\nThe number you chose {number} is not a multiple of 10.")
