# temp_conversion_tool.py

# Constants for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Exact factor for Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Exact factor for Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32  # The offset value for Fahrenheit conversions

def convert_to_celsius(fahrenheit):
    """
    Converts Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def convert_to_fahrenheit(celsius):
    """
    Converts Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Example usage
if __name__ == "__main__":
    # Example temperature conversions
    celsius_temp = 100
    fahrenheit_temp = 212
    
    print(f"{celsius_temp}°C is {convert_to_celsius(celsius_temp):.2f}°F")
    print(f"{fahrenheit_temp}°F is {convert_to_fahrenheit(fahrenheit_temp):.2f}°C")
