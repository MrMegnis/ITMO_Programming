import unittest
from io import StringIO
from src.lab4.task1.solution1 import solution
import pathlib
import os


class Lab4Task1TestCase(unittest.TestCase):
    def test_example(self):
        '''Тест из примера'''
        input_text = """2,4"""
        # print(os.path.realpath(os.path.dirname(__file__)))
        films_path = "films.csv"
        history_path = "history.csv"
        if os.name == "nt":
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{history_path}"
        else:
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}/{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}/{history_path}"
        result = solution(films_path, history_path, StringIO(input_text))
        answer = """Дюна"""
        self.assertEqual(result, answer)

    def test_many_recomendations(self):
        '''Тест для проверки рекомендации более одного фильма'''
        input_text = """2,4"""
        films_path = "films2.csv"
        history_path = "history2.csv"
        if os.name == "nt":
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{history_path}"
        else:
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}/{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}/{history_path}"
        result = solution(films_path, history_path, StringIO(input_text))
        answer = """Мстители: Финал, Дюна"""
        self.assertEqual(result, answer)

    def test_many_match_all(self):
        '''Тест с совпадением всех фильмов у одного из пользоватедей с данным'''
        input_text = """1,3,5"""
        films_path = "films2.csv"
        history_path = "history2.csv"
        if os.name == "nt":
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{history_path}"
        else:
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}/{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}/{history_path}"
        result = solution(films_path, history_path, StringIO(input_text))
        answer = """Хатико"""
        self.assertEqual(result, answer)

    def test_empty(self):
        '''Тест на пустой ввод'''
        input_text = """"""
        films_path = "films2.csv"
        history_path = "history2.csv"
        if os.name == "nt":
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}\\{history_path}"
        else:
            films_path = f"{os.path.realpath(os.path.dirname(__file__))}/{films_path}"
            history_path = f"{os.path.realpath(os.path.dirname(__file__))}/{history_path}"
        result = solution(films_path, history_path, StringIO(input_text))
        answer = """"""
        self.assertEqual(result, answer)
