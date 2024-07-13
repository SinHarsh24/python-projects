# Initialize an empty list to store to-do items
todos = []

# Start an infinite loop to continuously prompt the user for actions
while True:
    # Prompt the user for an action and strip any leading/trailing whitespace
    user_action = input("Type add, show, or exit: ").strip()

    # Use match-case statement to handle different user actions
    match user_action:
        case 'add':
            # If the user action is 'add', prompt for a to-do item and add it to the list
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            # If the user action is 'show', print all to-do items in the list capitalized
            for todo in todos:
                print(todo.capitalize())
        case 'exit':
            # If the user action is 'exit', break out of the loop
            break

# Print a completion message after exiting the loop
print("Done")
