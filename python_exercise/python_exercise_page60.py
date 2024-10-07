#esercizio numero 4.3 pagina 60

for value in range(1, 21):
    print(value)

#esercizio numero 4.4
    
for value in range(1, 101):
    print(value)

#esercizio numero 4.5

numbers = list(range(1, 101, 1))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#esercizio numero 4.6

numbers = []
for value in range(1,21):
    number = value * 1
    numbers.append(number)

print(numbers)

#esercizio numero 4.7

multiple_of_3 = list(range(3,31,3))
print(multiple_of_3)

multitples_of_three = []
for value in range(3, 31, 3):
    multiple_of_3 = value 
    multitples_of_three.append(value)

print(multitples_of_three)

#esercizio numero 4.8 

cubes = []
for value in range (1, 11):
    cubes.append(value ** 3)

print(cubes)

#esercizio numero 4.9 

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
