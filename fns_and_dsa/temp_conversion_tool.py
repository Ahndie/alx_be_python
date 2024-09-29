# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit temperature to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius temperature to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_user_input():
    """
    Prompt user for temperature and unit choice.
    """
    try:
        temp_str = input("Enter a temperature value: ")
        temperature = float(temp_str)
        unit = input("Is it in Celsius (C) or Fahrenheit (F)? ").lower()
        return temperature, unit
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    try:
        temperature, unit = get_user_input()

        if unit == "c":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is approximately {converted_temp:.2f}°F")
        elif unit == "f":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is approximately {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
