def main():
    while True:
        # Ask for student's name
        name = input("\nEnter student's name (or type 'Exit' to quit): ")

        # Check for exit condition
        if name.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        # Ask for 3 subject marks
        try:
            mark1 = float(input("Enter marks for subject 1: "))
            mark2 = float(input("Enter marks for subject 2: "))
            mark3 = float(input("Enter marks for subject 3: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for marks.")
            continue

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        # Determine Grade
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Print clean formatted output
        print("-" * 30)
        print(f"Name    : {name}")
        print(f"Average : {average:.1f}")
        print(f"Grade   : {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()
