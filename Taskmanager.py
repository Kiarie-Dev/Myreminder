from datetime import datetime
import os
import json
from typing import List, Dict


# Constants
ERROR_READING_FILE_MSG = "Error reading tasks file. Starting with an empty task list!"
TASKS_FILE = 'tasks.json'
ERROR_SAVING_TASKS_MSG = "Error saving tasks!"
INCOMPLETE_TASKS_MSG = "You have incomplete tasks:"
NO_TASKS_MSG = "You have no tasks."
INVALID_CHOICE_MSG = "Invalid choice. Please try again."


class TaskManager:
    def __init__(self, name: str):
        self.name = name
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict[str, str]]:
        """Loading files from a JSON file."""
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(ERROR_READING_FILE_MSG)
                return []
            return []
    
    def save_tasks(self) -> None:
        """Save tasks to a JSON file."""
        try:
            with open(TASKS_FILE, 'w') as file:
                json.dump(self.talks, file, indent=4)
        except IOError:
            print(ERROR_SAVING_TASKS_MSG)


    def start_up(self):
        """Start the application and present options to the user."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Today is {current_date}. What are you planning, {self.name}?")

        if self.tasks:
            print(INCOMPLETE_TASKS_MSG)
            self.view_tasks(only_incomplete=True)
        else:
            print(NO_TASKS_MSG)
        
        while True:
            print("\nOptions:")
            print("1. View all tasks")
            print("2. Add a new task")
            print("3. Delete a task")
            print("4. Mark a task as complete")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.mark_task_complete()
            elif choice == '5':
                break
            else:
                print(INVALID_CHOICE_MSG)
        

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start_up()