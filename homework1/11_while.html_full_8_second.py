
'''
Задание
Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соответствующий ответ. Например:
'''

speach =  {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Не подскажете?": "Пошел проч малой",
           "Почем опиум для народа?": "Дораха!", "Пока": "Ну пока!"}

def ask_user():
    user_answer = input('Что скажешь? ')
    if speach.get(user_answer) != None:
        if user_answer == "Пока":
            print(speach.get(user_answer))
            return False
        print(speach.get(user_answer))
        return True
    else:
        print("Не понял?")
        return True

var_ask_user = True
while var_ask_user:
    var_ask_user = ask_user()

