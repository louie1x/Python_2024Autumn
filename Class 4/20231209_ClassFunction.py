class Car:
    def __init__(self, color):
        self.color = color
        self.next = None

#Traverse the linked list
def traverse(head):
    ptr = head
    while True:
        print("The color of the car is {}.".format(ptr.color))
        if ptr.next == head:
            break
        ptr = ptr.next
    print("Finish traverse!")
        
#Initiate the first element of single linked link
head = Car("red") #Add new element
ptr = head #Set the position of the pointer
ptr.next = None #There is no next element now

#Add next element into linked list
new_data = Car("blue") #Add the next element
ptr.next = new_data #Set the position of the pointer
new_data.next = head #Point to the head for circular architechture
ptr = new_data #The position of the pointer sohuld be the postition of the new element

new = Car("black") #Add the new element
new.next = head #The new firsdt element points to the origianl head element

#Find the element (ptr) which points to the original head element and turns to point to new element
ptr = head
while ptr.next != head:
    ptr = ptr.next
ptr.next = new

head = new

new = Car("pink") #Add the new element

#Find the element (ptr) which your want the new node to insert after
ptr = head
while ptr.color != "red":
    ptr = ptr.next

#Insert new node into the linked list
new.next = ptr.next
ptr.next = new

traverse(head)