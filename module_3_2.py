def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if '@' and ('.com' or '.ru' or '.net') not in (recipient or sender):
        print(f'Невозможно отправить письмо с адрес {sender} на адрес {recipient}')

    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с одреса {sender} на адрес {recipient}')





send_email("", "vasyok1337@gmail.com", sender="university.help@gmail.com")
send_email("", "urban.fan@gmail.ru", sender="urban.info@gmail.com")
send_email("", "urban.student@mail.uk", sender="university.help@gmail.uk")
send_email("", "vasyok1337@gmail.com", sender="vasyok1337@gmail.com")