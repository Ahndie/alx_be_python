# temp_conversion_tool.py

# Global variables (conversion factors)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius temperature to Fahrenheit.
    """
    fahrenheit_temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit_temp

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit temperature to Celsius.
    """
    celsius_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius_temp

# Example usage
if __name__ == "__main__":
    celsius_value = 25
    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value}°C is approximately {fahrenheit_value:.2f}°F")

    fahrenheit_value = 77
    celsius_value = fahrenheit_to_celsius(fahrenheit_value)
    print(f"{fahrenheit_value}°F is approximately {celsius_value:.2f}°C")
