class Stack:
    def __init__(self):
        # Each stack instance gets its own internal list
        self.data: list[int] = []

    def __repr__(self) -> str:
        """Readable string representation of the stack."""
        return f"Stack({self.data})"
    
    def push(self, item: int) -> None:
        self.data.append(item)
        
    def pop(self) -> int:
        if self.data == []:
            raiseValueError: "Stack is empty"
        return self.data.pop()
    
    def element_exists(self, val: int) -> bool:
        does_exist = False
        while self.data != []:
            element_popped = self.pop()


def main():
    print("Stacks.")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    s.pop()
    print(s)


if __name__ == "__main__":
    main()