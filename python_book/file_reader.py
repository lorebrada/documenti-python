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

lines = contents.splitlines()
for line in lines:
    print(line)
