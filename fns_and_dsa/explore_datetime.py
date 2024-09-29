# explore_datetime.py

from datetime import datetime, timedelta  # Ensure correct imports

def display_current_datetime():
    """
    Displays the current date and time, and performs timedelta operations.
    """
    current_time = datetime.now()
    print(f"Current date and time: {current_time}")

    # Add 5 days to the current date
    future_time = current_time + timedelta(days=5)
    print(f"Date and time after 5 days: {future_time}")

    # Subtract 10 hours from the current time
    past_time = current_time - timedelta(hours=10)
    print(f"Date and time 10 hours ago: {past_time}")

    # Calculate the difference between two dates
    another_time = datetime(2024, 1, 1, 12, 0, 0)
    time_difference = another_time - current_time
    print(f"Time difference between {another_time} and now: {time_difference}")

def calculate_future_date(days: int):
    """
    Calculates the date that is a specified number of days from the current date.
    
    Parameters:
    days (int): Number of days to add to the current date.

    Returns:
    datetime: The future date.
    """
    current_time = datetime.now()
    future_date = current_time + timedelta(days=days)
    return future_date

# Call the functions
if __name__ == "__main__":
    display_current_datetime()

    # Example usage of calculate_future_date
    days_to_add = 10
    future_date = calculate_future_date(days_to_add)
    print(f"\nThe date {days_to_add} days from now will be: {future_date}")
