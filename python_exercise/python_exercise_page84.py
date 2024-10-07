#esercizio numero 5.3 pagina 84

alien_color = 'green', 'yellow', 'red'

alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points!")

alien_color = 'yellow'
if alien_color == 'yellow':
    print("You earned 5 points!")


alien_color = 'red'
if alien_color == 'blue':
    print("You earned 5 points!")


#esercizio numero 5.4
    
alien_color = 'green', 'yellow', 'red'

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
if alien_color != 'green':
    print("You just earned 10 points")


alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You earned 10 points!")

#esercizio numero 5.5

alien_color = 'green', 'yellow', 'red'

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("you just earned 15 points!")


alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("you just earned 15 points!")


alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("you just earned 15 points!")


#esercizio numero 5.5
    
age = 23

if age < 2:
    print("This person is still a baby")
elif age >= 2 and age < 4:
    print("This person is a toddler")
elif age >= 4 and age < 13:
    print("This person is a kid")
elif age >= 13 and age < 20:
    print("This person is a teenager")
elif age >= 20 and age < 65:
    print("This person is an adult")
else: 
    print("This person is an elder")
