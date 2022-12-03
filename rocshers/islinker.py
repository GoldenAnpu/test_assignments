import json
import os
import re
import logging
from urllib.error import HTTPError
import urllib.request as request

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


class URLLinesChecker:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.url_regexp = '^(?! )((?:(?<=[^a-zA-Z0-9]){0,}(?:(?:https?\:\/\/){0,1}(?:[a-zA-Z0-9\%]{1,}\:[a-zA-Z0-9\%]{1,' \
                          '}[@]){,1})(?:(?:\w{1,}\.{1}){1,5}(?:(?:[a-zA-Z]){1,})|(?:[a-zA-Z]{1,}\/[0-9]{1,3}\.[0-9]{1,' \
                          '3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,4}){1})){1}(?:(?:(?:\/{0,1}(?:[a-zA-Z0-9\-\_\=\-]){1,' \
                          '})*)(?:[?][a-zA-Z0-9\=\%\&\_\-]{1,}){0,1})(?:\.(?:[a-zA-Z0-9]){0,}){0,1})(?!.* $)'

        self.methods_to_test = (
            'GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH', 'SEARCH')
        self.dict_of_results = {}
        self.tuple_of_lines = ()
        self.urls_to_check = set()

    def split_lines(self) -> tuple:
        self.tuple_of_lines = tuple(self.input_string.splitlines())
        return self.tuple_of_lines

    def process_lines(self) -> tuple:
        line_number = 0
        for line in self.tuple_of_lines:
            line_number += 1
            if re.match(self.url_regexp, line):
                self.urls_to_check.add(line)
            else:
                self.return_not_url_message(line_number)
        self.urls_to_check = tuple(self.urls_to_check)  # for better iteration
        return self.urls_to_check

    @staticmethod
    def return_not_url_message(line_number: int) -> logging.info:
        logging.info(f' Строка "{line_number}" не является ссылкой')

    @staticmethod
    def prepare_url(url: str) -> str:
        url = url.strip()
        if url.startswith('www'):
            url = 'https://' + url
        return url

    def check_http_methods(self) -> dict:
        logging.info(' Обработка URLов. Пожалуйста подождите...')
        for url in self.urls_to_check:
            prepared_url = self.prepare_url(url)
            dict_of_responses = {}
            for method in self.methods_to_test:
                prep = request.Request(prepared_url, method=method)
                try:
                    response = request.urlopen(prep).status
                except HTTPError as err:
                    response = err.code
                if str(response) == '405':
                    continue
                else:
                    dict_of_responses[method] = response
            self.dict_of_results[prepared_url] = dict_of_responses
        return self.dict_of_results

    def get_results(self):
        print(json.dumps(self.dict_of_results, indent=4))


def check_existence_of_data():
    logging.info(' Пожалуйста, поместите ваши данные в input_data.txt файл.')
    logging.info(' Для продолжения нажмите любую кнопку.')
    input()
    while os.path.getsize('input_data.txt') == 0:
        logging.warning(' Файл пуст!')
        logging.warning(' Пожалуйста, поместите ваши данные в input_data.txt файл.')
        logging.warning(' После чего нажмите любую кнопку.')
        input()


if __name__ == "__main__":
    check_existence_of_data()
    with open("input_data.txt") as file:
        input_data = file.read()
        collected_lines = URLLinesChecker(input_data)
        collected_lines.split_lines()
        collected_lines.process_lines()
        collected_lines.check_http_methods()
        collected_lines.get_results()
