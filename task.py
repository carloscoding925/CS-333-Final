# Carlos Hernandez
# CS 333, Erin Keith
class Task:
    def __init__(self):
        self.desc = "Sample Description"
        self.date = "01/01/0001"
        self.complete = False

    def changeDate(self, userDate):
        self.date = userDate

    def changeDescription(self, userDesc):
        self.desc = userDesc

    def setComplete(self, userBool):
        self.complete = userBool
    
    def setTask(self, userDate, userDesc, userBool):
        self.date = userDate
        self.desc = userDesc
        self.complete = userBool

    def printTask(self):
        print(f"Date: {self.date}")
        print(f"Description: {self.desc}")
        if(not self.complete):
            print("Complete: No")
        else:
            print("Complete: Yes")

        return True

    def returnDesc(self):
        return self.desc
    
    def returnDate(self):
        return self.date
    
    def returnComplete(self):
        return self.complete