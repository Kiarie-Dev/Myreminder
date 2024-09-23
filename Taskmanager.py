from datetime import datetime
import os
import json
from typing import List, Dict


# Constants
ERROR_READING_FILE_MSG = "Error reading tasks file. Starting with an empty task list!"
TASKS_FILE = 'tasks.json'


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

    def start_up(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Today is {current_date}. What are you planning, {self.name}?")
        

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start_up()