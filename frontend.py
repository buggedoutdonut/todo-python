import functions
import FreeSimpleGUI


label = FreeSimpleGUI.Text("Hi type to do")
input_box = FreeSimpleGUI.InputText(tooltip="To-Do")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("My App",layout=[[label, input_box, add_button]])
window.read()
window.close()