#importing the required modules
import tkinter as tk
from tkinter import ttk
from todo_functions import Utils

#main function
if __name__ == "__main__":
    #creating a window
    window = tk.Tk()
    #setting the title of the window
    window.title("To-Do List")
    #setting the geometry of the window
    window.geometry("400x500")
    #Setting window not to be resizable
    window.resizable(width=False, height=False)
    #setting window background color
    window.configure(bg="#87CEEB")

    #Defining an empty list
    tasks = []
    
    #defining frame
    frm =ttk.Frame(window)
    #using the pack method to place the frame in the window
    frm.place(x=20, y=150)

    #creating a label using the Label() widget
    label = tk.Label(master=window,
        text="Enter the task:",
        font=("Terminal", 20),
        background="sky blue",
        foreground="black")
    
    #using the place method to place the label in the window
    label.place(x=20, y=50)

    #defining an entry field with the Entry() widget
    task_ent = tk.Entry(
        master=window,
        width=40)
    
    #using the place method to place the task entry field in the window
    task_ent.place(x=20, y=100)

    #creating the add task button
    addtask_btn = tk.Button(
        master=window,
        text="Add Task",
        foreground="Black",
        background="Red")

    #using the place method to place the add task button in the window
    addtask_btn.place(x=270, y=97)

    #creating the delete task button
    del_btn = tk.Button(
        master=window,
        text="Delete Task",
        foreground="Black",
        background="Red")
    
    #Using the place method to place the delete button in the window
    del_btn.place(x=50, y=420)

    #creating the delete all task button
    delall_btn = tk.Button(
        master=window,
        text="Delete All Task",
        foreground="Black",
        background="Red")
    
    #Using the place method to place the button in the window
    delall_btn.place(x=200, y=420)

    #creating the list box for the tasks
    task_listbox = tk.Listbox(
        master=frm,
        width=50,
        height=15,
        background="Light Blue",
        selectmode=tk.SINGLE)
    
    #creating a scroll bar
    scrollbar = ttk.Scrollbar(frm, command=task_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    #styling the scrollbar
    style = ttk.Style()
    style.configure("Vertical.TScrollbar", troughcolor="grey80",)

    #Applying the modified style to the scrollbar
    style.configure(style="Vertical.TScrollbar")

    #Attaching the scrollbar to the task_listbox widget
    task_listbox.configure(yscrollcommand=scrollbar.set)

    #using the place method to place the 
    #task_listbox in the window
    task_listbox.pack(side=tk.LEFT, expand=True, fill="both")
 
    #Create Utils object and pass the necessary argument
    utils = Utils(tasks, task_listbox, task_ent)

    #Updating the button command with the corresponding methods
    addtask_btn.config(command=utils.add_task)
    del_btn.config(command=utils.delete_task)
    delall_btn.config(command=utils.deleteAllTask)

    #start the application
    window.mainloop()