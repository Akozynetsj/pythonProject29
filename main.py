import logging
import random

class RandomNumberGenerator:
    def __init__(self):
        self.logger = logging.getLogger('RandomNumberGenerator')
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('numbers.log')
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def generate_numbers(self, filename, count):
        try:
            with open(filename, 'w') as file:
                for i in range(count):
                    number = random.randint(1, 100)
                    file.write(str(number) + '\n')
                    self.logger.info(f"Згенероване число: {number}")
            self.logger.info(f"Згенеровані числа успішно записано у файл {filename}")
        except Exception as e:
            self.logger.error(f"Помилка запису згенерованих чисел у файл {filename}: {str(e)}")


generator = RandomNumberGenerator()


filename = 'numbers.txt'
count = 10
generator.generate_numbers(filename, count)
