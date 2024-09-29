# temp_conversion_tool.py

# Conversion factors constants
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(fahrenheit):
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
    
    print(f"{celsius_temp}°C is {celsius_to_fahrenheit(celsius_temp):.2f}°F")
    print(f"{fahrenheit_temp}°F is {fahrenheit_to_celsius(fahrenheit_temp):.2f}°C")
