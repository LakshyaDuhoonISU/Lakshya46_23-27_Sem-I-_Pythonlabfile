#WAP to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def size(self):
        return len(self.items)
    
    def print_stack(self):
        print("Stack:", self.items)

def main():
    my_stack = Stack()

    while True:
        print("\n1)Push element")
        print("2)Pop element")
        print("3)Check size of stack")
        print("4)View Stack")
        print("5)Exit program\n")
        choice = int(input("Enter choice: "))

        while choice<=0 or choice>5:
            print("Invalid choice")
            break

        if choice == 1:
            val = int(input("Enter the value to be pushed into the stack: "))
            my_stack.push(val)
        elif choice == 2:
            popped_element = my_stack.pop()
            print(f"{popped_element} popped from stack")
        elif choice == 3:
            print("Stack size:", my_stack.size())
        elif choice == 4:
            my_stack.print_stack()
        elif choice == 5:
            print("Exiting program")
            exit()

if __name__ == "__main__":
    main()
