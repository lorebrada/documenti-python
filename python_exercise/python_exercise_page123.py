# esercizio numero 7.4 pagina 123

prompt = "\nPlease Tell me which type of toppings you want:"
prompt += "\nEnter quit to end the program."

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping.title()} to your pizza!")
 
    
# esercizio numero 7.5 
    
prompt = "\nPlease tell me your age:"
prompt += "\nEnter 'quit' to end the program."

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
    
    if age <= 3:
        print("\nYour ticket is free!")
    elif 3 < age <= 12:
        print("\nYour ticket costs $10!")
    else:
        print("\nThe ticket costs $15!")


# esercizio numero 7.6 (es. 1 con punti 1 e 2.)
        
prompt = "\nPlease Tell me which type of toppings you want:"
prompt += "\nEnter quit to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# esercizio numero 7.6 (es.1 con punto numero 3.)
        
prompt = "\nPlease Tell me which type of toppings you want:"
prompt += "\nEnter quit to end the program."

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(topping)
    
