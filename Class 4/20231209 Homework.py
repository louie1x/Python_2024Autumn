class Car:
    def __init__(self, color):
        self.color = color
        self.next = None

#Traverse the linked list
def traverse(head):
    ptr = head
    while ptr != None:
        print("The color of the car is {}.".format(ptr.color))
        ptr = ptr.next
    
    print("Finish traverse!")
        
#Initiate the first element of single linked link
head = Car("red")
car1 = Car("blue")
#Add a node to the first position fo link list
car1.next = head
head = car1
#Find th last position object of linked list
ptr = head
while ptr.next != None:
    ptr = ptr.next
#Create new objet cnad add a node to the last position of linked list
newcar = Car("black")
ptr.next = newcar
newcar = None
#Find the position you want to add object
ptr = head
while ptr.color != "red":
    ptr = ptr.next
#Create new object and add a node to the middle of linked list
car2 = Car("pink")
car2.next = ptr.next
ptr.next = car2
#Find the position of the object you want to delete from linked list
ptr = head
while ptr.color != "red":
    ptr = ptr.next
#Delete
delete = ptr.next
ptr.next = delete.next

traverse(head)

#----------------------------------------------------------------------------

class student:
    def __init__(self, name, mathscore):
        self.name = name
        self.mathscore = mathscore
        self.next = None
 
#Traverse the linked list
def traverse(head):
    ptr = head
    while ptr != None:
        print("The student name is {} and the math score is {}.".format(ptr.name, ptr.mathscore))
        ptr = ptr.next
    
    print("Finish traverse!")

student1 = student("Louie", "8")
traverse(student1)