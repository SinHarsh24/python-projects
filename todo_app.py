# Prompt message to be displayed when asking for user input
user_prompt = "Enter a todo :"

# Taking input from the user for three to-do items
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

# Creating a list of to-do items along with a predefined string "Hello"
todos = [todo1, todo2, todo3, "Hello"]

# Printing the list of to-do items
print(todos)

# Printing the type of the first to-do item (which will be a string)
print(type(todo1))
