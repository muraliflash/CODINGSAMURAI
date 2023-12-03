import os

class TodoList:
    def __init__(self):
        self.tasks = []
        self.file_path = "todolist.txt"
        self.load_tasks()

    def display_menu(self):
        print("\n----- To-Do List Menu -----")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Quit")

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task = {"title": title, "description": description, "completed": False}
        self.tasks.append(task)
        print("Task added successfully!")

    def list_tasks(self):
        print("\n----- Task List -----")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['title']} - {task['description']} ({status})")

    def mark_complete(self):
        self.list_tasks()
        try:
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            self.tasks[task_index]["completed"] = True
            print("Task marked as complete!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self):
        self.list_tasks()
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            del self.tasks[task_index]
            print("Task deleted successfully!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(f"{task['title']}|{task['description']}|{task['completed']}\n")

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    title, description, completed_str = line.strip().split("|")
                    completed = True if completed_str == "True" else False
                    task = {"title": title, "description": description, "completed": completed}
                    self.tasks.append(task)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.mark_complete()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.save_tasks()
                print("Tasks saved. Quitting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()
