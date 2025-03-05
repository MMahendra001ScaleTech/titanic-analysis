import json
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, description, due_date=None):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'Pending',
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("\nTask '{}' added successfully!".format(title))

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!")
            return

        print("\nYour Tasks:")
        print("-" * 60)
        for task in self.tasks:
            print("ID: {}".format(task['id']))
            print("Title: {}".format(task['title']))
            print("Description: {}".format(task['description']))
            print("Status: {}".format(task['status']))
            print("Due Date: {}".format(task['due_date'] or 'Not set'))
            print("Created: {}".format(task['created_at']))
            print("-" * 60)

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                self.save_tasks()
                print("\nTask {} marked as completed!".format(task_id))
                return
        print("\nTask with ID {} not found!".format(task_id))

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("\nTask {} deleted successfully!".format(task_id))
                return
        print("\nTask with ID {} not found!".format(task_id))

def main():
    task_manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            if due_date.strip() == "":
                due_date = None
            task_manager.add_task(title, description, due_date)
            
        elif choice == '2':
            task_manager.list_tasks()
            
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                task_manager.mark_completed(task_id)
            except ValueError:
                print("\nPlease enter a valid number!")
            
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("\nPlease enter a valid number!")
            
        elif choice == '5':
            print("\nThank you for using Task Manager!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()