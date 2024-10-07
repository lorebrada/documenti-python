# esercizio numero 8.9 pagina 146

def show_messages(messages):
    """Print a simple message to each in the list"""
    for message in messages:
       print(message)
    
text_messages = [
    "Hello there!",
    "How are you today?",
    "Just checking in.",
    "Hope you're doing well!",
    "Let me know if you need anything."
]
show_messages(text_messages)

#esercizio numero 8.10 

# Define the function to show messages
def show_messages(messages):
    for message in messages:
        print(message)

# Define the function to send messages and move them to another list
def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
        sent_messages.append(message)

# List of text messages
text_messages = [
    "Hello there!",
    "How are you today?",
    "Just checking in.",
    "Hope you're doing well!",
    "Let me know if you need anything."
]

# Empty list to store sent messages
sent_messages = []

# Call the function to send and move messages
send_messages(text_messages, sent_messages)

# Print both lists to confirm the messages were moved correctly
print("Original messages:")
show_messages(text_messages)

print("\nSent messages:")
show_messages(sent_messages)


#esercizio numero 8.11

# Define the function to show messages
def show_messages(messages):
    for message in messages:
        print(message)

# Define the function to send messages and move them to another list
def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
        sent_messages.append(message)

# List of text messages
text_messages = [
    "Hello there!",
    "How are you today?",
    "Just checking in.",
    "Hope you're doing well!",
    "Let me know if you need anything."
]

# Empty list to store sent messages
sent_messages = []

# Call the function to send and move messages with a copy of the list
send_messages(text_messages[:], sent_messages)

# Print both lists to confirm the messages were moved correctly
print("Original messages:")
show_messages(text_messages)

print("\nSent messages:")
show_messages(sent_messages)