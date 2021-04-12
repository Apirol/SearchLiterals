from input_handler import read_to_list
import re

class Literals:
    filepath: str
    text: str

    __literals = {}

    def __init__(self, filepath):
        self.filepath = filepath
        self.text = read_to_list(self.filepath)

    def __add_literal(self, regex_result, index):
        indexes = set()
        for item in regex_result:
            literals = self.literals
            if (literals.get(item)):
                indexes = self.literals[item]
                indexes.add(index)
            else:
                indexes.add(index)
            self.__add__(item, indexes)

    def __add__(self, key, value):
        self.__literals[key] = value

    @property
    def literals(self):
        return self.__literals

    def find_literals(self):
        regex1 = r'\'(.+?)\''
        regex2 = r'\"(.+?)\"'

        for iter, item in enumerate(self.text):
            if item == "":
                continue

            result_regex1 = re.findall(regex1, item)
            result_regex2 = re.findall(regex2, item)
            self.__add_literal(result_regex1, iter)
            self.__add_literal(result_regex2, iter)
        return self.literals

    def print_literals(self):
        return 0
