#!/usr/bin/python3
"""A Python script that, for a given employee ID,
returns infomation about his/her TODO list progress.
"""

if __name__ == "__main__":
    """ required modules """
    import request
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    id = int(sys.argv[1])
    URL = "https://jsonplaceholder.typicode.com/"
    param = {"userId": id}

    user = requests.get(URL + "/users", params=param).json()
    employee_name = user[id].get('name')
    todos = requests.get(URL + "/todos", params=param).json()

    completed_tasks = [task['title'] for task in todos if task['completed']]
    completed_count = len(completed_tasks)
    total_task = len(todos)

    print(
        f"Employee {employee_name} is done with tasks(
            {completed_count}/{total_task})")

    for task in completed_tasks:
        print(f"\t {task}")
