import streamlit as st
import functions 

# Get the list of todos from the functions module
todos = functions.get_todos()

# Function to add a new todo item
def add_todo():
    # Get the new todo item from the session state
    todo = st.session_state['new_todo'] + "\n"
    # Append the new todo to the list
    todos.append(todo)
    # Write the updated list of todos back to storage
    functions.write_todos(todos)

# Set the title and subtitle of the Streamlit app
st.title("ToDoApp")
st.subheader("My Todo App using Streamlit")
st.write("This app is to improve productivity")

# Iterate over the list of todos and create a checkbox for each
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # If the checkbox is checked, remove the todo from the list
    if checkbox:
        todos.pop(index)
        # Write the updated list of todos back to storage
        functions.write_todos(todos)
        # Remove the corresponding session state entry
        del st.session_state[todo]
        # Rerun the script to update the UI
        st.experimental_rerun()

# Create a text input for adding a new todo item
# The `on_change` parameter should be the function name, not a string
st.text_input(label=" ", placeholder="New Todo", on_change=add_todo, key="new_todo")
