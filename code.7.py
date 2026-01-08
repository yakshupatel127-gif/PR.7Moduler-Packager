# ===== IMPORTING BUILT-IN MODULES =====
import datetime
import time
import math
import random
import uuid
import string


# ===== DATETIME & TIME OPERATIONS =====
def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Date and Time:", datetime.datetime.now())

        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            print("Difference:", abs((date2 - date1).days), "days")

        elif choice == "3":
            print("Formatted Date:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == "4":
            input("Press Enter to start stopwatch")
            start = time.time()
            input("Press Enter to stop")
            print("Elapsed Time:", round(time.time() - start, 2), "seconds")

        elif choice == "5":
            sec = int(input("Enter seconds: "))
            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1
            print("Time's up!")

        elif choice == "6":
            break
        else:
            print("Invalid choice!")


# ===== MATHEMATICAL OPERATIONS =====
def mathematical_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Functions")
        print("4. Area of Circle")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial:", math.factorial(n))

        elif choice == "2":
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (%): "))
            t = float(input("Enter time (years): "))
            ci = p * (1 + r / 100) ** t
            print("Compound Interest:", round(ci, 2))

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("Sin:", math.sin(rad))
            print("Cos:", math.cos(rad))
            print("Tan:", math.tan(rad))

        elif choice == "4":
            r = float(input("Enter radius: "))
            print("Area of Circle:", round(math.pi * r * r, 2))

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


# ===== RANDOM DATA GENERATION =====
def random_operations():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Generate Random Password")
        print("4. Generate OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            lst = [random.randint(1, 50) for _ in range(5)]
            print("Random List:", lst)

        elif choice == "3":
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(chars) for _ in range(length))
            print("Generated Password:", password)

        elif choice == "4":
            print("Generated OTP:", random.randint(100000, 999999))

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


# ===== UUID GENERATION =====
def uuid_operation():
    print("\nGenerated UUID:", uuid.uuid4())


# ===== FILE OPERATIONS (CUSTOM LOGIC) =====
def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            filename = input("Enter file name: ")

        if choice == "1":
            open(filename, "w").close()
            print("File created successfully!")

        elif choice == "2":
            data = input("Enter data to write: ")
            with open(filename, "w") as f:
                f.write(data)
            print("Data written successfully!")

        elif choice == "3":
            with open(filename, "r") as f:
                print("File Content:\n", f.read())

        elif choice == "4":
            data = input("Enter data to append: ")
            with open(filename, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully!")

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


# ===== MODULE EXPLORATION USING dir() =====
def explore_module():
    module_name = input("Enter module name to explore: ")
    try:
        module = __import__(module_name)
        print("Available Attributes:\n", dir(module))
    except ImportError:
        print("Module not found!")


# ===== MAIN MENU =====
def main():
    while True:
        print("\n" + "=" * 35)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 35)
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()
        elif choice == "2":
            mathematical_operations()
        elif choice == "3":
            random_operations()
        elif choice == "4":
            uuid_operation()
        elif choice == "5":
            file_operations()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice! Try again.")


# ===== PROGRAM EXECUTION =====
if __name__ == "__main__":
    main()