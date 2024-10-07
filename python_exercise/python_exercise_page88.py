#esercizio numero 5.8 pagina 88

usernames_list = ['admin', 'mr beast', 'cicciogamer89', 'jordan', 'dario']

for username_list in usernames_list:
    if username_list  == 'admin':
        print("Hello admin, would you like to see a status report?.")
    else:
        print(f" Hello {username_list}, thank you for logging in again!.")


#esercizio numero 5.9

usernames_list = []

if usernames_list:
    for username_list in usernames_list:
        print(f"Hello {username_list},thank you for logging in again!.")
    print("\nFiished list")
else:
    print("we need to find some users!")


#esercizio numero 5.10

current_users = ['anna.com', 'alice.net', 'italia.gov', 'lorenzo.it', 'FHE.py']

new_users = ['anna.com', 'italia.gov', 'andrea.net', 'lucia.it', 'casa.it']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}, enter new username.")
    else:
        print(f"username {new_user} is available to use.")


lowercase_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"{new_user}, enter new username.")
    else:
        print(f"Username '{new_user}' is available to use.")


#esercizio numero 5.11

ordinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in ordinal_numbers:
    if number == '1':
        print('1st')
    elif number == '2':
        print('2nd')
    elif number == '3':
        print('3rd')
    else:
        print(f"{number}th")

print("\nThese are the first 9 ordinal numbers.")
    