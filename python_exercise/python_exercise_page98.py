#esercizio numero 6.1 pagina 98 

person_0 = {'first_name':  'Samuele', 'last_name': 'Bradanini', 'age': '19 years old', 'city': 'Villa Guardia'}
print(person_0)

#esercizio numero 6.2

favorite_numbers = {
    'lorenzo': '1',
    'Sara': '24',
    'Andrea': '36',
    'Giovanni': '4',
    'Davide': '89',
}

number = favorite_numbers['lorenzo'].title()
print(f"Lorenzo's favorite number is {number}.")

number = favorite_numbers['Sara'].title()
print(f" Sara's favorite number is {number}.")

number = favorite_numbers['Andrea'].title()
print(f"Andrea's favorite number is {number}.")

number = favorite_numbers['Giovanni'].title()
print(f"Giovanni's favorite number is {number}.")

number = favorite_numbers['Davide'].title()
print(f"Davide's favorite number is {number}.")



#esercizio numero 6.3

glossary = {
    'Python': 'language', 
    'Dictionary': 'collection of key-value pairs',
    'Variables': 'value that can change',
    'List': 'sequence of variables',
    'Sorting': 'displacing a list in a particular order',
    }

gloss = glossary['Python'].title()
print(f"Python is a {gloss.lower()}.")

print("\n")

gloss = glossary['Dictionary'].title()
print(f"A Dictionary is a {gloss.lower()}.")

print("\n")

gloss = glossary['Variables'].title()
print(f"Variables are {gloss.lower()}.")

print("\n")

gloss = glossary['List'].title()
print(f"A List is a {gloss.lower()}.")

print("\n")

gloss = glossary['Sorting'].title()
print(f"Sorting is basically {gloss.lower()}.") 