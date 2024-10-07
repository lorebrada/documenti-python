# esercizio numero 7.8 pagina 127

sandwitch_orders = ['chicken sandwitch', 'egg sandwitch', 'seafood sandwitch', 'roast beef sandwitch', 'grilled beef sandwitch']
finished_sandwitches = []

while sandwitch_orders:
    ended_sandwitches = sandwitch_orders.pop()

    print(f"I made your {ended_sandwitches.title()}")
    finished_sandwitches.append(ended_sandwitches)

print("\nThe following sandwitches have been made:")

for finished_sandwitch in finished_sandwitches:
    print(finished_sandwitch.title())

print("\n")
# esercizio numero 7.9

sandwitch_orders = ['chicken sandwitch', 'pastrami', 'egg sandwitch', 'pastrami', 'seafood sandwitch', 'pastrami', 'roast beef sandwitch', 'grilled beef sandwitch']
finished_sandwitches = []

print(sandwitch_orders)

print("\n")

print("Sorry, but we ran out of pastrami!")

print("\n")

while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')

print(sandwitch_orders)

while sandwitch_orders:
    ended_sandwitches = sandwitch_orders.pop()

    print(f"I made your {ended_sandwitches.title()}")
    finished_sandwitches.append(ended_sandwitches)

print("\nThe following sandwitches have been made:")

for finished_sandwitch in finished_sandwitches:
    print(finished_sandwitch.title())

# esercizio numero 7.10 
    
responses ={}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, what would it be? ")

    responses[name] = response

    repeat = input("would you like to let another person to respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results---")
for name, response in responses.items():
    print(f"{name} would really like to go to {response}.")
    