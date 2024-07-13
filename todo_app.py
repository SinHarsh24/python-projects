# Initialize an empty list to store to-do items
todos = []

# Start an infinite loop to continuously prompt the user for actions
while True:
    # Prompt the user for an action and strip any leading/trailing whitespace
    user_action = input("Type add, show, edit or exit: ").strip()

    # Use match-case statement to handle different user actions
    match user_action:
        case 'add':
            # If the user action is 'add', prompt for a to-do item and add it to the list
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            # If the user action is 'show', print all to-do items in the list capitalized
            # Iterate through the list of to-do items with their indices
            for index, items in enumerate(todos):
                # Print the index and the capitalized to-do item
                print(index, '-', items.capitalize())
        case 'edit':
            # If the user action is 'edit', prompt for the number of the to-do item to edit
            number = int(input("Number of todo to edit: "))
            number = number - 1  # Adjust for zero-based index
            # Prompt for the new to-do item and replace the old item at the specified index
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'exit':
            # If the user action is 'exit', break out of the loop
            break

# Print a completion message after exiting the loop
print("Done")
