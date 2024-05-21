#!/usr/bin/python3
""" using API in python"""


if __name__ == "__main__":
    import requests
    import sys

    # getting value from terminal
    if len(sys.argv) < 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    else:
        id = int(sys.argv[1])

    # main url
    URL = "https://jsonplaceholder.typicode.com/"

    # params
    param = {
        "userId": id
    }
    # get the  user
    user = requests.get(URL + "/users", params=param)
    user = user.json()
    employee_name = user[id].get('name')

    # get todos
    todos = requests.get(URL + "/todos", params=param).json()

    # ratio of completed tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]
    completed_count = len(completed_tasks)
    total_task = len(todos)

    # output the results
    print(
        f"Employee {employee_name} is done with tasks(
            {completed_count}/{total_task})")

    # task title
    for task in completed_tasks:
        print(f"\t {task}")