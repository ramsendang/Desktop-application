from functions.json import *
from tkinter import *
from functions.actions import *

def delete(json_file_path, target_value, frame):
    # Read JSON data from the json file path 
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Identify keys associated with the specified value
    keys_to_delete = [key for key, value in json_data.items() if any(v == target_value for v in value.values())]

    # Delete key-value pair(s) associated with the specified value
    for key_to_delete in keys_to_delete:
        del json_data[key_to_delete]

    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
    frame.pack_forget()
    frame.pack()

def showTask(file_path, master):
    data = readJson(file_path)
    frame = Frame(master)
    title = Label(frame, text="Task Manager")
    title.grid(row=0, column= 3, sticky= W, pady=2)
    id = Label(frame, text="id")
    task = Label(frame, text="task")
    description = Label(frame, text="Description")
    time = Label(frame, text="Due Date")
    status = Label(frame, text="status")
    action = Label(frame, text="Actions")

    id.grid(row=1, column=0, sticky=W, pady=2)
    task.grid(row=1, column=1, sticky=W, pady=2)
    description.grid(row=1, column=2, sticky=W, pady=2)
    time.grid(row=1, column=3, sticky=W, pady=2)
    status.grid(row=1, column=4, sticky=W, pady=2)
    action.grid(row=1, column=5, sticky=W, pady=2)

    keys = list(data.keys())  # Get list of task IDs
    index = 0
    rowNumber = 2
    while index < len(keys):
        id= keys[index]
        taskInfo = data[id]
        idData = Label(frame, text=id)
        taskData = Label(frame, text=taskInfo['task'] )
        descriptionData = Label(frame, text=taskInfo['details'])
        timeData = Label(frame, text=taskInfo['due date'])
        statusData = Label(frame, text=taskInfo['status'])
        deleteButton = Button(frame, text="Delete", bd= '5', command=delete(file_path, taskInfo['task'], frame))
        updateButton = Button(frame, text="Update", bd= '5', command=frame.destroy)
    
        idData.grid(row=rowNumber, column=0, sticky=W, pady=2)
        taskData.grid(row=rowNumber, column=1, sticky=W, pady=2)
        descriptionData.grid(row=rowNumber, column=2, sticky=W, pady=2)
        timeData.grid(row=rowNumber, column=3, sticky=W, pady=2)
        statusData.grid(row=rowNumber, column=4, sticky=W, pady=2)
        deleteButton.grid(row=rowNumber, column=5, sticky=E, pady=2)
        updateButton.grid(row=rowNumber, column=6, sticky=E, pady=2)
        rowNumber +=1
        index += 1
    frame.pack()

def addTaskForm(master):
    form = Frame(master)
    taskLabel = Label(form, text="Task Name")
    taskEntry = Entry(form, width=50)
    text_var = StringVar()
    taskEntry['textvariable']= text_var

    form.pack()
    


