import os #dima hwa lowal kat3awna n3arfo wach lmilf kayn wla la

#  hado homa lma3lamiya dyal lhifad wa lqira2a (functions) dawal

def load_data():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
        
    return []
    
def save_data(tasks_list):
    with open("tasks.txt", "w") as file:
        for item in tasks_list:
            file.write(item + "\n")

 #had star hwa li kayjib lmaham o kayhnina mn lkhaatae lhmrae
tasks = load_data()

print("---my task manager---")

#db 3ad kaybda lqalb dyal lbrnamaj.
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. Delete Task")
    print("5. Edit Task")

    choice = input("select an option: ") 

    if choice == "3":
        save_data(tasks) #kansajlo kolchi qbal ma nkharjo
        print("Goodbye")
        break

    elif choice == "1":
        new_task = input( "Enter your task: ")
        tasks .append(new_task)
        save_data(tasks) #hifd fawri
        print("Task added and saved")

    elif choice == "2": 
        print("\n--- your tasks List ---")
        if not tasks:
            print("the list is empty")
        else:
            #hiya li kat3tina raqm dyal kol mohima tilqaeyan
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\n--- your tasks List ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Enter the number of the task to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_data(tasks)
                    print(f"Task '{deleted_task}' deleted and saved.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        if not tasks:
            print("No tasks to edit.")
        else:
            print("\n--- your tasks List ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Enter the number of the task to edit: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter the new task: ")
                    tasks[task_num - 1] = new_task
                    save_data(tasks)
                    print("Task updated and saved.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("nothing to delete")
        else:
            try:
                #hna fin ghaymsah b raqm
                num = int(input("enter the task number to delete: "))
                #kanmasho btartib (pop)
                removed = tasks.pop(num - 1)
                save_data(tasks) #kansajlo taghyir daqa wahda)
                print(f"Task '{removed}' deleted!")
            except:
                print("Invalid number! please enter a real task number.")
    else:    
                print("Invalid choice! please enter 1, 2, or 3,")


        

