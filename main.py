import logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger('Calculator')
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

    def add(self, a, b):
        result = a + b
        self.logger.info(f"Add: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.logger.info(f"Subtract: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.logger.info(f"Multiply: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.logger.info(f"Divide: {a} / {b} = {result}")
            return result
        else:
            self.logger.error("Divide by zero error.")
            raise ZeroDivisionError("Division by zero is not allowed.")
calculator = Calculator()


result1 = calculator.add(5, 3)
result2 = calculator.subtract(10, 4)
result3 = calculator.multiply(6, 2)
result4 = calculator.divide(15, 5)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
print(f"Result 4: {result4}")
