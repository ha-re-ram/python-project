# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

    def mark_task_completed(self, task_number):
        try:
            self.tasks[task_number - 1] = f"[X] {self.tasks[task_number - 1]}"
        except IndexError:
            print("Invalid task number.")

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task completed")
        print("4. Display tasks")
        print("5. Quit")

        option = input("Choose an option: ")

        if option == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif option == "2":
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif option == "3":
            task_number = int(input("Enter the task number to mark completed: "))
            todo_list.mark_task_completed(task_number)
        elif option == "4":
            todo_list.display_tasks()
        elif option == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()