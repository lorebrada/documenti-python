#esercizio numero 6.4 pagina 104

glossary = {
    'Python': 'language', 
    'Dictionary': 'collection of key-value pairs',
    'Variables': 'value that can change',
    'List': 'sequence of variables',
    'Sorting': 'displacing a list in a particular order',
    'code': 'piece of software',
    'looping': 'repeating something once a condition is met',
    'software': 'piece of code that creates programs',
    'set': 'unordered, unchangeable collection',
    'tuple': 'type of data structure similar to lists'
    }

for key, value in glossary.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


#esercizio numero 6.5

rivers = {
   'Nile': 'Egypt',
   'Amazon': 'Brazil',
   'Mississippi': 'United States'
}

for name, river in rivers.items():
    print(f"The {name.title()} runs through {river.title()}.")

for name in rivers.keys():
    print(name.title())

for name, river in rivers.items():
    print(f"{river.title()}")


#esercizio numero 6.6
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'david': 'julia',
    'andrew': 'java',
    'lawrence': 'javascript',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
if 'jacob' not in favorite_languages.keys():
    print(" jacob, please take the poll!")



