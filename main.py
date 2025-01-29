path_to_file = "./books/frankenstein.txt"

def read_file():
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    return len(text.split())


def count_chars():
    d = {}
    for word in read_file():
        for char in word.lower():
            d[char] = d.get(char, 0) + 1
    return d

def print_report():
    d = count_chars()
    for key, value in d.items():
        if key.isalpha():
            print(f"the '{key}' character was found {value} times")


def main():
    print_report()




if __name__ == "__main__":
    main()