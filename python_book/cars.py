cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


car = 'bmw'
print(car == 'bmw')


car = 'audi'
print(car == 'bmw')

#in questo caso audi è scritto sia in minuscolo che in maiuscolo. sono due valori differenti, perciò l' uguaglianza è falsa.
car = 'Audi'
print(car == 'audi')


car = 'Audi'
print(car.lower() == 'audi')


car = 'Audi'
print(car.lower() == 'audi')
print(car)