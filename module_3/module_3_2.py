def send_email(message, rec, *, sender='azabotkin04@gmail.com'):

    if '@' and ('.com' or '.ru' or '.net') not in (sender or rec):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {rec}")
    elif sender == rec:  #мне кажется, что if тут подходит лучше, так как если у пользователя будут обе ошибки, он их сразу сможет исправить
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'azabotkin04@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {rec}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {rec}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')