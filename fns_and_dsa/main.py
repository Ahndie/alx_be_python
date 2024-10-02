# temp_conversion_tool.py

# Constants for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)  # Factor to convert Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32  # Offset used in Fahrenheit to Celsius conversion

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def convert_to_celsius(fahrenheit):
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
    celsius = 100
    fahrenheit = 212
    
    print(f"{celsius}°C is {convert_to_fahrenheit(celsius):.2f}°F")
    print(f"{fahrenheit}°F is {convert_to_celsius(fahrenheit):.2f}°C")
