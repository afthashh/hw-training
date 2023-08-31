import json
from datetime import datetime

class EmployeeLog:
    task_list = []

    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.login_time = None
        self.logout_time = None
        self.tasks = []

    def log_in(self):
        self.login_time = datetime.now()

    def log_out(self):
        if self.login_time is not None:
            self.logout_time = datetime.now()
            self.create_json_file()

    def add_task(self):
        if self.login_time is None:
            print("Please log in first.")
            return

        task_title = input("Enter task title: ")
        task_description = input("Enter task description: ")
        task_success = input("Was the task successful? (y/n): ").lower() == "y"

        start_time = datetime.now()
        task = {
            "task_title": task_title,
            "task_description": task_description,
            "start_time": start_time.strftime('%Y-%m-%d %H:%M'),
            "end_time": None,
            "task_success": task_success
        }
        self.tasks.append(task)

    def end_task(self):
        if self.login_time is None:
            print("Please log in first.")
            return

        if not self.tasks:
            print("No tasks to end.")
            return

        end_time = datetime.now()
        self.tasks[-1]["end_time"] = end_time.strftime('%Y-%m-%d %H:%M')

    def create_json_file(self):
        if self.login_time is None or self.logout_time is None:
            print("Cannot create JSON file without proper login/logout times.")
            return

        json_data = {
            "emp_name": self.emp_name,
            "emp_id": self.emp_id,
            "login_time": self.login_time.strftime('%Y-%m-%d %H:%M'),
            "logout_time": self.logout_time.strftime('%Y-%m-%d %H:%M'),
            "tasks": self.tasks
        }

        filename = f"{self.emp_name}_{self.login_time.strftime('%Y-%m-%d')}.json"
        with open(filename, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        EmployeeLog.task_list.append(json_data)


emp_name = input("Enter your name: ")
emp_id = int(input("Enter your employee ID: "))
employee = EmployeeLog(emp_name, emp_id)
employee.log_in()

while True:
    choice = input("Select an option: 1 - Add task, 2 - End task, 3 - Log out, 4 - Exit: ")
    
    if choice == "1":
        employee.add_task()
    elif choice == "2":
        employee.end_task()
    elif choice == "3":
        employee.log_out()
        break
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print(json.dumps(EmployeeLog.task_list, indent=4))
