task_list = []
user_list = ["Admin", "User1", "User2"]
completed_list = []
while True:
    print("\n================================")
    print("       TASK MANAGEMENT SYSTEM")
    print("================================")
    print("1. Admin Section")
    print("2. User Section")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        password = input("Enter Admin Password: ")
        if password != "admin123":
            print("Wrong password!")
            continue
        while True:
            print("\n========== ADMIN SECTION ==========")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. View All Tasks")
            print("5. View Users")
            print("6. Exit")
            admin_choice = input("Enter your choice: ")
            if admin_choice == "1":

                task_name = input("Enter task name: ")
                status = input("Enter status: ")

                task_list.append([task_name, status])

                print("Task added successfully!")
            elif admin_choice == "2":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    print("\n----- TASK LIST -----")
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            task_list[i][0],
                            "-",
                            task_list[i][1]
                        )
                    number = int(input("Enter task number: "))
                    if number >= 1 and number <= len(task_list):
                        new_name = input("Enter new task name: ")
                        new_status = input("Enter new status: ")
                        task_list[number - 1][0] = new_name
                        task_list[number - 1][1] = new_status
                        print("Task updated successfully!")
                    else:
                        print("Invalid task number.")
            elif admin_choice == "3":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    print("\n----- TASK LIST -----")
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            task_list[i][0], "-",
                            task_list[i][1]
                        )
                    number = int(input("Enter task number to delete: "))
                    if number >= 1 and number <= len(task_list):
                        deleted = task_list.pop(number - 1)
                        print("Deleted task:", deleted[0])
                    else:
                        print("Invalid task number.")
            elif admin_choice == "4":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    print("\n========== ALL TASKS ==========")
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            ".",
                            task_list[i][0],
                            "-",
                            task_list[i][1])
            elif admin_choice == "5":
                print("\n========== USERS ==========")
                for user in user_list:
                    print(user)
            elif admin_choice == "6":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice!")
    elif choice == "2":

        username = input("Enter username: ")

        if username not in user_list:
            print("User not found!")
            continue
        while True:
            print("\n========== USER SECTION ==========")
            print("1. View My Tasks")
            print("2. Add Task")
            print("3. Update My Task")
            print("4. Delete My Task")
            print("5. Mark Task Complete")
            print("6. Exit")
            user_choice = input("Enter your choice: ")
            if user_choice == "1":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    print("\n========== MY TASKS ==========")
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            ".",
                            task_list[i][0],
                            "-",
                            task_list[i][1])
            elif user_choice == "2":
                task_name = input("Enter task name: ")
                task_list.append([task_name, "Pending"])
                print("Task added successfully!")
            elif user_choice == "3":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            ".",
                            task_list[i][0],
                            "-",
                            task_list[i][1]
                        )
                    number = int(input("Enter task number: "))
                    if number >= 1 and number <= len(task_list):
                        new_name = input("Enter new task name: ")
                        new_status = input("Enter new status: ")
                        task_list[number - 1][0] = new_name
                        task_list[number - 1][1] = new_status
                        print("Task updated successfully!")
                    else:
                        print("Invalid task number.")
            elif user_choice == "4":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            ".",
                            task_list[i][0],
                            "-",
                            task_list[i][1]
                        )
                    number = int(input("Enter task number to delete: "))
                    if number >= 1 and number <= len(task_list):
                        deleted = task_list.pop(number - 1)
                        print("Deleted:", deleted[0])
                    else:
                        print("Invalid task number.")

            elif user_choice == "5":
                if len(task_list) == 0:
                    print("No tasks available.")
                else:
                    for i in range(len(task_list)):
                        print(
                            i + 1,
                            ".",
                            task_list[i][0],
                            "-",
                            task_list[i][1]
                        )
                    number = int(
                        input("Enter task number to complete: ")
                    )
                    if number >= 1 and number <= len(task_list):
                        task_list[number - 1][1] = "Completed"
                        completed_list.append(
                            task_list[number - 1][0])
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
            elif user_choice == "6":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice!")
    elif choice == "3":

        print("\nThank you for using Task Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
