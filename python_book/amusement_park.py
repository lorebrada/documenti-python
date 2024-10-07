age = 3
if age < 4:
    print("Your admission cost is 0$.")
elif age < 18:
    print("You admission cost is 25$.")
else:
    print("Your admission cost is 40$.")


age = 12
if age <= 16:
    print("You are not allowed to drink alcohol.")
elif age >= 16 and age < 18:
    print("You are allowed to drink alcohol, but not to buy it.")
else:
    print("You can drink and buy alcohol.")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")


age = 66
if age < 4:
    price = 0

elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")