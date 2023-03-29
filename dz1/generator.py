def find_strings(file_name: str, word: str):
    strings = []
    with open(file_name, 'r') as file:
        mylist = [line.rstrip('\n') for line in file]
    for string in mylist:
        string = string.split(' ')
        for words in string:
            print(words, string)
            if word == words:
                strings.append(words)
    return strings


def main():
    text = input()
    find_strings('file.txt', text)


if __name__ == "__main__":
    main()
