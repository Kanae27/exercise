# The tasks are stored in memory and can be managed through a command-line interface.
class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.title}: {self.description}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for idx, task in enumerate(self.tasks):
            print(f"{idx+1}. {task}")

    def view_task(self, index):
        if 0 <= index < len(self.tasks):
            print(f"Task {index+1}:")
            print(f"Title: {self.tasks[index].title}")
            print(f"Description: {self.tasks[index].description}")
        else:
            print("Invalid task index.")

    def update_task(self, index, title=None, description=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            print("Task updated.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted.")
        else:
            print("Invalid task index.")

def main():
    task_list = TaskList()
    while True:
        print("\nTask Lister - Choose an option:")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. View Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Task title: ")
            desc = input("Task description: ")
            task_list.create_task(title, desc)
        elif choice == "2":
            task_list.list_tasks()
        elif choice == "3":
            task_list.list_tasks()
            idx = int(input("Enter task number to view: ")) - 1
            task_list.view_task(idx)
        elif choice == "4":
            task_list.list_tasks()
            idx = int(input("Enter task number to update: ")) - 1
            title = input("New title (leave blank to keep current): ")
            desc = input("New description (leave blank to keep current): ")
            task_list.update_task(idx, title if title else None, desc if desc else None)
        elif choice == "5":
            task_list.list_tasks()
            idx = int(input("Enter task number to delete: ")) - 1
            task_list.delete_task(idx)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
