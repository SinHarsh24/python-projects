# Initialize an empty list to store to-do items
todos = []

def add_todo():
    """Prompt the user to add a new to-do item."""
    todo = input('Enter a todo: ').strip()  # Get user input for the new to-do item
    if todo:  # Check if the input is not empty
        todos.append(todo)  # Add the new to-do item to the list
        print(f"Added: {todo}")  # Inform the user that the item was added
    else:
        print("Todo item cannot be empty.")  # Inform the user that the input was empty

def show_todos():
    """Display all to-do items."""
    if todos:  # Check if there are any to-do items in the list
        for index, item in enumerate(todos, start=1):  # Iterate over the list with indices starting from 1
            print(f"{index} - {item.capitalize()}")  # Print the index and the to-do item, capitalizing the first letter
    else:
        print("No to-do items to show.")  # Inform the user that there are no to-do items

def edit_todo():
    """Edit an existing to-do item."""
    try:
        number = int(input("Number of todo to edit: "))  # Get user input for the item number to edit
        if 1 <= number <= len(todos):  # Check if the input number is within the valid range
            new_todo = input('Enter new todo: ').strip()  # Get user input for the new to-do item
            if new_todo:  # Check if the new input is not empty
                todos[number - 1] = new_todo  # Update the specified to-do item
                print(f"Todo #{number} updated to: {new_todo}")  # Inform the user that the item was updated
            else:
                print("New todo item cannot be empty.")  # Inform the user that the new input was empty
        else:
            print("Invalid todo number.")  # Inform the user that the input number was out of range
    except ValueError:
        print("Please enter a valid number.")  # Inform the user that the input was not a valid number

def main():
    """Main loop to prompt the user for actions."""
    while True:  # Start an infinite loop to continuously prompt the user for actions
        user_action = input("Type add, show, edit, or exit: ").strip().lower()  # Get user input for the action

        if user_action == 'add':  # If the user action is 'add'
            add_todo()  # Call the add_todo function
        elif user_action == 'show':  # If the user action is 'show'
            show_todos()  # Call the show_todos function
        elif user_action == 'edit':  # If the user action is 'edit'
            edit_todo()  # Call the edit_todo function
        elif user_action == 'exit':  # If the user action is 'exit'
            print("Done")  # Print a completion message
            break  # Break out of the loop to exit the program
        else:
            print("Invalid action. Please type add, show, edit, or exit.")  # Inform the user of an invalid action

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the program
