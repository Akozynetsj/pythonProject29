import logging

class DataRecorder:
    def __init__(self):
        self.logger = logging.getLogger('DataRecorder')
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('data.log')
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def record_data(self, filename):
        try:
            data = input("Введіть дані: ")
            self.logger.info(f"Введені дані: {data}")
            with open(filename, 'w') as file:
                file.write(data)
            self.logger.info(f"Дані успішно записано у файл {filename}")
        except Exception as e:
            self.logger.error(f"Помилка запису даних у файл {filename}: {str(e)}")


recorder = DataRecorder()
filename = 'data.txt'
recorder.record_data(filename)
