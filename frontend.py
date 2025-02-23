from FreeSimpleGUI import BLUES
import functions
import FreeSimpleGUI

from functions import write_todo

label = FreeSimpleGUI.Text("To-do")
input_box = FreeSimpleGUI.InputText(tooltip="To-Do", key="todo")
add_button = FreeSimpleGUI.Button("Add")
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
item_list = FreeSimpleGUI.Listbox(values=functions.get_todo(), key="todos",
                                  enable_events=True, size=(45,10))



window = FreeSimpleGUI.Window("My App",layout=[[input_box, add_button],
                                                   [item_list],
                                                   [complete_button,edit_button]],
                                                   font=("Sans Serif",20))

while True:
    button_event, input_value = window.read()
    todo_list = functions.get_todo()
    print(button_event)
    print(input_value)
    match button_event:
        case "Add":
            todo = input_value["todo"]
            todo_list.append(todo + "\n")
            write_todo(todo_list)
            window["todos"].update(values=todo_list)
        case "Edit":
            todo = input_value["todos"][0]
            new_todo = input_value["todo"] + "\n"

            get_index = todo_list.index(todo)
            todo_list[get_index] = new_todo
            functions.write_todo(todo_list)
            window["todos"].update(values=todo_list)
        case "todos":
            window["todo"].update(value=input_value["todos"][0])
        case "Complete":
            selected_todo = input_value["todos"][0]
            get_index = todo_list.index(selected_todo)
            todo_list.pop(get_index)
            functions.write_todo(todo_list)
            window["todos"].update(values=todo_list)
        case FreeSimpleGUI.WIN_CLOSED:
            break



window.close()