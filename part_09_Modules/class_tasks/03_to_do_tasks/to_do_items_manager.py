def display_menu():
    print("""
    Enter 1 to add new task
    Enter 2 to view all tasks
    Enter 3 To mark task as completed
    Enter 4 to delete a task
    Enter 5 to Exit
    
    """)
    user_choice = int(input())
    if user_choice < 6 or user_choice > 0:
