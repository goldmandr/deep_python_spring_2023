def find_strings(file_name: str, word: str, strings: list):
    with open(file_name, 'r') as file:
        mylist = [line.rstrip('\n') for line in file]
    for string in mylist:
        spl_string = string.split(' ')
        for words in spl_string:
            if word == words:
                strings.append(string)
    return strings


def main():
    text = input()
    answer = find_strings('file.txt', text, strings=[])
    print(answer)


if __name__ == "__main__":
    main()
