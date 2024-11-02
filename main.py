# Использование %:
def procent():
    team1_num = 5
    team2_num = 6
    print('В команде Мастера кода участников: %s !' % (team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

#Использование format():
def format():
    score_2 = 42
    team1_time = 18015.2
    print('Команда Волшебники данных решила задач: {} !'.format(score_2))
    print('Волшебники данных решили задачи за {} с !'.format(team1_time))

#Использование f-строк:
def f_string(score_1 = 40, score_2 = 42):
    team_1 = "Мастера кода"
    team_2 = "Волшебники данных"
    tasks_total = score_1 + score_2
    team1_time = 1552.512
    team2_time = 2153.31451
    time_avg = (team1_time + team2_time) / 2
    print(f'Команды решили {score_1} и {score_2} задач')
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print(f'Результат битвы: победа команды {team_1} !')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print(f'Результат битвы: победа команды {team_2} !')
    else:
        print("Ничья!")

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')
f_string(20, 1)



