import csv


class Model:
    def __init__(self):
        self.__filename = None
        self.__line = 0
        self.__header = []
        self.__data = []

    @property
    def filename(self):
        return self.__filename

    @property
    def header(self):
        return self.__header

    @property
    def data(self):
        return self.__data

    @filename.setter
    def filename(self, value):
        self.__filename = value

    def read_data(self):
        self.__header = []
        self.__data = []
        with open(self.__filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            try:
                self.__header = next(reader)
                for row in reader:
                    self.__data.append(row)
            except StopIteration:
                pass
            file.seek(0)
        return self.__header, self.__data

    @staticmethod
    def search_data(search_string, data):
        search_results = []
        search_string = search_string.split(' ')
        for row in data:
            if all(any(word in value.lower() for value in row) for word in search_string):
                search_results.append(row)
        return search_results
