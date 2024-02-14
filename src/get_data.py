import json
from typing import Any

import requests

from src.config import DATA
from src.abstract_class import AbstractClass


class GetVacancies(AbstractClass):
    all = []

    def __init__(self, name_vacancy: str):
        self.name_vacancy: str = name_vacancy
        self.message = "Vacancies found"
        self.all_vacancy = self.get_vacancy_from_api()

    def __repr__(self):
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self) -> str | Any:
        """Get reliable information about vacancies for the user"""

        if isinstance(self.name_vacancy, str):
            keys_response = {'text': f'NAME:{self.name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']
        else:
            self.message = "Vacancy not found"
            return self.message

    def save_info(self) -> str or list:
        """A json file with information about vacancies has been created"""

        if len(self.all_vacancy) == 0:
            self.message = "Vacancy not found"
            return self.message
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
            return self.all_vacancy
