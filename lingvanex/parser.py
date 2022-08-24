def try_to_save(filename, answer=''):
    """ Decides to create or open an existing file for the following interaction

    :param filename: name for txt file
    :param answer: mode for open()
    :return: list [file, answer]
    """
    try:
        file = open(f'{filename}.txt', 'x', encoding='UTF-8')
        answer = 'X'
        return file, answer
    except FileExistsError:
        print(f'\nFile {filename}.txt already exists')
        while answer not in ['A', 'O']:
            answer = input(' - type O if you want to overwrite\n'
                           ' - type A if you want to append\n\n'
                           'Your choice: ')
        if 'O' in answer:
            print(f'\n{filename}.txt overwrote')
            file = open(f'{filename}.txt', 'w', encoding='UTF-8')
            return file, answer
        elif 'A' in answer:
            print(f'\n{filename}.txt extended')
            file = open(f'{filename}.txt', 'a', encoding='UTF-8')
            return file, answer
        elif 'X' in answer:
            file = open(f'{filename}.txt', 'x', encoding='UTF-8')
            return file, answer


received_file = 'PythonTest.txt'

try:
    with open(received_file, encoding='UTF-8') as test_file:
        lines_list = test_file.readlines()
except FileNotFoundError:
    print(f'\nPlease drop {received_file} file in the same directory as parser.py and run again')
    exit()

english_file = try_to_save('English')
russian_file = try_to_save('Russian', english_file[1])  # operation must be the same for both files

for line in lines_list:
    if not line.startswith('#') and not line.startswith('\n'):  # don't need to process unnecessary lines
        line = line.replace('\n', '')  # to avoid empty lines
        dictionary = line.split('\t')
        english_list = list(dict.fromkeys(dictionary[0].split(' ; ')))  # remove duplicates after splitting
        russian_list = list(dict.fromkeys(dictionary[1].split(' ; ')))  # remove duplicates after splitting
        for english_item in english_list:
            for russian_item in russian_list:
                english_file[0].write(f'{english_item}\n')
                russian_file[0].write(f'{russian_item}\n')
english_file[0].close()
russian_file[0].close()
