class Calc:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.history = []

    def get_input(self):
        while True:
            try:
                self.value1 = float(input("Enter First Number: "))
                self.value2 = float(input("Enter Second Number: "))
                break
            except ValueError:
                print("Please enter valid numbers")

    def add(self):
        return self.value1 + self.value2

    def sub(self):
        return self.value1 - self.value2

    def mul(self):
        return self.value1 * self.value2

    def div(self):
        try:
            return self.value1 / self.value2
        except ZeroDivisionError:
            return "Can't divide by 0"

    def show_history(self):
        print("Calculation History:")
        if not self.history:
            print("No calculations yet.")
        else:
            for record in self.history:
                print(record)


# Main Loop
cal = Calc()

operations = {
    'add': cal.add,
    'sub': cal.sub,
    'mul': cal.mul,
    'div': cal.div
}

while True:
    print("\nSelect an operation:")
    print("Type 'add' for Addition")
    print("Type 'sub' for Subtraction")
    print("Type 'mul' for Multiplication")
    print("Type 'div' for Division")
    print("Type 'history' to view past results")
    print("Type 'exit' to quit")

    op = input("Enter your choice: ").lower()

    if op in operations:
        cal.get_input()
        result = operations[op]()
        print(f"Result = {result}")
        cal.history.append(f"{cal.value1} {op} {cal.value2} = {result}")

    elif op == 'history':
        cal.show_history()

    elif op == 'exit':
        print("Exiting the calculator. Thank you!")
        break

    else:
        print("Invalid operation. Please try again.")
