import argparse
import sys
import re


def read_to_list(filename):
    with open(filename, 'r') as file:
        nums = file.read().splitlines()
    return nums


class Literals:
    filepath: str
    text = []

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


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')

    return parser


if __name__ == '__main__':
    parser = createParser()
    path = parser.parse_args(sys.argv[1:])

    literals = Literals(path.path)
    all_literals = literals.find_literals()
    for key, value in all_literals.items():
        if (len(value) > 1):
            print("Lines with ", key, ": ", end="")
            for item in value:
                print(item, " ", end="")
            print("\n")
