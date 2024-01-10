from tkinter import *
# tkinter._test()
master = Tk()
master.geometry("500x200")
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

idData = Label(frame, text="id")
taskData = Label(frame, text="task")
descriptionData = Label(frame, text="Description")
timeData = Label(frame, text="Due Date")
statusData = Label(frame, text="status")
deleteButton = Button(frame, text="Delete", bd= '5', command=master.destroy)

# grid view
idData.grid(row=2, column=0, sticky=W, pady=2)
taskData.grid(row=2, column=1, sticky=W, pady=2)
descriptionData.grid(row=2, column=2, sticky=W, pady=2)
timeData.grid(row=2, column=3, sticky=W, pady=2)
statusData.grid(row=2, column=4, sticky=W, pady=2)
deleteButton.grid(row=2, column=5, sticky=W, pady=2)


frame.pack()



# grid method to arrange label in respective 

master.mainloop()