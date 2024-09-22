class User:
    '''
    Класс пользователя содержащий атрибуты:
    '''
    def __init__(self, login, password, age):
        self.login = login
        self.password = hash(password)
        self.age = int(age)

class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in (self, nickname, password):
        if users[nickname] == password