from datetime import datetime
import calendar
import logging


class FileParser:
    def __init__(self, filename='PythonTest.txt'):
        self.filename = filename
        self.native = 'en'
        self.translate = 'ru'
        self.data = None

    def read_file(self):
        try:
            with open(self.filename, encoding='UTF-8') as test_file:
                self.data = test_file.readlines()
                return self.data
        except FileNotFoundError:
            print(f'\nPlease drop {self.filename} file in the same directory as parser.py and run again')
            exit()

    def cook_translation(self):
        lines_list = self.read_file()
        native_file = self.create_file_to_save(self.native)
        translate_file = self.create_file_to_save(self.translate)
        for line in lines_list:
            if not line.startswith('#') and line != '\n':  # don't need to process unnecessary lines
                line = line.replace('\n', '')  # to avoid empty lines
                dictionary = line.split('\t')
                native_list = list(dict.fromkeys(dictionary[0].split(' ; ')))  # remove duplicates after splitting
                translate_list = list(dict.fromkeys(dictionary[1].split(' ; ')))  # remove duplicates after splitting
                self.write_to_language_file(native_list, translate_list, native_file, translate_file)
        native_file.close()
        translate_file.close()
        print('Done')

    def write_to_language_file(self, native_list, translate_list, native_file, translate_file):
        for native_item in native_list:
            for translate_item in translate_list:
                native_file.write(f'{native_item}\n')
                translate_file.write(f'{translate_item}\n')

    def create_file_to_save(self, language):
        if language == 'en':
            filename_save = 'English'
        elif language == 'ru':
            filename_save = 'Russian'
        else:
            filename_save = 'indefinite'

        try:
            file = open(f'{filename_save}.txt', 'x', encoding='UTF-8')
            return file
        except FileExistsError:
            stamp = calendar.timegm(datetime.utcnow().utctimetuple())
            print(f'File {filename_save}.txt already exists. Stamp {stamp} added to filename')
            filename_save = filename_save + '_' + str(stamp)
            file = open(f'{filename_save}.txt', 'x', encoding='UTF-8')
            return file


if __name__ == '__main__':
    txt_file = FileParser()
    txt_file.cook_translation()
