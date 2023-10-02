tasks = []


def display_menu():
    print("Enter 1 to add new task\n"
          "Enter 2 to view all tasks\n"
          "Enter 3 To mark task as completed\n"
          "Enter 4 to delete a task\n"
          "Enter 5 to Exit\n"
          "")
    return int(input("Enter your choice: "))


def add_task():
    task_name = (input("Enter the task name: "))
    task_completed_status = False
    new_task = (task_name, task_completed_status)
    tasks.append(new_task)
    if new_task in tasks:
        print(f"{task_name} was added successfully")
    else:
        print(f"{task_name} added FAILED!!")


def view_tasks():
    print(f"Task:\t|\tCompleted:")
    print("---------------------------")
    for task, status in tasks:
        print(f"{task}\t    |\t{status}")


def get_task_index():
    for task in tasks:
        print(f"{tasks.index(task)+1}. {task[0]}")
    return int(input("enter the number of the task: "))-1


def mark_complete():
    user_task = get_task_index()
    tasks[user_task] = (tasks[user_task][0], True)
    print(f"The task: {tasks[user_task][0]} complete status change to: {tasks[user_task][1]}")


def delete_task():
    user_task = get_task_index()
    print(f"The task: {tasks.pop(user_task)[0]} was removed.")


def main():
    while True:
        user_choice = display_menu()
        match user_choice:
            case 1:  # add new task
                add_task()
            case 2:  # view all tasks
                view_tasks()
            case 3:  # mark task as completed
                mark_complete()
            case 4:  # delete a task
                delete_task()
            case 5:  # exit
                quit()
        print("")


if __name__ == '__main__':
    main()

