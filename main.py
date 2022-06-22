empty_chars_array = ["а", "б", "е", "ё", "ж", "з", "и", "й", "л", "о",
                     "р", "у", "ф", "х", "ц", "ч", "ъ", "ы", "ь", "э", "ю", "я"]

def return_letter_from_number(number):
    if number == "1":
        return "т"
    elif number == "2":
        return "н"
    elif number == "3":
        return "шщ"
    elif number == "4":
        return "м"
    elif number == "5":
        return "п"
    elif number == "6":
        return "сз"
    elif number == "7":
        return "г"
    elif number == "8":
        return "в"
    elif number == "9":
        return "д"
    elif number == "0":
        return "к"

def find_specific_letter(word, letter_1, start_index, letter_2 = None):
    if letter_2 == None:
        for i in range(start_index, len(word)):
            if word[i] == letter_1:
                if i == 0:
                    return True
                else:
                    return i
            elif word[i] not in empty_chars_array:
                return False
    else:
        for i in range(start_index, len(word)):
            if word[i] == letter_1 or word[i] == letter_2:
                if i == 0:
                    return True
                else:
                    return i
            elif word[i] not in empty_chars_array:
                return False

def test_for_empty_chars(word, start_index):
    result = False
    for index in range(start_index, len(word)):
        if word[index] not in empty_chars_array:
            result = True
            break
    return result


def create_list_from_file(input_number):
    all_words = []
    with open(f'{input_number}_words.txt', encoding='UTF-8') as file:
        for line in file:
            all_words.append(line)
    return all_words

def main():
    words = []
    with open('russian_nouns.txt', encoding='UTF-8') as file:
        for line in file:
            words.append([line, -1])

    input_number = input('Введите число: ')

    for digit in input_number:
        finding_letter = return_letter_from_number(digit)

        if len(finding_letter) == 1:
            unsuitable_words = []
            for word in words:
                if find_specific_letter(word[0], finding_letter, word[1]+1):
                    if find_specific_letter(word[0], finding_letter, word[1]+1) == True:
                        word[1] = 0
                    else:
                        word[1] = find_specific_letter(word[0], finding_letter, word[1]+1)
                else:
                    unsuitable_words.append(word)

            for word in unsuitable_words:
                try:
                    words.remove(word)
                except ValueError:
                    print('Не могу удалить', word)

        elif len(finding_letter) == 2:
            unsuitable_words = []
            for word in words:
                if find_specific_letter(word[0], finding_letter[0], word[1]+1, finding_letter[1]):
                    if find_specific_letter(word[0], finding_letter[0], word[1]+1, finding_letter[1]) == True:
                        word[1] = 0
                    else:
                        word[1] = find_specific_letter(word[0], finding_letter[0], word[1]+1, finding_letter[1])
                else:
                    unsuitable_words.append(word)

            for word in unsuitable_words:
                try:
                    words.remove(word)
                except ValueError:
                    print('Не могу удалить', word)


    unsuitable_words = []
    for word in words:
        if test_for_empty_chars(word[0].strip(), word[1]+1):
            unsuitable_words.append(word)

    for word in unsuitable_words:
        try:
            words.remove(word)
        except ValueError:
            print('Не могу удалить', word)

    if words:
        for word in words:
            print(word[0])
    else:
        print('Я ничего не нашёл')


if __name__ == '__main__':
    main()
