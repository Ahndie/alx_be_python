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
        # Accessing class attribute
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b

# Main function to demonstrate class and static methods
def main():
    # Using the static method
    result_add = Calculator.add(10, 20)
    print(f"Addition (static method): 10 + 20 = {result_add}")

    # Using the class method
    result_multiply = Calculator.multiply(5, 4)
    print(f"Multiplication (class method): 5 * 4 = {result_multiply}")

if __name__ == "__main__":
    main()
