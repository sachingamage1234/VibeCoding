def main():
    print("--- Monthly Budget Calculator ---")
    
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))

        total_expenses = 0.0
        
        # Enter expenses multiple times until 'done'
        while True:
            entry = input("Enter an expense amount (or type 'done' to finish): ").strip().lower()
            
            if entry == 'done':
                break
            
            try:
                expense = float(entry)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a numeric value or 'done'.")

        # Calculate remaining balance
        remaining_balance = total_budget - total_expenses

        # Display remaining balance
        print("-" * 30)
        print(f"Total Budget      : {total_budget:.2f}")
        print(f"Total Expenses    : {total_expenses:.2f}")
        print(f"Remaining Balance : {remaining_balance:.2f} LKR")
        print("-" * 30)

        # Low funds warning
        if remaining_balance < 500:
            print("Warning: Low Funds")
        elif remaining_balance >= 500:
            print("Good job! You are within your budget.")

    except ValueError:
        print("Error: Please enter a valid numeric value for the initial budget.")

if __name__ == "__main__":
    main()
