def find_strings(file_name: str, word: str, strings: list):
    with open(file_name, 'r') as file:
        mylist = (line.rstrip('\n').lower() for line in file)
        for string in mylist:
            spl_string = string.split(' ')
            for words in spl_string:
                if word == words:
                    yield string


def main():
    text = input('Add word to find\n').lower()
    answer = find_strings('file.txt', text, strings=[])
    list_of_strings = []
    for strings in answer:
        list_of_strings.append(strings)
    print(list_of_strings)


if __name__ == "__main__":
    main()
