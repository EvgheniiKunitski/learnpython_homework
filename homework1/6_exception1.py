"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

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

    
if __name__ == "__main__":
    var_ask_user = True
    while var_ask_user:
        try:
            var_ask_user = ask_user()
        except(KeyboardInterrupt):
            print()
            print("Пока!")
            break

