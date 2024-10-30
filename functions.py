FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    """the code below read a 'to do list and return the value' """
    with open(filepath, "r") as file_local:
        """ the code below write to do item in a text file"""
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
