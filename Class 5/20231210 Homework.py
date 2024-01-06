## Homework 3.1
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

first = Employee("Amy", 25)
first.next = None

ptr = first
while ptr.next != None:
    ptr = ptr.next


second = Employee('Eddy', 43)
ptr.next = second
second.next = None

ptr = first
while ptr.next != None:
    ptr = ptr.next

third = Employee('Esme', 32)
ptr.next = third
third.next = None


def traverse(head):
    ptr = head
    while ptr != None:
        print('The employee name is {} and the age is {}.'.format(ptr.name, ptr.age))
        ptr = ptr.next

    print('Finish traverse!')

traverse(first)