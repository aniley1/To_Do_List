import tkinter as tk
from todo import TodoList

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")

        self.todo_list = TodoList()
        self.todo_list.load_from_file("tasks.txt")

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.list_button = tk.Button(root, text="List Tasks", command=self.list_tasks)
        self.list_button.pack()

        self.save_quit_button = tk.Button(root, text="Save and Quit", command=self.save_and_quit)
        self.save_quit_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.todo_list.add_task(task)
        self.task_entry.delete(0, tk.END)

    def remove_task(self):
        task = self.task_entry.get()
        self.todo_list.remove_task(task)
        self.task_entry.delete(0, tk.END)

    def list_tasks(self):
        tasks_text = "\n".join(self.todo_list.tasks) if self.todo_list.tasks else "No tasks found."
        tasks_window = tk.Toplevel(self.root)
        tasks_window.title("Tasks")
        tasks_label = tk.Label(tasks_window, text=tasks_text)
        tasks_label.pack()

    def save_and_quit(self):
        self.todo_list.save_to_file("tasks.txt")
        self.root.quit()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
