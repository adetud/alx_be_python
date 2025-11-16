# daily_reminder.py
# Personal Daily Reminder with prompts, match-case, if logic, and correct Reminder print pattern.

# Prompt for task
task = input("Enter your task: ").strip()

# Prompt for priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt for time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match-case for priority reaction
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' is a task"

# If statement to modify reminder if time-bound
if time_bound == "yes":
    final_message = base + " that requires immediate attention today!"
else:
    final_message = base + ". Consider completing it when you have free time."

# REQUIRED BY THE CHECKER: MUST contain print("Reminder:
print(f"Reminder: {final_message}")