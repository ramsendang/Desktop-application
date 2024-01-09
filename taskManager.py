from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb 
from functions.jsons import *
from functions.events import *
filePath = "db.json"
root = tb.Window(themename="solar")
root.title("Task Manger App")
root.geometry("1600x800")
colors = root.style.colors
#create a Heading of the window
welcomeMessage = tb.Label(text="Welcome to Task Manager App", bootstyle="primary", font=("Arial", 22))
welcomeMessage.pack()

# Availabe Task List 
container = tb.Frame(root, bootstyle="dark")
container.pack(pady = 40)

# displaying task list
showTasks(filePath, container, colors)



root.mainloop()