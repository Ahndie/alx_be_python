# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to return the product of two numbers."""
        # Adjusting the output format for "calculation type"
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Main function to demonstrate class and static methods
def main():
    # Using the static method
    result_add = Calculator.add(10, 5)
    print(f"The sum is: {result_add}")

    # Using the class method
    result_multiply = Calculator.multiply(10, 5)
    print(f"The product is: {result_multiply}")

if __name__ == "__main__":
    main()
