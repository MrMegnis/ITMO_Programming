import unittest
from io import StringIO
from src.lab4.task1.solution1 import solution


class Lab4Task1TestCase(unittest.TestCase):
    def test_example(self):
        '''Тест из примера'''
        input_text = """2,4"""
        result = solution("films.csv", "history.csv", StringIO(input_text))
        answer = """Дюна"""
        self.assertEqual(result, answer)

    def test_many_recomendations(self):
        '''Тест для проверки рекомендации более одного фильма'''
        input_text = """2,4"""
        result = solution("films2.csv", "history2.csv", StringIO(input_text))
        answer = """Мстители: Финал, Дюна"""
        self.assertEqual(result, answer)

    def test_many_match_all(self):
        '''Тест с совпадением всех фильмов у одного из пользоватедей с данным'''
        input_text = """1,3,5"""
        result = solution("films2.csv", "history2.csv", StringIO(input_text))
        answer = """Хатико"""
        self.assertEqual(result, answer)

    def test_empty(self):
        '''Тест на пустой ввод'''
        input_text = """"""
        result = solution("films2.csv", "history2.csv", StringIO(input_text))
        answer = """"""
        self.assertEqual(result, answer)