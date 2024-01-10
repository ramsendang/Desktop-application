from tkinter import *
from functions.actions import *
# tkinter._test()
master = Tk()
master.geometry("1200x600")
file_path = "database.json"
showTask(file_path, master)
addTaskForm(master)



# grid method to arrange label in respective 

master.mainloop()