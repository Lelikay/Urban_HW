class User:
    '''
    Класс пользователя содержащий атрибуты: логин, пароль, проверка пароля
    '''
    def __init__(self, login, password, password_confirm):
        self.login = login
        if password == password_confirm:
            self.password = password

class Database:
    def __init__(self):
        self.data ={}

    def add_user(self, login, password):
        self.data[login] = password

    def __str__(self):
        return 'я список всех аккаунтов'

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Добрый день! Сделайте выбор:\n 1-Вход\n 2-Регистрация\n')
        if choice == '1':
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password in database.data[login]:
                    print(f'Hello, {login}')
                    break
                else:
                    print('Введён не верный пароль.')
            else:
                print(f'There is no login "{login}"')
        if choice == '2':
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                password_con := input('Повторно введите пароль: '))
            if (password != password_con):
                print('Пароли не совподают, попробуй снова.')
                # or (('A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'P' or
                # 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z') not in password) or
                # ('0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9') not in password):
            continue
            database.add_user(user.login, user.password)
        print(database.data)