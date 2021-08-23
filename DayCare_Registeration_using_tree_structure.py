import datetime

today = datetime.datetime.now()

class Birthdate:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def printBirthday(self):
        print(str(self.month) +"/"+ str(self.day) +"/"+ str(self.year))

class Child:

    def __init__(self, name, gender, guardian, contact_no, address, month, day, year):
        self.name = name
        self.gender = gender
        self.guardian = guardian
        self.contact_no = contact_no
        self.address = address
        self.birthdate = Birthdate(month, day, year)
        self.age = int(today.strftime("%Y")) - year
        self.left = None
        self.right = None

    def PrintChildInfo(self):
        print("__Child Info__")
        print("Name          : " + str(self.name))
        print("Gender        : " + str(self.gender))
        print("Guardian Name : " + str(self.guardian))
        print("Contact no.   : " + str(self.contact_no))
        print("Address       : " + str(self.address))
        print("Birthdate     : ", end="")
        self.birthdate.printBirthday()
        print("Age           : " + str(self.age))
        print("")

class ChildTree:

    def __init__(self, child = None):
        self.data = child
        self.right = None
        self.left = None

    def insertChild(self,temp): #Insertion of child into tree

        if(self.data):
            if(temp.age < self.data.age ):
                if(self.left == None):
                    self.left = ChildTree(temp)
                else:
                    self.left.insertChild(temp)
            else:
                if(self.right == None):
                    self.right = ChildTree(temp)
                else:
                    self.right.insertChild(temp)
        else:
            self.data = temp

    def displayChild(self): #preorder (ascending order)
        if(self.left):
            self.left.displayChild()
        self.data.PrintChildInfo()
        if(self.right):
            self.right.displayChild()


tree = ChildTree()
x = Child("Ajay", "M", "Seva", "012-13456", "Address", 8, 16, 2013)
tree.insertChild(x)
x = Child("Sarah", "F", "Laura", "017-13456", "Address", 2, 14, 2016)
tree.insertChild(x)
x = Child("Kamal", "M", "Dave", "019-13456", "Address", 4, 4, 2018)
tree.insertChild(x)
x = Child("Michell", "F", "Raja", "014-13456", "Address", 5, 5, 2016)
tree.insertChild(x)

tree.displayChild()
