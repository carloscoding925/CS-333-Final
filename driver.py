# Carlos Hernandez
# CS 333, Erin Keith
 
from todoList import ToDoList
from task import Task

def main():
    myToDoList = ToDoList()

    userChoice = "1"

    while(userChoice != "0"):
        print("Welcome! ")
        print("Select an option:")
        print("1. Add Tasks")
        print("2. Display Tasks")
        print("3. Modify Tasks")
        print("0. Exit\n")
        userChoice = input()

        if(userChoice == "1"):
            userTask = Task()

            print("Please enter a date in format MM/DD/YYYY:")
            inputDate = input()

            print("Please enter a description: ")
            inputDesc = input()
            inputComplete = False
            print("\n")

            userTask.setTask(inputDate, inputDesc, inputComplete)
            myToDoList.addTask(userTask)
        elif(userChoice == "2"):
            myToDoList.printAllTasks()
        elif(userChoice == "3"):
            print("Which task would you like to modify?")
            userOption = input()

            myToDoList.modifyTask(userOption)
        elif(userChoice == "0"):
            print("\n")
        else:
            print("Choose a valid option:\n")

if __name__ == "__main__":
    main()