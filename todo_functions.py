import tkinter as tk
from tkinter import messagebox

class Utils():
    """Utility class for handling tasks in a todo list"""

    def __init__(self, tasks, task_listbox, task_ent):
        self.tasks = tasks
        self.task_listbox = task_listbox
        self.task_ent = task_ent

    def add_task(self):
        """Defining the add task function"""  
        #Getting the value from the entry field
        task_value = self.task_ent.get()
        #check if the entry field is empty
        if len(task_value) == 0:
            #Dispaly an empty field message
            messagebox.showinfo("Error", "Field is Empty")
        else:
            #Adding the value to the tasks list
            self.tasks.append(task_value)
            #Calling the function to update the list
            self.list_update()     
            #deleting the task entry field
            self.task_ent.delete(0, tk.END)


    def list_update(self):
        """Defining the function to update the list"""
        #Calling the function to clear the list
        self.clear_list()
        #iterating through the string in the list
        for task in self.tasks:
            #using the insert method to insert the tasks in the listbox
            self.task_listbox.insert(tk.END, task)

    
    def delete_task(self):
        """Defining the delete task function"""
        #Using the try and except
        try:
            #Getting the selected entry from the task_listbox
            value = self.task_listbox.get(self.task_listbox.curselection())
            #checking if the selected value is in the tasks list
            if value in self.tasks:
                #remove the task from the list
                self.tasks.remove(value)
            #calling the function to update the list
            self.list_update() 
        except:
            #Displaying the message box with "No Task selected" message for an exception
            messagebox.showinfo("Error", "No Task Selected. Cannot Delete")

    
    def deleteAllTask(self):
        """Defining a function to delete all task"""
        #display a message box to ask user for confirmation
        confirmation = messagebox.askyesno("Delete All","Are you sure?")
        #If the value is true
        if confirmation:
            #using the while loop to iterate through the tasks list until its empty
            while (len(self.tasks) != 0):
                #using the clear method to clear out the elements in the list
                self.tasks.clear()
            #calling the function to update the list
            self.list_update()
            
    
    def clear_list(self):
        """Defining the function to clear the list"""
        #delete all enteries from the list box
        self.task_listbox.delete(0, tk.END)
