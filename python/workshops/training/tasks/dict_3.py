# Написать программу, которая спрашивает у пользователя, какие у него имя, фамилия, возраст, любимая еда, музыкальная группа и заветная мечта.
# Результаты программа должна складывать в словарь, в котором ключи - имена и фамилии пользователей, значения - все остальное.
# Программа должна спрашивать эту информацию у 7 пользователей.
# Потом она должна загадывать вам мечту, или мечту и еду, или музыкальную группу, или музыкальную группу и еду (выбирая, что именно загадать, случайным образом) и предлагать угадать, что это был за пользователь.

def define():
    persfood = {}
    persmuusic = {}
    persdream = {}
    name = input() + ' ' + input()
    age = input()
    persfood[name] = input()
    persmuusic[name] = input()
    persdream[name] = input()


def food(name):
    persfood = {}
    persfood[name] = input()
    return persfood

    for i in range(7):
        persfood = {}
        persmuusic = {}
        persdream = {}
        name = input() + ' ' + input()
        age = input()
        persfood[name] = input()
        persmuusic[name] = input()
        persdream[name] = input()

def music(name):
