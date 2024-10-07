# esercizio numero 10.11 pagina 206 (parte 1)

from pathlib import Path
import json

numbers = [0, 1, 2, 3, 4, 5, 6]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

print(numbers)

# esercizio numero 10.11 (parte 2)

from pathlib import Path
import json

number = input("What is your favourite number?")

path = Path('number.json')
contents = json.dumps(number)
path.write_text(contents)

print(f"I know your favourite number! It's {number}!")


# esercizio numero 10.12 

from pathlib import Path
import json

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")


# esercizio numero 10.13 

from pathlib import Path
import json

def get_stored_user_info(path):
    """store the user informations"""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    game = input("What's your favorite game? ")
    animal = input("What's your favorite animal? ")

    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

greet_user()


# esercizio numero 10.14 

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")    
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()