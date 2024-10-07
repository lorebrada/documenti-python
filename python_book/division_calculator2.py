print("Give me two numbers, and I'll divide them.")
print("enter 'q' to quit.")

while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
