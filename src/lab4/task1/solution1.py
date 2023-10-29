import csv
from sys import stdin

films = dict() # словарь всех фильмов из файла


def parse_csv(file_name: str) -> list:
    '''
    Получает данные из файла csv и возварщает их как список
    >>> parse_csv("films.csv")
    [['1', 'Мстители: Финал'], ['2', 'Хатико'], ['3', 'Дюна'], ['4', 'Унесенные призраками']]
    >>> parse_csv("history.csv")
    [['2', '1', '3'], ['1', '4', '3'], ['2', '2', '2', '2', '2', '3']]
    '''
    with open(file_name, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        data = list()
        for row in reader:
            data.append(row)
    return data


def get_all_films(films_file: str):
    '''Получение списка фильмов из файла'''
    global films
    raw_data = parse_csv(films_file)
    films = dict()
    for data in raw_data:
        film = Film(int(data[0]), data[1])
        films[data[0]] = film


def get_all_users(users_history_file: str) -> list:
    '''Получение историй просмотров всех пользователей'''
    raw_data = parse_csv(users_history_file)
    users = list()
    for data in raw_data:
        users.append(User(data))
    return users


class Film:
    '''Класс, представляющий собой отдельный фильм, имеет идентификатор _id и название name'''
    def __init__(self, identificator: int, name: str):
        self._id = identificator
        self.name = name

    def get_id(self):
        '''Получение идентификатора фильма'''
        return self._id

    def get_name(self):
        '''Получение названия фильма'''
        return self.name

    def __repr__(self):
        return f"{self._id} {self.name}"

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)


class User:
    '''Класс, представляющий пользователя, имеет историю просмотров history и множество просмотренных фильмов watched'''
    def __init__(self, history: list):
        self.history = [films[i] for i in history]
        self.watched = set(self.history)

    def get_history(self):
        '''Получение истории просмотра пользователя'''
        return self.history

    def get_watched(self):
        '''Получение множетсва просмотренных фильмов пользователя'''
        return self.watched

    def match(self, other):
        '''Получение коэффициента совпадения просмотренных фильмов'''
        matched_films = self.watched.intersection(other.watched)
        return len(matched_films) / len(other.watched)


def solution(films_file: str, history_file: str, flow=stdin):
    '''Решение задачи'''
    get_all_films(films_file)
    users = get_all_users(history_file)
    inp = flow.readline()
    if inp == "":
        return ""
    inp = list(inp.strip().split(","))
    user_to_recomend = User(inp)
    match_raiting = [(user_to_recomend.match(user), user) for user in users]
    match_raiting.sort(key=lambda x: x[0])
    mathced_user = list(filter(lambda x: x[0] != 1, match_raiting))[-1][1]
    print(", ".join(list(map(str, mathced_user.get_watched().difference(user_to_recomend.get_watched())))))
    return ", ".join(list(map(str, mathced_user.get_watched().difference(user_to_recomend.get_watched()))))


if __name__ == "__main__":
    print(solution("films.csv", "history.csv"))
