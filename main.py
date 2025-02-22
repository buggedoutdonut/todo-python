from functions import get_todo, write_todo
import time

todo_list = get_todo()

while True:
    user_command = input("Do you want to add, show, edit, complete to-do or exit? ").strip()

    if user_command.upper().startswith("ADD "):
        add_todo = user_command[4:] + "\n"
        todo_list.append(add_todo.capitalize())

        write_todo("todo.txt",todo_list)

    elif user_command.upper().startswith("SHOW"):
        if len(todo_list) < 1:
            print("No to-do to show.")
        else:
            for index, item in enumerate(todo_list):
                newItem = item.strip("\n")
                print(f"{index + 1}. {newItem}")

    elif user_command.upper().startswith("EDIT "):
        try:
            select_index = int(user_command[5:])
            edit_todo = input("What would be the new todo? ")
            todo_list[select_index-1] = edit_todo

            write_todo("todo.txt", todo_list)
            print("Edit successful.")
        except ValueError:
            print("Please type the index of the todo.")

    elif user_command.upper().startswith("COMPLETE "):
        try:
            select_index = int(user_command[9:])
            print(f"{todo_list[select_index-1].strip("\n")} has been completed.")
            todo_list.pop(select_index-1)

            write_todo("todo.txt", todo_list)
        except (IndexError, ValueError, SyntaxError):
            print("Index does not exist.")

    elif "EXIT" in user_command[:4].upper():
        break

    else:
        print("Invalid command.")

