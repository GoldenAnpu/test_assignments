from datetime import datetime
import calendar
import logging
import sys

logging.basicConfig(level=logging.INFO)


class FileParser:
    def __init__(self, filename, native='en', translate='ru'):
        self.filename = filename
        self.n_language = native
        self.t_language = translate
        self.data = None
        self.native_list = None
        self.translate_list = None

    def read_source_file(self):
        """ Read source file by lines and handles error if file not found """
        try:
            with open(self.filename, encoding='UTF-8') as test_file:
                self.data = test_file.readlines()
                return self.data
        except FileNotFoundError:
            logging.error(f' File not found. Please check the path and name for file {self.filename} and '
                          f'run again.')
            logging.info(' ---------------------------------------------------------------------------------------')
            logging.info(' You can call script execution with an argument pointing to the name of the source '
                         'file.')
            logging.info(' ---------------------------------------------------------------------------------------')
            exit()

    def create_file_to_save(self, language):
        """ Specify how to name files in various situations.
            Create files with specific names.
            Specific names are only supported for two languages: en and ru.
        """
        if language == self.n_language:
            filename_save = 'English'
        elif language == self.t_language:
            filename_save = 'Russian'
        else:
            filename_save = 'indefinite'

        try:
            file = open(f'{filename_save}.txt', 'x', encoding='UTF-8')
            return file
        except FileExistsError:
            stamp = calendar.timegm(datetime.utcnow().utctimetuple())
            logging.warning(f' File {filename_save}.txt already exists. Stamp {stamp} added to filename')
            filename_save = filename_save + '_' + str(stamp)
            file = open(f'{filename_save}.txt', 'x', encoding='UTF-8')
            return file

    def remove_duplicates_from_line(self, temp_dictionary, temp_list):
        """ Remove duplicate translations if only unique pairs are needed and saves to new lists. """
        if temp_list == 'native':
            self.native_list = list(dict.fromkeys(temp_dictionary[0].split(' ; ')))
        elif temp_list == 'translate':
            self.translate_list = list(dict.fromkeys(temp_dictionary[1].split(' ; ')))

    def write_to_language_files(self, native_file, translate_file):
        for native_item in self.native_list:
            for translate_item in self.translate_list:
                native_file.write(f'{native_item}\n')
                translate_file.write(f'{translate_item}\n')

    def cook_translation(self):
        """ Full cycle of preparing files with translation without duplication """
        native_file = self.create_file_to_save(self.n_language)
        translate_file = self.create_file_to_save(self.t_language)
        for line in self.data:
            if not line.startswith('#') and line != '\n':  # don't need to process unnecessary lines
                line = line.replace('\n', '')  # to avoid empty lines
                dictionary = line.split('\t')
                self.remove_duplicates_from_line(dictionary, 'native')
                self.remove_duplicates_from_line(dictionary, 'translate')
                self.write_to_language_files(native_file, translate_file)
        native_file.close()
        translate_file.close()
        logging.info(' Processed successfully')


if __name__ == "__main__":
    if len(sys.argv) > 1:  # support call argument in command line to select source file
        sys_filename = str(sys.argv[1])
        txt_file = FileParser(sys_filename)
    else:
        txt_file = FileParser('PythonTest.txt')
    txt_file.read_source_file()
    txt_file.cook_translation()



