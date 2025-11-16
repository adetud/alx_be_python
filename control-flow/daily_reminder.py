# daily_reminder.py
# Simple personal daily reminder using match-case, if, and loops.
# Prompts: Task, Priority, Is it time-bound?

def prompt_task():
    while True:
        task = input("Enter your task: ").strip()
        if task:
            return task
        print("Please enter a non-empty task description.")

def prompt_priority():
    while True:
        p = input("Priority (high/medium/low): ").strip().lower()
        if p in ("high", "medium", "low"):
            return p
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

def prompt_time_bound():
    while True:
        tb = input("Is it time-bound? (yes/no): ").strip().lower()
        if tb in ("yes", "no"):
            return tb
        print("Invalid answer. Please enter 'yes' or 'no'.")

def build_reminder(task, priority, time_bound):
    # Use match-case for priority-specific reaction
    match priority:
        case "high":
            base = f"'{task}' is a high priority task"
        case "medium":
            base = f"'{task}' is a medium priority task"
        case "low":
            base = f"'{task}' is a low priority task"
        case _:
            base = f"'{task}' is a {priority} priority task"

    # Modify depending on time sensitivity
    if time_bound == "yes":
        reminder = f"Reminder: {base} that requires immediate attention today!"
    else:
        reminder = f"Reminder: {base}. Consider completing it when you have free time."
    return reminder

def main():
    task = prompt_task()
    priority = prompt_priority()
    time_bound = prompt_time_bound()

    reminder = build_reminder(task, priority, time_bound)
    print()
    print(reminder)

if __name__ == "__main__":
    main()