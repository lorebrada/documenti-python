#esercizio numero 3.4 pagina 41

dinner = ['Ilaria', 'Lorenzo', 'Davide']
print(dinner)
dinner_invite = dinner.pop(0)
print(f"I would like to invite {dinner_invite.title()} to dinner.")

dinner_invite = dinner.pop(1)
print(f"I would like to invite {dinner_invite.title()} to dinner.")

dinner_invite = dinner.pop(-1)
print(f"I would like to invite {dinner_invite.title()} to dinner.")


#Metodo numero 2

dinner = ['Ilaria', 'Lorenzo','Davide']
message = dinner.pop(0)
print(f"I would like to invite {message.title()} to dinner with me.")
message = dinner.pop(1)
print(f"I would like to invite {message.title()} to dinner with me.")
message = dinner.pop(-1)
print(f"I would like to invite {message.title()} to dinner with me.")


#metodo numero 3 (probabilmente l'unico sensato)

dinner = ['Ilaria', 'Lorenzo','Davide']
message = f"I would like to invite you to dinner, {dinner[0].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[1].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[2].title()}."
print(message)


#esercizio numero 3.5 pagina 42 

dinner = ['Ilaria', 'Lorenzo','Davide']
message = f"I would like to invite you to dinner, {dinner[0].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[1].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[2].title()}."
print(message)

del dinner[1]
print(dinner)

dinner.append('Luca')
print(dinner)

dinner = ['Ilaria', 'Lorenzo','Luca']
message = f"I would like to invite you to dinner, {dinner[0].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[1].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[2].title()}."
print(message)



#esercizio numero 3.6 pagina 42
dinner = ['Ilaria', 'Lorenzo','Luca']
message = f"I would like to invite you to dinner, {dinner[0].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[1].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[2].title()}."
print(message)
message = "I'm glad to announce that i've found a bigger table!!"
print(message)


dinner.insert(0, 'Anna')
print(dinner)


dinner.insert(2, 'Samuele')
print(dinner)

dinner.append('Andrea')
print(dinner)

dinner = ['Anna', 'Ilaria', 'Samuele', 'Lorenzo','Luca', 'Andrea']
message = f"I would like to invite you to dinner, {dinner[0].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[1].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[2].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[3].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[4].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[5].title()}."
print(message)


#Esercizio numero 3.7 pagina 42

dinner = ['Anna', 'Ilaria', 'Samuele', 'Lorenzo','Luca', 'Andrea']
message = f"I would like to invite you to dinner, {dinner[0].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[1].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[2].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[3].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[4].title()}."
print(message)
message = f"I would like to invite you to dinner, {dinner[5].title()}."
print(message)

message = f"I unfortunately just discovered that there are only two places left at the restaurant, so i have space for only two of you, sorry!"
print(message)


dinner = ['Anna', 'Ilaria', 'Samuele', 'Lorenzo','Luca', 'Andrea']
popped_dinner = dinner.pop(0)
print(popped_dinner)
popped_dinner = dinner.pop(3)
print(popped_dinner)
popped_dinner = dinner.pop(1)
print(popped_dinner)
popped_dinner = dinner.pop(2)
print(popped_dinner)

print(dinner)


dinner = ['Ilaria', 'Lorenzo']
invite = dinner.pop(0)
print(f"You are still invited to dinner, {invite.title()}.")
invite = dinner.pop(-1)
print(f"You are still invited to dinner, {invite.title()}.")

dinner = ['Ilaria', 'Lorenzo']

dinner.remove('Lorenzo')
print(dinner)
dinner.remove('Ilaria')
print(dinner)