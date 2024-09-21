from datetime import datetime


class TaskManager:
    def __init__(self, name: str):
        self.name = name
        
    def start_up(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Today is {current_date}. What are you planning, {self.name}?")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start_up()