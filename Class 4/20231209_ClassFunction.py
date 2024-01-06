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

traverse(ptr)