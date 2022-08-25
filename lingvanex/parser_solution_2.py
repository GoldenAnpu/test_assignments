from datetime import datetime
import calendar
import logging
import sys

logging.basicConfig(level=logging.DEBUG)


class FileParser:
    def __init__(self, filename, native='en', translate='ru'):
        self.filename = filename
        self.n_language = native
        self.t_language = translate
        self.data = None
        self.native_data = []
        self.translate_data = []
        self.native_data_cleaned = []
        self.translate_data_cleaned = []
        self.stamp = None
        self.n_filename = None
        self.t_filename = None

    def read_source_file(self):
        """ Reads source file by lines and handles error if file not found """
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

    def store_language_data(self):
        """ Splits and saves language-based data into a lists, avoiding comment lines and empty lines. """
        for line in self.data:
            if not line.startswith('#') and line != '\n':  # don't need to process unnecessary lines
                line = line.replace('\n', '')  # to avoid empty lines
                dictionary = line.split('\t')
                self.native_data.append([dictionary[0]])
                self.translate_data.append([dictionary[1]])

    def remove_duplicates_from_line(self):
        """ Removes duplicate translations if only unique pairs are needed and saves to new lists. """
        for element in self.native_data:
            cleaned_element = list(dict.fromkeys(element[0].split(' ; ')))
            self.native_data_cleaned.append(cleaned_element)
        for element in self.translate_data:
            cleaned_element = list(dict.fromkeys(element[0].split(' ; ')))
            self.translate_data_cleaned.append(cleaned_element)

    def determine_file_name(self, exists=False):
        """ Specifies how to name files in various situations.
        Certain name is only supported for two languages: en and ru.

        If a file with the same name exists in the directory, it is expanded with a timestamp.
        """
        self.stamp = calendar.timegm(datetime.utcnow().utctimetuple())
        if exists:
            if self.n_language == 'en':
                self.n_filename = f'English_{self.stamp}'
            else:
                self.n_filename = f'n_indefinite_{self.stamp}'

            if self.t_language == 'ru':
                self.t_filename = f'Russian_{self.stamp}'
            else:
                self.t_filename = f't_indefinite_{self.stamp}'
        else:
            if self.n_language == 'en':
                self.n_filename = 'English'
            else:
                self.n_filename = 'n_indefinite'

            if self.t_language == 'ru':
                self.t_filename = 'Russian'
            else:
                self.t_filename = 't_indefinite'

    def create_files_and_write(self):
        with open(f'{self.n_filename}.txt', 'x', encoding='UTF-8') as native_file:
            with open(f'{self.t_filename}.txt', 'x', encoding='UTF-8') as translate_file:
                n = 0
                while n < len(self.native_data_cleaned):
                    for native_item in self.native_data_cleaned[n]:
                        for translate_item in self.translate_data_cleaned[n]:
                            native_file.write(f'{native_item}\n')
                            translate_file.write(f'{translate_item}\n')
                    n += 1

    def process_errors_when_save(self):
        try:
            self.determine_file_name()
            self.create_files_and_write()
            logging.info(' Processed successfully.')
        except FileExistsError:
            self.determine_file_name(exists=True)
            self.create_files_and_write()
            logging.warning(f' Files already exist. Stamp {self.stamp} added to filenames.')
            logging.info(' Processed successfully.')

    def cook_translation(self):
        """ Full cycle of creating files with translation without duplication """
        self.read_source_file()
        self.store_language_data()
        self.remove_duplicates_from_line()
        self.process_errors_when_save()


if __name__ == "__main__":
    if len(sys.argv) > 1:  # supports call argument in command line to select source file
        sys_filename = str(sys.argv[1])
        txt_file = FileParser(sys_filename)
    else:
        txt_file = FileParser('PythonTest.txt')
    txt_file.cook_translation()

