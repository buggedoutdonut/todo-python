import datetime
import time
import functions
import FreeSimpleGUI
from functions import write_todo

FreeSimpleGUI.theme("Navy Blue")
label = FreeSimpleGUI.Text("To-do")
input_box = FreeSimpleGUI.InputText(tooltip="To-Do", key="todo")
add_button = FreeSimpleGUI.Button("Add")
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
item_list = FreeSimpleGUI.Listbox(values=functions.get_todo(), key="todos",
                                  enable_events=True, size=(45,10))
exit_button = FreeSimpleGUI.Button("Exit")
error_label = FreeSimpleGUI.Text("", key="error")
date_time = FreeSimpleGUI.Text("", key="datetime")

window = FreeSimpleGUI.Window("My App",layout=[[date_time],
                                                   [input_box, add_button],
                                                   [item_list],
                                                   [complete_button,edit_button, exit_button, error_label]],
                                                   font=("Sans Serif",20))

while True:
    button_event, input_value = window.read(timeout=400)
    todo_list = functions.get_todo()
    print(button_event)
    print(input_value)
    window["datetime"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    window["error"].update(value="")
    match button_event:
        case "Add":
            todo = input_value["todo"]
            if todo != "":
                todo_list.append(todo + "\n")
                write_todo(todo_list)
                window["todos"].update(values=todo_list)
            else:
                window["error"].update(value="Add todo can't be blank.")
                continue
        case "Edit":
            try:
                todo = input_value["todos"][0]
                new_todo = input_value["todo"] + "\n"

                get_index = todo_list.index(todo)
                todo_list[get_index] = new_todo
                functions.write_todo(todo_list)
                window["todos"].update(values=todo_list)
            except IndexError:
                window["error"].update(value="No to-do to edit.")
        case "todos":
            try:
                window["todo"].update(value=input_value["todos"][0])
            except IndexError:
                window["error"].update(value="No more to-do to select.")
        case "Complete":
            try:
                selected_todo = input_value["todos"][0]
                get_index = todo_list.index(selected_todo)
                todo_list.pop(get_index)
                functions.write_todo(todo_list)
                window["todos"].update(values=todo_list)
                window["todo"].update(value="")
            except IndexError:
                window["error"].update(value="No more to-do to complete.")
        case FreeSimpleGUI.WIN_CLOSED:
            break
        case "Exit":
            exit()


window.close()