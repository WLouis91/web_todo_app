import streamlit as st
import  functions

#This is web.py application it runs on the browser to run that code you need to go on the terminal an write "streamlit run web.py"
#and press Enter the broswer will open automatically to see the application.

todos= functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

    print(todo)


st.title("My To App")
st.subheader("This is an App")
st.write("this app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo", on_change=add_todo,key="new_todo")


# print("Helo")

# st.session_state # this allows you to see what you enter the entry box it shows as a dictionary but it's not a dictionary
