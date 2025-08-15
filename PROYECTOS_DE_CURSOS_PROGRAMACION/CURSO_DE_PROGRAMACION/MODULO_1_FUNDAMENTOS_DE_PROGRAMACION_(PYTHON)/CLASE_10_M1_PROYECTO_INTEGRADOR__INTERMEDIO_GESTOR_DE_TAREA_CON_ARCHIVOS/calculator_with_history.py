# === calculator with history ===
file_history = "history.txt"

#todo  Returns the sum
def add(a, b):
    return a + b 

#todo # Returns subtraction
def sub(a, b):
    return a - b

#todo Returns multiplication
def mul(a, b):
    return a * b

#! Returns the division. Be careful with division by 0
def div(a, b):
    if b == 0:
        raise ValueError("Not defined")
    return a / b


#todo # Save the operation in history.txt
def save_history(text):
    with open(file_history, "a", encoding="utf-8") as file:
        file.write(text + "\n")
#todo Displays the content of the history
def view_history():
    try:
        with open(file_history, "r", encoding="utf-8") as file:
            content = file.read()
        if content:
            print("\nHISTORY")
            print("\ncontent")
        else:
            print("History is empty")
    except FileNotFoundError:
        print("The history file is not found")

#todo Clears all history content
def clear_history():
    with open(file_history, "w", encoding="utf-8") as file:
        file.write(" ")
        pass
    print("History has been cleared")

#? Main loop with menu
if __name__ == "__main__":
    while True:
        print("""
    === Calculator with History ===
    [1] Add
    [2] Subtract
    [3] Multiply
    [4] Divide
    [5] View history
    [6] Clear history
    [0] Exit
    """)
        option = input("select one option ")

        if option == "1":
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = add(a, b)
                print(f"\nThe result is: {result}")
                save_history(f"{a} + {b} = {result}")
            except ValueError:
                print("Enter two valid numbers!")

        elif option == "2": 
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = sub(a, b)
                print(f"\nThe result is: {result}")
                save_history(f"{a} - {b} = {result}")
            except ValueError:
                print("Enter two valid numbers!")
        
        elif option == "3":
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = mul(a, b)
                print(f"\nThe result is: {result}")
                save_history(f"{a} * {b} = {result}")
            except ValueError:
                print("Enter two valid numbers!")

        elif option == "4": 
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = div(a, b)
                print(f"\nThe result is: {result}")
                save_history(f"{a} / {b} = {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif option == "5":
            view_history()
        elif option == "6":
            clear_history()
        elif option == "0":
            break
        else:
            print("Invalid option")
print("Thank you for using the program")