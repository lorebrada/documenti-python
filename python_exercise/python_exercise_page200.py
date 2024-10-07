# esercizio numero 10.6 pagina 200 (prima parte)

print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    answer = int(first_number) + int(second_number)
    print(answer)



# esercizio numero 10.6 seconda parte 

print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(f"The answer is {answer}")


# esercizio numero 10.7 

print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    answer = int(first_number) + int(second_number)
    print(answer)



# esercizio numero 10.6 seconda parte 

print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(f"The answer is {answer}")


# esercizio numero 10.8 

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")


# esercizio numero 10.9 

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print(f"\nReading file: {filename}")
        print(contents)


# esercizio numero 10.10

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')

