import tkinter as tk
from tkinter import filedialog
def save_tasks(self):
    tasks = self.tasks_listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task.partition("[")[0].strip() + "\n")


class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

      
        self.geometry("400x400")
        self.title("To-Do List")

        self.create_widgets()

    def create_widgets(self):
        self.task_input = tk.Entry(self, width=30)
        self.task_input.pack(pady=10)

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=5)
        self.tasks_listbox.bind("<ButtonRelease-1>", self.toggle_task_completion)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=5)

        self.edit_task_button = tk.Button(self.button_frame, text="Edit Task", command = self.edit_task)
        self.edit_task_button.grid(row=0, column=0, padx=5)  #initiall column = 0

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command = self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=5)  # Changed column to 1

        self.save_button = tk.Button(self, text="Save", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self, text="Load", command=self.load_tasks)
        self.load_button.pack(pady=5)  

    def add_task(self):
        task = self.task_input.get()
        if task:
            task_data = f"{task} [ ]"  # Task description with checkbox
          
            self.tasks_listbox.insert(tk.END, task_data)
            self.task_input.delete(0, tk.END)

    def edit_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            new_task = self.task_input.get()
            if new_task:
                task_data = f"{new_task} [ ]"  # Task description with checkbox
                self.tasks_listbox.delete(task_index)
                self.tasks_listbox.insert(task_index, task_data)
                self.task_input.delete(0, tk.END)

    def delete_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            self.tasks_listbox.delete(task_index)

    def save_tasks(self):
        tasks = self.tasks_listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task.partition("[")[0].strip() + "\n")  
    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]

            self.tasks_listbox.delete(0, tk.END)

            for task in tasks:
                self.tasks_listbox.insert(tk.END, task)

    def toggle_task_completion(self, event):
        widget = event.widget
        index = widget.nearest(event.y)
        task = widget.get(index)
        if task.endswith("[ ]"):
            widget.delete(index)
            widget.insert(index, task[:-3] + "[\u2713]")  # Mark task as completed
        elif task.endswith("[\u2713]"):
            widget.delete(index)
            widget.insert(index, task[:-3] + "[ ]")  # Mark task as not completed


