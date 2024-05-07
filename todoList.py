# Carlos Hernandez
# CS 333, Erin Keith
from task import Task

class ToDoList:
    
    def __init__(self):
        self.checkList = {}
        self.counter = 0
        self.task = Task()

    def addTask(self, userTask):
        self.checkList[self.counter] = userTask
        self.counter = self.counter + 1

    def removeTask(self, userKey):
        self.checkList.pop(userKey - 1)
        self.counter = self.counter - 1
    
    def printAllTasks(self):
        for x in range(self.counter):
            self.task = self.checkList[x]
            print(f"Task {x + 1}: ")
            self.task.printTask()
            print("")

        return True

    def printSpecificTask(self, userChoice):
        if(userChoice >= self.counter + 1):
            return False
        elif(userChoice < self.counter + 1):
            self.task = self.checkList[userChoice - 1]
            self.task.printTask()
            print("")
            return True

    def modifyTask(self, userTask):
        print("What would you like to modify? \n")
        print("1. Date")
        print("2. Description")
        print("3. Completion Status\n")
        userChoice = input()

        userTask = int(userTask)
        self.task = self.checkList[userTask - 1]

        if userChoice == "1":
            print("Enter a new date:")
            newDate = input()
            self.task.changeDate(newDate)
        elif userChoice == "2":
            print("Enter a new description:")
            newDesc = input()
            self.task.changeDescription(newDesc)
        elif userChoice == "3":
            print("Enter completion status (T/F):")
            newStatus = input()
            if(newStatus == "T"):
                myBool = True
            elif(newStatus == "F"):
                myBool = False
            self.task.setComplete(myBool)

        self.checkList[userTask - 1] = self.task

        return True

    def returnChecklist(self):
        return self.checkList
    
    def returnCounter(self):
        return self.counter
    
    def returnTask(self):
        return self.task