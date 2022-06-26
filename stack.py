import sys

class Stack:
    def __init__(self):
        self.__s = []
        self.__top = -1

    def isEmpty(self):
        if(self.__top == -1):
            return True
        else:
            return False

    def top(self):
        if(self.isEmpty()==True):
            print("Empty stack")
        else:
            print("The top element is : ", self.__s[self.__top])
    def push(self, element):
        self.__s.append(element)
        self.__top = self.__top + 1
    
    def Pop(self):
        self.__s.pop()
        self.__top = self.__top - 1
    def print_stack(self):
        print("Stack: ", self.__s[::-1])


stack = Stack()
while(True):
    print("Enter the operation you want to perform")
    print("1. Push");print("2. Pop");print("3. Print Stack");print("4. Exit")
    ch = int(input())
    if ch==1:
        ele = int(input("Enter the element : "))
        stack.push(ele)
    elif ch ==2:
        stack.Pop()
    elif ch == 3:
        stack.print_stack()
    else:
        sys.exit()

