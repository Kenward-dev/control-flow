# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority level entered.")

# Modify reminder based on time-bound status
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print("Reminder:", reminder)

elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
    print("Reminder:", reminder)

