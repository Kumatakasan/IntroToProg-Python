# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# GKumataka, 08.07.2021 started work on loading data
# GKumataka, 08.08.2021 Finished all options and commented code
# GKumataka, 08.09.2021 Changed how I imported original file
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
# Removed some variables I didn't use or defined later
strFile = "TodoList.txt"  # Document of data storage
strData = ""  # A row of text data from the file
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
dicRow = {}

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, 'r')  # Opening file as readable

for line in objFile:  # Reading in current items in ToDoList.txt and appending to lstTable
    lstrow = line.strip().split(',')
    dicRow = {'Task': lstrow[0], 'Priority': lstrow[1].strip()}
    lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """

    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    # Reading in file items and printing
    if (strChoice.strip() == '1'):
        for row in lstTable:  # Printing current items in list
            print(row['Task'], ' | ', row['Priority'])

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Please enter the task: ")  # Asks user for task
        strPriority = input("Please enter a priority for the task: ")  # Asks user for priority level
        dicRow = {'Task': strTask, 'Priority': strPriority}  # Creates a dictionary
        lstTable.append(dicRow)  # Appends to lstTable
        print("The task, " + strTask + ", was added to the list with a priority of " + strPriority + ".")
        #print(lstTable)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        count = 0

        print('The current tasks you can delete are:')
        for row in lstTable:  #Printing current tasks to show what can be deleted
            print(row['Task'])
        print()
        rmTask = input("Please enter the task you wish to remove: ")

        # Searching list for task.  If found it removes task, this loops until found or end of list
        for row in lstTable:
            if row['Task'].lower() == rmTask.lower():
                lstTable.remove(row)
                print("The task has been deleted.")
                count = count + 1
            else:
                continue

        # If no task was found in current list, outputs task was not found
        # A bit redundant with showing the items in the list, but lets user know input was incorrect
        if count == 0:
            print('The task entered was incorrect.  Back to Main Menu')
            continue


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # Opening file and saving lstTable from memory.  File is overridden(using 'w')
        with open(strFile, "w") as writer:
            for row in lstTable:
                writer.write(row['Task'] + ', ' + row['Priority'] + '\n')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # Adding and exit statement
        print("Exiting your To-Do list!")
        break  # and Exit the program
