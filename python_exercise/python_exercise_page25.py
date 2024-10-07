# esercizio numero 2.3 pagina 25

name = "lorenzo"
msg = f"Hello {name.title()}, would you like to learn some Python today?"

print(msg)


# esercizio numero 2.4 

name = "lorenzo"

print(name.lower())
print(name.upper())
print(name.title())


# esercizio numero 2.5

print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')


# esercizio numero 2.6

famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

print(message)


# esercizio numero 2.7

name = "\tLorenzo Bradanini\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())


# esercizio numero 2.8

filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')

print(simple_filename)