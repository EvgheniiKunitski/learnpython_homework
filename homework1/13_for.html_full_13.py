'''
Оценки
Создать список из словарей с оценками учеников разных классов школы вида 
[{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''

awesome_school = [
            {'school_class': '4a', 'scores': [8,9,6,7,5]},
            {'school_class': '4b', 'scores': [3,4,4,5,2]},
            {'school_class': '4c', 'scores': [5,7,8,8,7]},
            {'school_class': '6f', 'scores': [8,9,6,7,8]}
            ]


avg_class = 0
total_school_sum = 0
total_school_score_count = 0

for i in awesome_school:
    avg_class=sum(i["scores"])/len(i["scores"])
    for j in i["scores"]:
        total_school_sum += j
        total_school_score_count += 1
    print(f'Class "{i["school_class"]}" average score is {avg_class}')

print(f'awesome_school has average score {total_school_sum/total_school_score_count}')
