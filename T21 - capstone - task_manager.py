# =====importing libraries===========
import datetime

# ====Login Section====
# reads usernames and passwords from user.txt file
user_file = open('user.txt', 'r')

# sets up empty lists for username and password to store from the file

username_list = []
password_list = []

# populates the empty lists (username and password) with data from the user_file
for line in user_file:
    user, password = line.strip("\n").split(", ")
    username_list.append(user)
    password_list.append(password)

# asks user to input username
username = input("Please input your username: ")
# sets up while loop to validate username against username_list
while username not in username_list:
    print("You have entered an invalid username.")
    username = input("Please input your username: ")

# sets up while loop to validate password against password_list
password = input("Please input your password: ")
while password not in password_list:
    print("This is not the correct password. Please try again.")
    password = input("Please input your password: ")

# closes user_file as first part of programme complete
user_file.close()

# once username and password validated, continues to run programme

# menu if username is 'admin' (enables options to register a user and get stats about task)
if username == 'admin':
    # ensures user input converted to lower case
    menu_choice = input('''\nPlease select one of the following options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    s - View stats
    e - Exit
    ''').lower()

# menu if username is not 'admin'
elif username != 'admin':
    # ensures user input converted to lower case
    menu_choice = input('''\nPlease select one of the following options below:
    a - Adding a task
    va - View all tasks
    vm - View my task
    e - Exit
    ''').lower()

# enables 'admin' user to add a new username and password to the user.txt file
if menu_choice == 'r' and username == "admin":
    # opens user.txt file and enables contents to be appended
    f = open('user.txt', 'a+')
    # Asks user for new username. When they enter it, it is stored as string in variable 'username'
    username1 = str(input("Please enter the username you would like to use: "))
    # Asks user for new password. When they enter it, it is stored as string in variable 'password'
    password = str(input("Please enter the password you would like to use: "))
    # Ask user to confirm password and verify the new password and confirmed password are the same
    password_confirm = str(input("Please confirm your password: "))
    # sets up while loop to validate password_confirm against password
    while password != password_confirm:
        print("The two passwords do not match. Please try again.")
        password = str(input("Please enter the password you would like to use: "))
        password_confirm = str(input("Please confirm your password: "))

    # Use the write method to append the contents of the variables name to the text file
    # which is represented by the object f.
    f.write(f"\n{username1}, {password}")
    f.close()

# additional check that username must be 'admin', in case someone inputs 'r' against second menu when not admin
elif menu_choice == 'r' and username != "admin":
    print("You are not authorised to perform this action.")

elif menu_choice == 'a':
    # opens tasks.txt file and enables contents to be appended
    f = open('tasks.txt', 'a+')
    # Asks user to input new information as variables, which will then be stored in tasks.txt file
    user = str(input("To whom would you like this task to be assigned? "))
    task = str(input("What is the title of this task? "))
    description_task = str(input("Please provide a description of this task: "))
    current_date = datetime.datetime.today()
    current_date_formatted = datetime.datetime.today().strftime('%d %b %Y')  # format the date to dd words yyyy
    due_date = input("What is the due date for this task (in xx month year) ")

    # Use the write method to append the contents of the variables name to the text file, which is
    # represented by the object f
    f.write(f"\n{user}, {task}, {description_task}, {current_date_formatted}, {due_date}, No")
    f.close()

elif menu_choice == 'va':
    # opens txt file and enables reading
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
        Completed:\t\t\t\t{completed}
        """)

    # closes file
    f.close()

elif menu_choice == 'vm':

    # opens txt file and enables reading
    f = open('tasks.txt', 'r')

    user_database = 0
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

        if assigned_to == username:
            print(f"""
            Task:\t\t\t\t\t{task}
            Assigned to:\t\t\t{assigned_to}
            Task description:\t\t{task_desc}
            Date assigned:\t\t\t{date_assigned}
            Due date:\t\t\t\t{due_date}
            Completed:\t\t\t\t{completed}
            """)
            user_database += 1

    if user_database == 0:
        print("You do not have any tasks assigned to you.")

    # closes file
    f.close()

elif menu_choice == 's' and username == 'admin':
    # opens tasks file and enables reading
    f = open('tasks.txt', 'r')

    count_task = 0
    # iterates through lines of file
    for line in f:
        #  counts each line
        count_task += 1
    print(f"There are {count_task} tasks in your tasks file.")

    f.close()

    # opens user file and enables reading
    f = open('user.txt', 'r')

    count_user = 0
    # iterates through lines of file
    for line in f:
        #  counts each line
        count_user += 1
    print(f"There are {count_user} users in your user file.")

    f.close()

# additional check that username must be 'admin', in case someone inputs 's' against second menu when not admin
elif menu_choice == 's' and username != 'admin':
    print("You are not authorised to perform this action.")

elif menu_choice == 'e':
    print('Goodbye!!!')
    exit()

else:
    print("This option is not available. Please try again!")
