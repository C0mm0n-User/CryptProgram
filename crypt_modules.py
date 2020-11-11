from utils import *


def permutation(action_choice, input_text, step):
    """
    Шифр - транспонирование
    :param action_choice: encrypt or decrypt
    :param input_text: str
    :param step: int or str
    :return: str
    """
    # Проверка типа ключа
    try:
        step = int(step)
    except ValueError:
        step = len(step)

    # Проверка action_choice
    if action_choice == 'encrypt':
        pass
    else:
        len(input_text) // step

    # Алгоритм шифра
    output_text = ''
    for letter in range(step):
        for i in range(len(input_text) // step):
            output_text += input_text[letter + (i * step)]
    return output_text


def column_permutation(action_choice, input_text, password):
    """
    шифр, меняющий местами "колонки", использую ключевое слово
    :param action_choice: encrypt or decrypt
    :param input_text: str
    :param password: str
    :return: str
    """
    # Проверка action_choice
    if action_choice == 'encrypt':
        word_to_sequence = word_to_sequence_encrypt(password)
    else:
        word_to_sequence = word_to_sequence_decrypt(password)
    print(word_to_sequence)

    # Алгоритм шифра
    output_text = ''
    for i in range(len(input_text) // len(password)):
        for letter in range(len(password)):
            output_text += input_text[int(word_to_sequence[letter]) + i * len(password)]
    return output_text


def row_permutation(action_choice, input_text, password):
    """
    шифр, меняющий местами "ряды", использую ключевое слово
    :param action_choice: encrypt or decrypt
    :param input_text: str
    :param password: str
    :return: str
    """
    # Проверка action_choice
    if action_choice == 'encrypt':
        word_to_sequence = word_to_sequence_encrypt(password)
    else:
        word_to_sequence = word_to_sequence_decrypt(password)
    print(word_to_sequence)

    # Алгоритм шифра
    output_text = ''
    for i in range(len(password)):
        for letter in range(len(input_text) // len(password)):
            output_text += input_text[int(word_to_sequence[i]) * (len(input_text) // len(password)) + letter]
    return output_text


def caesar(action_choice, input_text, key_word, key_step, alphabet):
    """

    :param action_choice:
    :param input_text:
    :param key_word:
    :param key_step:
    :param alphabet:
    :return:
    """
    if isinstance(key_step, int) is True:
        pass
    else:
        try:
            key_step = int(key_step)
        except ValueError:
            key_step = len(key_step)

    output_text = ''
    modified_alphabet = alphabet_key_step(alphabet_key_word(alphabet, key_word), key_step)
    print(modified_alphabet)

    if action_choice == 'encrypt':
        f_list = alphabet
        s_list = modified_alphabet
    else:
        f_list = modified_alphabet
        s_list = alphabet

    for symbol in input_text:
        for i in range(len(alphabet)):
            if symbol == f_list[i]:
                output_text += s_list[i]
    print(input_text)
    return output_text


def caesar_ymove(action_choice, input_text, key_word, alphabet):
    num_of_lines = len(alphabet)//magic_square(alphabet)
    new_alphabet = alphabet_key_word(alphabet, key_word)
    alphabet_list = alphabet_xy(new_alphabet)
    output_text = ''

    print(new_alphabet)
    print(alphabet_list)
    print(num_of_lines)

    if action_choice == 'encrypt':
        var = 1
    else:
        var = -1

    for char in input_text:
        for elem in alphabet_list:
            if char == elem[0]:
                for letter in alphabet_list:
                    if num_of_lines > elem[2]+var > -1:
                        if (elem[2]+var) == letter[2] and elem[1] == letter[1]:
                            output_text += letter[0]
                    elif elem[2]+var == num_of_lines:
                        if letter[2] == 0 and elem[1] == letter[1]:
                            output_text += letter[0]
                    elif elem[2]+var == -1:
                        if letter[2] == num_of_lines-1 and elem[1] == letter[1]:
                            output_text += letter[0]
    return output_text


def caesar_xymove(action_choice, input_text, key_word, alphabet):
    num_of_lines = len(alphabet)//magic_square(alphabet)
    num_of_columns = magic_square(alphabet)
    new_alphabet = alphabet_key_word(alphabet, key_word)
    alphabet_list = alphabet_xy(new_alphabet)
    output_text = ''

    print(new_alphabet)
    print(alphabet_list)
    print(num_of_lines)

    if action_choice == 'encrypt':
        var = 1
    else:
        var = -1

    for i in range(0, len(input_text), 2):
        for elem in alphabet_list:
            if input_text[i] == elem[0]:
                for elem2 in alphabet_list:
                    if input_text[i+1] == elem2[0]:
                        if elem[1] == elem2[1]:
                            for letter in alphabet_list:
                                if num_of_lines > elem[2] + var > -1:
                                    if (elem[2] + var) == letter[2] and elem[1] == letter[1]:
                                        output_text += letter[0]
                                elif elem[2] + var == num_of_lines:
                                    if letter[2] == 0 and elem[1] == letter[1]:
                                        output_text += letter[0]
                                elif elem[2] + var == -1:
                                    if letter[2] == num_of_lines - 1 and elem[1] == letter[1]:
                                        output_text += letter[0]
                            for letter2 in alphabet_list:
                                if num_of_lines > elem2[2] + var > -1:
                                    if (elem2[2] + var) == letter2[2] and elem2[1] == letter2[1]:
                                        output_text += letter2[0]
                                elif elem2[2] + var == num_of_lines:
                                    if letter2[2] == 0 and elem2[1] == letter2[1]:
                                        output_text += letter2[0]
                                elif elem2[2] + var == -1:
                                    if letter2[2] == num_of_lines - 1 and elem2[1] == letter2[1]:
                                        output_text += letter2[0]
                        elif elem[2] == elem2[2]:
                            for letter in alphabet_list:
                                if num_of_columns > elem[1] + var > -1:
                                    if (elem[1] + var) == letter[1] and elem[2] == letter[2]:
                                        output_text += letter[0]
                                elif elem[1] + var == num_of_columns:
                                    if letter[1] == 0 and elem[2] == letter[2]:
                                        output_text += letter[0]
                                elif elem[1] + var == -1:
                                    if letter[1] == num_of_columns - 1 and elem[2] == letter[2]:
                                        output_text += letter[0]
                            for letter2 in alphabet_list:
                                if num_of_columns > elem2[1] + var > -1:
                                    if (elem2[1] + var) == letter2[1] and elem2[2] == letter2[2]:
                                        output_text += letter2[0]
                                elif elem2[1] + var == num_of_columns:
                                    if letter2[1] == 0 and elem2[2] == letter2[2]:
                                        output_text += letter2[0]
                                elif elem2[1] + var == -1:
                                    if letter2[1] == num_of_columns - 1 and elem2[2] == letter2[2]:
                                        output_text += letter2[0]
                        else:
                            if action_choice == 'encrypt':
                                for letter in alphabet_list:
                                    if letter[1] == elem2[2] and letter[2] == elem[1]:
                                        output_text += letter[0]
                                for letter2 in alphabet_list:
                                    if letter2[1] == elem[2] and letter2[2] == elem2[1]:
                                        output_text += letter2[0]
                            else:
                                for letter in alphabet_list:
                                    if letter[1] == elem2[1] and letter[2] == elem[2]:
                                        output_text += letter[0]
                                for letter2 in alphabet_list:
                                    if letter2[1] == elem[1] and letter2[2] == elem2[2]:
                                        output_text += letter2[0]
    return output_text


if __name__ == '__main__':
    alphabet_used = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    action = 'decrypt'
    text = delete_spaces('ЖАКСАЛНДТ ОЦКН Ш ВШАДТМ ХШЕКВ КСШФ И УСКСНЛТ ГАМ ЕЛЙПКЖКФ'
                         'ШНЕЯ ФЕК РНШЛ ДЛ НСЛЕКЖАКСАЛНДЛМ ИФЕД ДКШСК Б ВШКЖ')
    key1 = '6'
    key2 = delete_repeats('АЛЕКСАНДРПУШКИН')

    print(caesar_xymove(action, text, key2, alphabet_used))
