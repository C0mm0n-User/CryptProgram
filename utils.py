def word_to_sequence_encrypt(key):
    """

    :param key:
    :return:
    """
    sequence = []
    abc = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for letter in abc:
        var = 0
        for symbol in key:
            var += 1
            if symbol == letter:
                sequence.append(var-1)
    return sequence


def word_to_sequence_decrypt(key):
    """
    some text
    :param key:
    :return:
    """
    sequence = []
    var_sequence = word_to_sequence_encrypt(key)
    var = ''
    for i in var_sequence:
        var += key[int(i)]
    for symbol in key:
        perem = 0
        for letter in var:
            if symbol == letter:
                for char in sequence:
                    if char == perem:
                        break
                else:
                    sequence.append(perem)
                    break
            perem += 1
    return sequence


def alphabet_key_word(alphabet, key):
    modified_alphabet = delete_repeats(key + alphabet)
    return modified_alphabet


def alphabet_key_step(alphabet, key):
    modified_alphabet = ''
    for i in range(key):
        modified_alphabet += alphabet[len(alphabet) - key + i]
    modified_alphabet += alphabet
    modified_alphabet = delete_repeats(modified_alphabet)
    return modified_alphabet


def alphabet_xy(alphabet):
    num_of_lines = magic_square(alphabet)
    alphabet_list = []
    for i in range(len(alphabet) // num_of_lines):
        for char in range(num_of_lines):
            alphabet_list.append((alphabet[i * num_of_lines + char], char, i))
    return alphabet_list


def magic_square(alphabet):
    var = 0
    for i in range(2, len(alphabet)//2):
        if (len(alphabet) % i) == 0:
            if len(alphabet)//i >= i:
                var = i
    return len(alphabet)//var


def delete_spaces(text):
    """
    delete all spaces in the text, returns text
    :param text: str
    :return: str
    """
    modified_text = ''
    for i in text:
        if i != ' ' and i != '/n':
            modified_text += i
    return modified_text


def delete_repeats(text):
    """
    delete repeatable symbols in the text, return modified text
    :param text: str
    :return: str
    """
    modified_text = ''
    for letter in text:
        for symbol in modified_text:
            if symbol == letter:
                break
        else:
            modified_text += letter
    return modified_text


if __name__ == '__main__':
    print(alphabet_xy(alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,-'))
