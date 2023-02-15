# This is my Capstone III project - improving on Capstone II by using dictionaries, functions and string manipulation
# =====importing libraries===========
import datetime

# =========defining functions to be called in programme============


# defines function - gets existing usernames from user.txt and returns a dictionary
def dictionary():
    # establishes empty dictionary
    username_dict = {}
    file = open("user.txt", "r")
    for line in file:
        # splits key and value at the ',' and then writes to dictionary
        f = line.split(",")
        username_dict.update({f[0].strip(): f[1].strip()})
    file.close()
    return username_dict


# defines function for main menu with two options for display taking username as argument
def main_menu(username):
    # menu if username is 'admin' (enables additional options to register a user and get stats about task)
    if username == 'admin':
        option = input('''\nPlease select one of the following options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        vs - View stats
        gr - Generate reports
        e - Exit
        ''').lower()
        menuchoice(option, username)

    # menu if username is not 'admin'
    elif username != 'admin':
        option = input('''\nPlease select one of the following options below:
        a - Adding a task
        va - View all tasks
        vm - View my task
        e - Exit
        ''').lower()
        menuchoice(option, username)


# defines function - registering a new user
def reg_user():
    f = open('user.txt', 'a')
    new_username = str(input("Please enter the username you would like to use: "))
    # calls dictionary() function and checks if username matches keys in dictionary (i.e. is taken)
    while new_username in dictionary():
        print("This username is taken. Please choose another one: ")
        new_username = str(input("Please enter the username you would like to use: "))

    # once a new username is input then moves to next stage - asks for password twice and checks they are same
    password = str(input("Please enter the password you would like to use: "))
    password_confirm = str(input("Please confirm your password: "))
    while password != password_confirm:
        print("The two passwords do not match. Please try again.")
        password = str(input("Please enter the password you would like to use: "))
        password_confirm = str(input("Please confirm your password: "))
    f.write(f"\n{new_username}, {password}")
    f.close()
    print("\nYou have successfully added a new user. Now return to the main menu")
    main_menu(username)


# defines function - add task
def add_task():
    f = open('tasks.txt', 'a+')
    user = str(input("To whom would you like this task to be assigned? "))
    task = str(input("What is the title of this task? "))
    description_task = str(input("Please provide a description of this task: "))
    current_date_formatted = datetime.datetime.today().strftime('%d %b %Y')  # format the date to dd words yyyy
    # ensures date format is consistent using while loop and try/except
    while True:
        try:
            due_date = input("What is the due date for this task (in the following format - 10 Apr 2023)? ")
            datetime.datetime.strptime(due_date, '%d %b %Y')
            break
        except ValueError:
            print("Sorry, that is in the incorrect format. Try again!")
            continue
    # Use the write method to append the contents of the variables name to the text file, which is
    # represented by the object f
    due_date_formatted = datetime.datetime.today().strftime('%d %b %Y')
    f.write(f"{user}, {task}, {description_task}, {current_date_formatted}, {due_date_formatted}, No\n")
    f.close()
    print("\nYou have successfully added a new task. Now return to the main menu")
    main_menu(username)


# defines function - view all
def view_all():
    f = open('tasks.txt', 'r')
    # iterates through lines of file
    for line in f:
        #  splits each line into list
        split_tasks = line.split(", ")
        # separates out all info in list by index position
        assigned_to = split_tasks[0]
        task = split_tasks[1]
        task_desc = split_tasks[2]
        date_assigned = split_tasks[3]
        due_date = split_tasks[4]
        completed = split_tasks[5]

        print(f"""
            Task:\t\t\t\t\t{task}
            Assigned to:\t\t\t{assigned_to}
            Task description:\t\t{task_desc}
            Date assigned:\t\t\t{date_assigned}
            Due date:\t\t\t\t{due_date}
            Completed:\t\t\t\t{completed}""")
    f.close()
    print("\nHere are all the tasks. Now return to the main menu")
    main_menu(username)


# defines function - view mine
def view_mine():
    f = open('tasks.txt', 'r')

    user_database = 0
    data = f.readlines()

    for pos, line in enumerate(data, 1):
        split_tasks = line.strip("\n").split(", ")
        assigned_to = split_tasks[0]
        task = split_tasks[1]
        task_desc = split_tasks[2]
        date_assigned = split_tasks[3]
        due_date = split_tasks[4]
        completed = split_tasks[5]

        if assigned_to == username:
            print(f"""
            ***************************[{pos}]***************************
            Task:\t\t\t\t\t{task}
            Assigned to:\t\t\t{assigned_to}
            Task description:\t\t{task_desc}
            Date assigned:\t\t\t{date_assigned}
            Due date:\t\t\t\t{due_date}
            Completed:\t\t\t\t{completed}
            """)
            user_database += 1

    if user_database == 0:
        print("You do not have any tasks assigned to you. Return to the main menu")
        main_menu(username)


    # while loop for conditions of editing tasks
    while True:
        # asks for number of task to review and subtracts 1 to align with positions
        task_choice = int(input("\nPlease select which task you would like to review, or '-1' to return to the main "
                                "menu: ")) - 1
        # establishes new variable called edit_data which uses task_choice as index
        edit_data = data[task_choice]
        split_tasks = edit_data.strip("\n").split(", ")

        # if user inputs -1 (-1-1 = -2)
        if task_choice == -2:
            main_menu(username)

        elif task_choice < -2 or task_choice == -1:
            print("You have selected an invalid option. Please try again")
            continue

        # only allows you to amend your own task
        elif split_tasks[0] != username:
            print("You cannot edit someone else's task. Please try again")
            continue

        # does not allow you to edit completed tasks
        elif split_tasks[-1] == "Yes":
            print("This task has been completed and you cannot edit it. Please select another option")
            continue

        # breaks loop and moves into next section of code - editing tasks if none of conditions above met
        break

    while True:
        # asks user what they want to do to the task
        to_do_choice = int(input(f"""_________________________________[SELECT AN OPTION]_________________________________\n 
        1 - Edit the task \n 
        2 - Mark as completed \n """))

        # check for errors in input
        if to_do_choice <= 0 or to_do_choice >= 3:
            print("You have selected an invalid option, please try again.")
            continue

        elif to_do_choice == 1:
            which_choice = int(input(f"""_________________________________[SELECT AN OPTION]_________________________________\n
            1 - Change the name of the user to whom this task is assigned \n
            2 - Change the due date of the task \n
            """))
            if which_choice == 1:
                split_tasks = edit_data.split(", ")
                split_tasks[0] = input("To whom do you want to reassign this task? ")
                new_data = ", ".join(split_tasks)
                data[task_choice] = new_data

            elif which_choice == 2:
                split_tasks = edit_data.split(", ")
                # ensures date format is consistent using while loop and try/except

                while True:
                    try:
                        due_date = input("What is the due date for this task (in the following format - 10 Apr 2023)? ")
                        datetime.datetime.strptime(due_date, '%d %b %Y')
                        break
                    except ValueError:
                        print("Sorry, that is in the incorrect format. Try again!")
                        continue
                split_tasks[4] = due_date
                new_data = ", ".join(split_tasks)
                data[task_choice] = new_data

            tasks_write = open('tasks.txt', 'w')
            for line in data:
                tasks_write.write(line)
            tasks_write.close()
            print("\nYou have successfully modified this task. Now return to the main menu")
            main_menu(username)
            break

        elif to_do_choice == 2:
            split_tasks = edit_data.split(", ")
            split_tasks[-1] = "Yes\n"
            new_data = ", ".join(split_tasks)
            data[task_choice] = new_data

        tasks_write = open('tasks.txt', 'w')
        for line in data:
            tasks_write.write(line)
        tasks_write.close()
        print("\nYou have successfully modified this task. Now return to the main menu")
        main_menu(username)
        break


# defines function - generate report
def gen_report():
    f = open('tasks.txt', 'r')
    # establishes counters
    num_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    over_due = 0

    # info for report 1
    # iterates through lines of file to count tasks and separates out info in list by index
    # to calculate completed/uncompleted
    for line in f:
        num_tasks += 1

        #  splits each line into list
        split_tasks = line.strip("\n").split(", ")

        if split_tasks[-1] == "Yes":
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            # for the uncompleted tasks also check due date against current date
            current_date = datetime.datetime.today()
            # converts string data type to data object to compare with current date which is object
            due_date = split_tasks[-2]
            date_obj = datetime.datetime.strptime(due_date, '%d %b %Y')
            if date_obj < current_date:
                over_due += 1
        percentage_incomplete = round(((uncompleted_tasks / num_tasks) * 100), 2)
        percentage_overdue = round(((over_due / num_tasks) * 100), 2)

    ofile = open('task_overview.txt', 'w')
    ofile.write(
    f"""Here is your report giving you an overview of the tasks generated and tracked by this project:\n
            Total number of tasks in the project:\t\t\t\t\t\t\t{num_tasks}
            Total number of completed tasks:\t\t\t\t\t\t\t\t{completed_tasks}
            Total number of uncompleted tasks:\t\t\t\t\t\t\t\t{uncompleted_tasks}
            Total number of tasks not completed that are also overdue:\t\t{over_due}
            Percentage of tasks that are incomplete:\t\t\t\t\t\t{percentage_incomplete}%
            Percentage of tasks that are overdue:\t\t\t\t\t\t\t{percentage_overdue}%""")

    f.close()
    ofile.close()

    # generates second report on users
    num_users = 0
    user_file = open('user.txt', 'r')
    for line in user_file:
        num_users += 1

    file = open('user_overview.txt', 'w+')
    file.write(f"""Here is your report giving you an overview of the users and their tasks:\n
        There are {num_users} users registered with this project.
        There are {num_tasks} tasks in total as part of this project.\n""")

    task_file = open('tasks.txt', 'r')
    task_details = task_file.readlines()

    for usernames in dictionary():
        num_users += 1
        user_task = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        over_due = 0
        for lines in task_details:
            split_lines = lines.strip("\n").split(", ")
            if split_lines[0] == usernames:
                user_task += 1
                if split_lines[5] == "Yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                    # for uncompleted tasks also check due date against current date
                    current_date = datetime.datetime.today()
                    # converts string data type to data object to compare with current date which is object
                    due_date = split_lines[-2]
                    date_obj = datetime.datetime.strptime(due_date, '%d %b %Y')
                    if date_obj < current_date:
                        over_due += 1

        # performs calculations for the user report, including catching and handling
        # ZeroDivisionError if user has no tasks assigned to them
        task_list = [usernames, user_task, completed_tasks, uncompleted_tasks, over_due]
        all_tasks_perc = round((task_list[1] / num_tasks * 100), 2)
        try:
            user_perc_complete = round(((task_list[2] / task_list[1]) * 100), 2)
        except ZeroDivisionError:
            user_perc_complete = 0
        try:
            user_perc_incomplete = round(((task_list[3] / task_list[1]) * 100), 2)
        except ZeroDivisionError:
            user_perc_incomplete = 0
        try:
            overdue_perc = round(((task_list[4] / task_list[1]) * 100), 2)
        except ZeroDivisionError:
            overdue_perc = 0

        file.write(f"""
        For user {task_list[0]}:
        They have {task_list[1]} tasks assigned to them.
        Their tasks represent {all_tasks_perc}% of all tasks.
        {user_perc_complete}% have been completed.
        {user_perc_incomplete}% still need to be completed.
        {overdue_perc}% of their tasks are not completed and are overdue.\n""")

    task_file.close()
    user_file.close()
    file.close()


# defines function for view stats
def view_stats():

    print("""This displays a report about tasks and users in the IDE console, using text report files generated.
    It also generates report files 'task_overview.txt' and 'user_overview.txt' if these do not already exist\n""")

    # opens task overview file and enables reading, if file not created yet generates these by calling gen_report funct
    gen_report()
    file_task = open('task_overview.txt', 'r+')

    for line in file_task:
        # splits each line into a list
        content = line.split(", ")
        tasks = content[0]
        tasks.strip()
        print(tasks)
    print("\n")

    file_user = open('user_overview.txt', 'r+')
    for line in file_user:
        # splits each line into a list
        content = line.split(", ")
        users = content[0]
        users.strip()
        print(users)

    file_task.close()
    file_user.close()
    print("\nNow return to the main menu")
    main_menu(username)


# defines function for menuchoice taking option as an argument and returning the relevant function
def menuchoice(option, username):
    if option == "r" and username == "admin":
        return reg_user()
    elif option == "a":
        return add_task()
    elif option == "va":
        return view_all()
    elif option == "vm":
        return view_mine()
    elif option == "vs" and username == "admin":
        return view_stats()
    elif option == "gr" and username == "admin":
        print("Your reports are ready for you!")
        return gen_report()
    # additional check if username not 'admin' - these option won't display on non-admin menu
    # but if user were to input these letters then they will be returned to main menu
    elif option == "vs" or option == "gr" or option == "r" and username != "admin":
        print("You are not authorised to perform this action.")
        return main_menu(username)
    elif option == 'e':
        print('Goodbye!!!')
        exit()
    # for any other non valid option, will return user to main menu
    else:
        print("This option is not available. Please try again!")
        main_menu(username)


# ====Login Section====

# asks user for username and password and validates by calling the dictionary function
username = input("Please input your username: ")
# sets up while loop to validate username against dictionary
while username not in (dictionary()):
    print("You have entered an invalid username.")
    username = input("Please input your username: ")

# sets up while loop to validate password against username in dictionary
password = input("Please input your password: ")

correct_pass = dictionary().get(username)

while password != correct_pass:
    print("This is not the correct password. Please try again.")
    password = input("Please input your password: ")

# ==== once username and password validated, continues to run programme and call main_menu function====
main_menu(username)
