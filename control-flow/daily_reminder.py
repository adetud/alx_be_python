# daily_reminder.py
# A simple daily reminder script using match-case, if statements, and loops.

# --- Step 1: Prompt the user for information ---
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# --- Step 2: Process the task using match-case ---
while True:   # loop to ensure we only break after giving a correct reminder
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:  # default if priority is invalid
            print("Invalid priority. Please enter high, medium, or low.")
            priority = input("Priority (high/medium/low): ").strip().lower()
            continue  # repeat the loop until priority is valid

    # --- Step 3: Adjust message if task is time-bound ---
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # We print the final message and break the loop
    print("\nReminder:", message)
    break