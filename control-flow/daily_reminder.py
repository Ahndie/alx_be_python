# Ask the user for their task
Task = input("Enter your task: ")

# Ask for the priority level (high, medium, low)
Priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-sensitive (yes/no)
Time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop through the reminder 3 times to emphasize importance
for i in range(3):
    print("\nReminder #", i + 1)

    # Provide task details based on time sensitivity
    if time_bound == "yes":
        time_reminder = "This task is time-sensitive! Don't delay."
    else:
        time_reminder = "This task is not time-sensitive, but still important."

    # Provide customized reminder based on priority using match case
    match priority:
        case "high":
            print(f"Task: {task}")
            print("Priority: HIGH! Make sure to complete it ASAP.")
            print(time_reminder)
        case "medium":
            print(f"Task: {task}")
            print("Priority: Medium. Try to finish it today.")
            print(time_reminder)
        case "low":
            print(f"Task: {task}")
            print("Priority: Low. You can take your time, but don’t forget it.")
            print(time_reminder)
        case _:
            print(f"Task: {task}")
            print("Priority: Not clearly defined. Treat it with caution.")
            print(time_reminder)

    # Add a line to separate each reminder
    print("-" * 30)

print("\nGood luck with your task!")
