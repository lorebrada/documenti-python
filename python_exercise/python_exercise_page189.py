# esercizio numero 10.1 pagina 189
from pathlib import Path

path = Path('python_txt/learning_python.txt')
contents = path.read_text()

print(contents)

#second part of the exercise 

from pathlib import Path

path = Path('python_txt/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)


# esercizio numero 10.2 

message = "In Python you can pass an arbitrary number of arguments"
print(message.replace('Python', 'c'))

message = "In Python you can use boolean algebra "
print(message.replace('Python', 'c'))

message = "In Python you can store keys in a dictionary "
print(message.replace('Python', 'c'))

message = "In Python you can access elements into a list "
print(message.replace('Python', 'c'))


#esercizio numero 10.3

from pathlib import Path

path = Path('python_txt/pi_digits.txt')
contents = path.read_text()

print(contents)


# second part of this exercise 

from pathlib import Path

path = Path('python_txt/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

# third part of this exercise

from pathlib import Path

path = Path('python_txt/pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
