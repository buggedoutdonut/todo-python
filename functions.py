def get_todo():
    """Reads the To-Do List from the txt file
     then returns the list."""
    with open("todo.txt","r") as readFile:
        todo_list = readFile.readlines()
    return todo_list

def write_todo(filepath,todos):
    """Writes the current To-Do List into the txt file."""
    with open(filepath, "w") as writeFile:
        writeFile.writelines(todos)