from sys import stdin


class Person:
    '''Класс, представляющий собой отдельного человека, имеет ФИО name и возраст age'''

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"

    def __str__(self):
        return f"{self.name} ({self.age})"

    def get_name(self):
        '''Получение ФИО пользователя'''
        return self.name

    def get_age(self):
        '''Получение возраста пользователя'''
        return self.age


def solution(flow=stdin):
    '''Решение задачи'''
    groups = [18, 25, 35, 45, 60, 80, 100, 124]
    print_groups = {
        18: "0-18",
        25: "19-25",
        35: "26-35",
        45: "36-45",
        60: "46-60",
        80: "61-80",
        100: "81-100",
        124: "101+"
    }
    ans = list()
    breakdown_groups = {i: [] for i in groups}
    inp = flow.readline().strip()
    while inp != "":
        inp = inp.split(",")
        person = Person(inp[0], int(inp[1]))
        i = 0
        while person.get_age() > groups[i]:
            i += 1
        breakdown_groups[groups[i]].append(person)
        inp = flow.readline().strip()
    for i in groups[::-1]:
        group = breakdown_groups[i]
        if len(group) > 0:
            group.sort(key=lambda x: (-x.get_age(), x.get_name()))
            group = list(map(str, group))
            ans.append(f"{print_groups[i]}: {', '.join(group)}")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solution())
