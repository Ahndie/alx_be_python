# temp_conversion_tool.py

#Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Global Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Global Factor to convert Celsius to Fahrenheit


def convert_to_celsius(fahrenheit): #Convert Fahrenheit to Celsius using the global conversion factor.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
    

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius): #Converts Celsius to Fahrenheit using the global conversion factor.
    
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Function to handle user interaction
def user_interaction():
    """
    Prompts the user for temperature input and converts it based on the specified unit.
    Handles input validation and displays the result.
    """
    try:
        # Prompt the user for a temperature value
        temp_input = input("Enter the temperature: ")

        # Validate if input is numeric
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Convert input to float
        temperature = float(temp_input)

        # Prompt the user for the unit
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
        
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")
        
        else:
            # Raise error for invalid unit input
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

# Main execution block
if __name__ == "__main__":
    user_interaction()
