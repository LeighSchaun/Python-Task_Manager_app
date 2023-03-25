
# Importing date module
from datetime import date
import calendar

# creating list that will latr be used to stor input and data from text files
tasks = []
users_names = []
users_password = []
count = 0

# Defining the date function that will collect and convert dates
def get_date():
    todays_date = date.today()
    current_year = todays_date.year
    current_month = todays_date.month
    current_day = todays_date.day
    month_abbr = calendar.month_abbr[current_month]
    
    return f"{current_day} {month_abbr} {current_year}"

# Defining the register user function that takes current username and current_usernames list as arguments
def reg_user(current_user, current_usernames):
    print("Please register new user.")
    print()
    # Checks if the current user is logged in as admin
    if current_user == "admin":
        new_username = input("Please enter the new username: ")
        new_password = input("Please enter the new password: ")
        confirm_new_password = input("Please confirm the new password: ")

        # While loop to check if the user exists in the current users list
        while new_username in current_usernames:
            new_username = input("Sorry That user already exists please enter "
            "a different username: ")
        # If the username entered does not exist,the user can adda anew user
        if new_password == confirm_new_password:
            users_names.append(new_username)
            users_password.append(new_password)

            # Opens the text file that contains the current user details
            with open('user.txt', 'w', encoding='utf-8') as write_user:
                # Loops through the current users
                for index in range(len(users_names)):

                    # Writes the new user to the user.txt file
                    write_user.write(f"{users_names[index]}, "
                                        f"{users_password[index]}\n")
            # Lets the user know the new yser has been added
            print("New user added successfully")

        # Message displayed if the passwords entered does not match
        else:
            print("The new password does not match what you entered as the "
                    "confirmation password, Please try again.")
    # Displays if the user is not Admin
    else:
        print("Registering users is restricted to Admin access only")

# Defining a function to add a new task
def add_task():
    print("Please add a new task")
    print()

    #Prompts user for details of the new 
    new_task_user = input("Please enter the user for the new task: ")
    new_task_title = input("Please enter the task title for the new "
                            "task: ")
    new_task_des = input("Please enter the task description for the new "
                            "task: ")
    # Calls the get date function to convert and add the date to the task
    new_task_date = get_date()
    new_task_due = input("Please enter the task due date for the new "
                            "task in this format '06 Jan 2022': ")
    new_task_status = "No"

    new_task = f"{new_task_user}, {new_task_title}, {new_task_des}, "\
                f"{new_task_date}, {new_task_due}, {new_task_status}"

    # Adds the new task to the taks list
    tasks.append(new_task)

    # Opens the tasks file to append the new task to the file
    with open('tasks.txt', 'a', encoding='utf-8') as write_tasks:
        for index in range(len(tasks)):
                write_tasks.write(f"{tasks[index]}\n")

# Defines a function to update tasks
def update_tasks():
    # Opens the tasks file to read tasks
    with open('tasks.txt', 'r+', encoding='utf-8') as update_tasks:

        # Loops through tasks in task file
        for i in range(len(tasks)):
                # Writes the tasks to the tasks file
                update_tasks.write(f"{tasks[i]}\n")

# Defining a function to view all tasks
def view_all():
    print("Below is a list of your tasks")
    print()

    # Loops through tasks in the text file
    for task in tasks:
        task = task.split(", ")

        # Prints the task a easy to read manner for the user
        print(f"Assigned to:\t\t{task[0]}\nTask title:\t\t{task[1]}\n"
            f"Task description:\t{task[2]}\nAssigned date:\t\t{task[3]}\n"
            f"Due date:\t\t{task[4]}\nTask completed:\t\t{task[5]}\n")

# Defining a function to view all tasks entered
def view_mine():
    print("Below is a list of all tasks")
    print()

    # Creating a for loop to find the index of each tasks
    for index, task in enumerate(tasks):
        task = task.split(",")

        

        # checks which user is logged in and prints the tasks for that user
        if task[0] == username:
            

            # Prints the list of tasks associated to the user logged in
            print(f"Task number:\t\t {count}\nAssigned to:\t\t {task[0]}\nTask title:\t\t{task[1]}\n"
                f"Task description:\t{task[2]}\nAssigned date:\t\t{task[3]}\n"
                f"Due date:\t\t{task[4]}\nTask completed:\t\t{task[5]}\n"
                )

    selected_task = int(input("From selection of tasks above enter one of the "
                            "'Current task selection number' in order to "
                            "select that task to be marked as completed or"
                            " to edit the task. If you would like to "
                            "return to the main menu enter '-1': "))

    # Stores the tasks selected
    current_task = tasks[selected_task]
    
    print("")

    # Returns to main menu if user selects - 1
    if selected_task == -1:
        return

    # Checks if completion status of the task is already yes
    elif current_task[-3:] != "Yes":

        # Executes if user selects a task number
        if selected_task != -1:
            user_choice = input("Type 'm' to mark the current task as "
                                "completed, Or type 'e' to edit the current"
                                " task: ").lower()

            print("")

            # Marks the tasks complete if user selects m
            if user_choice == "m":
                tasks[selected_task] = tasks[selected_task].replace("No", "Yes")
                update_tasks()
                print("Current task has been marked as completed.\n")

            else:
                edit_selection = input("What would you like to edit, "
                    "'username' Or 'duedate'  "
                    "of the task: ").lower()

                # Allows the user to edit the username
                if edit_selection == "username":
                    current_task = current_task.split(",")
                    current_user = current_task[0]
                    
                    # Display the current user and request the details to change
                    user_replacement = input("The current user is "
                        f"{current_user}, Who would you like to change it "
                        "to: ")

                    tasks[selected_task] = tasks[selected_task].split(", ")
                    tasks[selected_task][0] = user_replacement
                    tasks[selected_task] = ", ".join(tasks[selected_task])

                    # Calls the update tasks function
                    update_tasks()
                    print("The Current task has been reassigned to "
                        f"{user_replacement}.\n")
                # Allows the user to edit the due date
                elif edit_selection == "duedate":
                    current_task = current_task.split(",")
                    current_due_date = current_task[4]

                    due_date_replacement = input("The current due date is "
                        f"{current_due_date}, What would you like to change it "
                        "to e.g. '20 Jan 2022'. Please use that format: ")

                    tasks[selected_task] = tasks[selected_task].split(', ')
                    tasks[selected_task][4] = due_date_replacement
                    tasks[selected_task] = ", ".join(tasks[selected_task])

                    # Calls the update task function
                    update_tasks()
                    print("The current tasks due date has been changed from"
                        f"{current_due_date} to {due_date_replacement}\n")

                else:

                    # Displays if the user enters an invalid option
                    return print("Sorry please choose only 'username' or 'duedate' to"
                        " edit the selected task.\n")
    else:
        print("Sorry you can only edit tasks that have not been marked as "
                "completed yet.\n")

# Definies a funtion to check tasks completion dates vs due dates
def compare_date(user_tasks):
    current_date = get_date() 
    current_date_split = current_date.split(" ")
    current_year = current_date_split[2]
    current_month = current_date_split[1]
    current_day = current_date_split[0]
    current_month_as_num = list(calendar.month_abbr).index(current_month)
    compare_current_date = date(int(current_year), int(current_month_as_num), int(current_day))

    # Sets overdue tasks to 0
    total_overdue_uncompleted = 0

    for task in user_tasks:
        task = task.split(", ")
        if task[-1] == "No":
            due_date = task[-2]
            due_date_split = due_date.split(" ")

            due_year = due_date_split[2]
            due_month = due_date_split[1]
            due_day = due_date_split[0]
            due_month_as_num = list(calendar.month_abbr).index(due_month)
            compare_due_date = date(int(due_year), int(due_month_as_num), int(due_day))

            # Checks if tasks is overdue by comparing current date to the due date entered
            is_overdue_uncompleted = compare_current_date > compare_due_date

            # increments the uncompleted overdue tasks if tasks overdue is  == True
            if is_overdue_uncompleted == True:
                total_overdue_uncompleted += 1

    return total_overdue_uncompleted

# Defines a functio to compare dates for each user who has overdue tasks
def compare_users_date():
    current_date = get_date() 
    current_date_split = current_date.split(" ")
    current_year = current_date_split[2]
    current_month = current_date_split[1]
    current_day = current_date_split[0]
    current_month_as_num = list(calendar.month_abbr).index(current_month)
    current_date = date(int(current_year), int(current_month_as_num), int(current_day))

    users_dict = {}
     
    with open('tasks.txt', 'r', encoding='utf-8') as f:
        for task in f:
            
            task = task.replace("\n", "")
            task = task.split(", ")

            due_date = task[-2]
            due_date_split = due_date.split(" ")

            due_year = due_date_split[2]
            due_month = due_date_split[1]
            due_day = due_date_split[0]
            due_month_as_num = list(calendar.month_abbr).index(due_month)
            due_date = date(int(due_year), int(due_month_as_num), int(due_day))

            # Checks if task is not completed but overdue
            if (task[-1] == "No") and (current_date > due_date): 
                user = task[0]
                
                if user in users_dict:
                    users_dict[user] += 1
                else:
                    users_dict[user] = 1

    return users_dict

# This generates the 'task_overview.txt' file with the required information to generate the overview or report
def generate_task_overview():
    total_tasks = 0
    total_completed_tasks = 0
    total_uncompleted_tasks = 0
    total_uncompleted_overdue_tasks = compare_date(tasks)

    for task in tasks:
        task = task.split(", ")
        total_tasks += 1

        if task[-1] == "Yes":
            total_completed_tasks += 1
        elif task[-1] == "No":
            total_uncompleted_tasks += 1

    # Calculates the percentage of incomplete tasks
    percentage_incomplete = (total_uncompleted_tasks/total_tasks) * 100

    # Calculates the percentage of tasks overdue
    percentage_overdue = (total_uncompleted_overdue_tasks/total_tasks) * 100

    # Writes the detailed statistics to the overview file
    with open('task_overview.txt', 'w', encoding='utf-8') as write_task_overview:
        write_task_overview.write("The total number of tasks that have been "
            f"generated and tracked: {total_tasks}\nThe total number of "
            f"completed tasks: {total_completed_tasks}\nThe total number of "
            f"uncompleted tasks: {total_uncompleted_tasks}\nThe total number "
            "of tasks that haven't been completed and that are overdue: "
            f"{total_uncompleted_overdue_tasks}\nThe percentage of tasks that "
            f"are incomplete: {percentage_incomplete}%\nThe percentage of tasks"
            f" that are overdue: {percentage_overdue}%\n")

    print("Task overview has been generated in 'task_overview.txt'.\n")

# This generates the 'user_overview.txt' file with the required information to generate the overview or report
def user_overview():
    total_tasks = len(tasks)
    total_users = len(users_names)
    users_with_tasks = []
    overdue_tasks = compare_users_date()

    with open('user_overview.txt', 'w', encoding='utf-8') as write_user_overview:
        write_user_overview.write(f"The total number of users: {total_users}\n"
            f"The total number of tasks: {total_tasks}\n")

        for user in users_names:
            write_user_overview.write(f"User: {user}\n")
            total_tasks_for_user = []
            total_completed_tasks_for_user = []
            total_uncompleted_tasks_for_user = []

            for task in tasks:
                task = task.split(", ")
                if task[0] == user:
                    total_tasks_for_user.append(task)
                    users_with_tasks.append(user)
                    if task[-1] == "Yes":
                        total_completed_tasks_for_user.append(task)
                    elif task[-1] == "No":
                        total_uncompleted_tasks_for_user.append(task)
                        
            # Checks if the user exists in the overdue tasks      
            if user in overdue_tasks:
                users_overdue_tasks = overdue_tasks[user]

            percentage_assigned_to_user = round((len(total_tasks_for_user)/total_tasks) * 100, 2)

            # If the user has overdue tasks, the percentages are calculated
            if len(total_tasks_for_user) != 0:
                percentage_task_completed = round((len(total_completed_tasks_for_user)/len(total_tasks_for_user)) * 100, 2)
                percentage_task_uncompleted = round((len(total_uncompleted_tasks_for_user)/len(total_tasks_for_user)) * 100, 2)
                percentage_overdue_uncompleted = round((users_overdue_tasks/len(total_tasks_for_user)) * 100, 2)

            # if the user does not have overdue tasks totals are set to 0    
            elif len(total_tasks_for_user) == 0:
                percentage_task_completed = 0
                percentage_task_uncompleted = 0
                percentage_overdue_uncompleted = 0

            write_user_overview.write("The total number of tasks assigned to "
                f"{user}: {len(total_tasks_for_user)}\nThe percentage of tasks"
                f" assigned to {user}: {percentage_assigned_to_user}%\nThe "
                f"percentage of tasks assigned to {user} that has been completed: "
                f"{percentage_task_completed}%\nThe percentage of tasks assigned"
                f" to {user} that must still be completed: {percentage_task_uncompleted}%\n"
                f"The percentage of tasks assigned to {user} that not yet been"
                f" completed and are overdue: {percentage_overdue_uncompleted}%\n")

    print("Users overview has been generated in 'user_overview.txt'.\n")
       
# Defining a function to read the task overview file
def read_task_overview():
    with open('task_overview.txt', 'r', encoding='utf-8') as read_task_overview:
        print("Tasks statistics.")
        print()
        for line in read_task_overview:
            line = line.strip("\n")
            line = line.split(": ")
            print(line[0] + ":" + "\t" + line[1])
        print("")

# Defining a function to read the user statistics
def read_user_overview():
    with open('user_overview.txt', 'r', encoding='utf-8') as read_user_overview:
        print("User statistics.")
        print()
        check_str = "overdue"
        for line in read_user_overview:
            line = line.strip("\n")
            line = line.split(": ")
            print(line[0] + ":" + "\t" + line[1])
            
            if line[0] == "The total number of tasks":
                print("")

            elif line[0][-7:] == check_str:
                print("")
        print("")

# Reads the task file
with open('tasks.txt', 'r', encoding='utf-8') as read_tasks:
    for task in read_tasks:
        task = task.strip("\n")
        tasks.append(task)

# reads the user file and creates a user and password list
with open('user.txt', 'r', encoding='utf-8') as read_user:
    for user in read_user:
        user = user.replace(",", "")
        user = user.strip("\n")
        user = user.split(" ")
        users_names.append(user[0])
        users_password.append(user[-1])

# Sets logged in status to false
logged_in = False

# While loop to continue if the logged in stays false
while not logged_in:
    
    print("Welcome to your task manager")
    print()

    # Requests login detials from user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Checks if the log username exist in the username list
    while username not in users_names:
        username = input("Invalid username entered, please try again: ")

    # assigns the username to the user index
    user_index = users_names.index(username)

    print("")

    # Executes if the username exists and sets logged in to True
    if (username == users_names[user_index]) and (password ==
        users_password[user_index]):
        logged_in = True
        print("Successfully logged in")
        print()

    # Checks f either username or passwords are entered correctly
    elif (username == users_names[user_index]) and (password !=
            users_password[user_index]):
        print("User not logged in, Correct username entered with incorrect "
                "password.")

    elif (username not in users_names) and (password in users_password):
        print("User not logged in, Incorrect username entered with correct "
                "password.")

    elif (username not in users_names) and (password not in users_password):
        print("User not logged in, Incorrect username entered with incorrect "
                "password.")

# Executes when logged in changes to True
while logged_in:

    # Check if the user logged in s admin to display the appropriate menu 
    if username == "admin":
        user_selection = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate report
ds - Display statistics
e - Exit
: ''').lower()

# This menu is displayed if the user is not admin
    else:
        user_selection = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    # Calls the function to add new user if r is selected
    if user_selection == "r":
        reg_user(username, users_names)

    # Calls the function to add new task if a
    elif user_selection == "a":
        add_task()
    # Calls the function to view all tasks if va is selected
    elif user_selection == "va":
        view_all()

    # Calls the function to view my task if vm is selected
    elif user_selection == "vm":
        view_mine()
    # Calls the functon to view the overview if ov is selected
    elif user_selection == "gr":

        generate_task_overview()
        user_overview()

    elif user_selection == "ds":

        generate_task_overview()
        user_overview()
        read_task_overview()
        read_user_overview()


    # This ends the program if the user has selected 'e'
    elif user_selection == "e":
        

        print('Goodbye!!!')

        # closes the program
        exit()

        
    # if incorrect option is selected
    else:
        print("Something was entered that isn't on the list, Please try to "
                "enter your selection again.")


