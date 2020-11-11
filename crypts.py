from crypt_modules import *
from utils import delete_spaces, delete_repeats

functions = {
            'permutation': permutation,
            'row_permutation': row_permutation,
            'column_permutation': column_permutation,
            'caesar': caesar,
            'caesar_y': caesar_ymove,
            'caesar_xy': caesar_xymove,
}


def crypt(params_list):

    cipher = params_list[0]

    params_list[2] = delete_spaces(params_list[2])
    params_list[3] = delete_spaces(params_list[3])
    params_list[4] = delete_spaces(params_list[4])
    params_list[5] = delete_repeats(delete_spaces(params_list[5]))

    if cipher == 'permutation':
        return functions[cipher](params_list[1], params_list[2], params_list[3])

    elif cipher == 'row_permutation'\
            or cipher == 'column_permutation':
        return functions[cipher](params_list[1], params_list[2], params_list[4])

    elif cipher == 'caesar':
        return functions[cipher](params_list[1], params_list[2], params_list[4], params_list[3], params_list[5])

    else:
        return functions[cipher](params_list[1], params_list[2], params_list[4], params_list[5])


if __name__ == '__main__':

    some_list = [
        'permutation',
        'encrypt',
        'sometext',
        'help',
        'abcdefghijklmnopqrstuvwxyz'
    ]

    print(crypt(some_list))
