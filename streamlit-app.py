import streamlit as st
import functions 
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("ToDoApp")
st.subheader("My Todo App using Streamlit")
st.write("This app is to improve productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo ,key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ",placeholder="New Todo",on_change="Add Todo",key= "new_todo" ) 