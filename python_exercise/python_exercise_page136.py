# esercizio numero 8.3 pagina 136 (positional arguments)

def make_shirt(shirt_size, shirt_message):
    """Display information about size and text of a shirt."""
    print(f"\nMy T-shirt is {shirt_size} in size and on it you can read the words: {shirt_message.title()}.")

make_shirt('XL', 'Live a life, you will remember')

#  esercizio numero 8.3 (Keyword arguments)

def make_shirt(shirt_size, shirt_message):
    """Display information about size and text of a shirt."""
    print(f"\nMy T-shirt is {shirt_size} in size and on it you can read the words: {shirt_message.title()}.")

make_shirt(shirt_size='XL', shirt_message='Live a life, you will remember')

