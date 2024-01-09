from tkinter import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import ttkbootstrap as tb 
from functions.jsons import *
def showTasks(filePath, container, colors):
    tasks = readJson(filePath)
    message = tb.Label(container, text="Your Abailable Task are :")
    message.pack(pady=10, padx=10)
    
    coldata = [
        {"text": "Task", "stretch": False},
        "Task Details",
        {"text": "Due Date", "stretch": False},
        {"text": " Status ", "stretch": False},
        {"text": " Actions ", "stretch": False},
    ]
    
    table = Tableview(
            master=container,
            coldata=coldata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None)
        )

    table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    # filling the tables rows 
    
    for key, entry in tasks.items():
        table.insert_row("end", [entry['task'],entry['details'], entry['due date'], entry['status'], tb.Label(master=table, bootstyle="danger", text="Delete").pack()] )