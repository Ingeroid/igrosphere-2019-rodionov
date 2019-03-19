import re


def read_file(file_path):
    with open(file_path, 'r')as f:
        return f.read()





if __name__ == "__main__":
    filename = "coverage-error.log"
    regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:\d\d\].+"
    lines = read_file(filename)
    print("Author is dmitriy.galamaga")
    print(filter_lines(regexp, lines))

