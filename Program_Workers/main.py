import time
from random import randint
import statistics


class Worker:
    __task_count_all_workers = 0
    __levels = ['1', '2', '3', '4']
    total_labor_costs = 0

    def __init__(self, name, surname, efficiency, lenght):
        self.name = name
        self.surname = surname
        self.efficiency = efficiency
        self.lenght = lenght
        self.work_list = []
        self._count_tasks = 0
        self.cost_dict = {}
        self.time_dict = {}
        self.task_dict = {}
        self.task_list = []
        self.cost_list = []
        self.level_list = []

    def introduse(self):
        print(f'Здраствуйте,  я {self.name} {self.surname}')

    def add_tasks(self):

        for i in range(self.lenght):
            print(f'Введите задачу для выполнения  работнику {self.name}')
            task = input()
            while True:
                hard = input("Введите уровень сложности задания числом от 1 до 4 включительно ")
                if hard in Worker.__levels:
                    hard = int(hard)
                    break
                else:
                    print('Повторите попытку ')

            self.work_list.append(task)

            print(f'Хорошо, я выполню задание "{task}"')

            for f in self.work_list:
                self.time_dict[f] = randint(2, 8)

            time_task = self.time_dict[task]

            cost = (6 * (hard + time_task)) * 5

            self.task_dict = {
                'Task': task,
                'Time': time_task,
                'Level': hard,
                'Cost': cost
            }

            self.task_list.append(self.task_dict)
            self.cost_list.append(self.task_dict['Cost'])
            self.level_list.append(self.task_dict['Level'])
            jurnal.add_task(worker_name=self.name, task_name=task, task_time=time_task, task_cost=cost, task_level=hard)
            jurnal.get_average_cost(workers_cost=self.cost_list, worker_name=self.name)
            jurnal.get_average_level_of_task(workers_level=self.level_list, worker_name=self.name)

    def start_work(self):

        if self.work_list:

            print('Приступаю к работе')
            i = 0

            while len(self.work_list) > 0:
                print(f'Подождите пожалуйста, задача в работе')
                last_task = self.work_list.pop(i)
                time.sleep(self.time_dict[last_task])
                print(f'Выполнена задача {last_task}')
                self._count_tasks += 1
                Worker.__task_count_all_workers += 1
                print(f'Осталось задач {len(self.work_list)}')

        else:
            print('Нет не выполненных заданий')

        return self.task_list

    @staticmethod
    def work_time():
        print('Истекло ли рабочее время?')
        working_time = time.localtime()
        if working_time.tm_hour >= 18 or working_time.tm_hour <= 8:
            print('You can go home)')
        else:
            print(f'Fast Work!!! Вам осталось еще пару часов!')

    @staticmethod
    def get_task_count_all_workers():
        print(Worker.__task_count_all_workers)

    def salary_count(self):
        count_money = 0
        for y in self.task_list:
            count_money += y['Cost']
        Worker.total_labor_costs += count_money
        print('')
        print(f'Итоговая зарплата за выполнение этих задач  для работника {self.name} составляет {count_money} $')
        return count_money

    def time_count(self):
        time_count = 0
        for i in self.task_list:
            time_count += i['Time']

        print('')
        print(f'Предпологаемое время на выполнение данных задач для работника {self.name} составит {time_count} часов')


class Jurnal:

    def __init__(self):
        self.averages_cost = 0
        self.tasks = {}
        self.cost_of_task = {}
        self.workers_cost = []
        self.worker_cost_dict = {}
        self.averages_level = 0
        self.worker_level_dict = {}

    def add_task(self, worker_name, task_name, task_time, task_cost, task_level):
        if worker_name not in self.tasks:
            self.tasks[worker_name] = [{'Task': task_name, 'Time': task_time, 'Level': task_level, 'Cost': task_cost}]
        else:
            self.tasks[worker_name].append({
                'Task': task_name, 'Time': task_time, 'Level': task_level, 'Cost': task_cost})

    def display_tasks_by_user(self, worker_name):
        print(f'Вывод задач для {worker_name}')
        print(*self.tasks[worker_name], sep='\n')

    def get_average_cost(self, workers_cost, worker_name):
        self.averages_cost = statistics.mean(workers_cost)
        self.worker_cost_dict[worker_name] = self.averages_cost

    def get_average_level_of_task(self, workers_level, worker_name):
        self.averages_level = statistics.mean(workers_level)
        self.worker_level_dict[worker_name] = self.averages_level

    def display_average_level_of_task(self, worker_name):
        print('')
        print(f'Средний уровень сложности за выполнение задания для {worker_name} '
              f'равен {self.worker_level_dict[worker_name]}')

    def display_average_cost(self, worker_name):
        print('')
        print(f'Средняя цена за выполнение задания для {worker_name} составляет {self.worker_cost_dict[worker_name]} $')

    def display_all_task(self):
        for key in self.tasks.keys():
            print(f'Задачи сотрудника {key}')
            print(*list(self.tasks[key]), sep='\n')

    @staticmethod
    def display_total_labor_costs(total_salary):
        print('')
        print(f'Итоговые затраты на оплату труда составят {total_salary} $')


jurnal = Jurnal()

worker_1 = Worker(name='Victor', surname='Melnikov', efficiency='2 clience / hour', lenght=4)
worker_2 = Worker(name='john', surname='Smith', efficiency='1 clience / hour', lenght=3)

worker_1.introduse()

worker_2.introduse()


worker_1.add_tasks()

worker_2.add_tasks()

worker_1.start_work()
worker_1.salary_count()
worker_1.time_count()

worker_2.start_work()
worker_2.salary_count()
worker_2.time_count()


jurnal.display_tasks_by_user(worker_1.name)
jurnal.display_tasks_by_user(worker_2.name)
jurnal.display_all_task()

jurnal.get_average_cost(worker_1.cost_list, worker_1.name)
jurnal.get_average_cost(worker_2.cost_list, worker_2.name)
jurnal.display_average_cost(worker_1.name)
jurnal.display_average_cost(worker_2.name)

jurnal.get_average_level_of_task(worker_1.level_list, worker_1.name)
jurnal.get_average_level_of_task(worker_2.level_list, worker_2.name)
jurnal.display_average_level_of_task(worker_1.name)
jurnal.display_average_level_of_task(worker_2.name)

jurnal.display_total_labor_costs(Worker.total_labor_costs)
'''
каждая задача - рандомная стоимость
сколько в итоге заработает каждый работник
*сделать у задачи время выполнеия (случайное число)


Все задачи находятся в писке ворк_лист
1. К каждой задаче вводится только название и сложность
name=input()
level=input()
time = ....
price = ...

2. Сама задача - это словарь - {'name': 'task_1', 'level': 2, 'time':'randint()', 'price':randint}
[
{'name': 'task_1', 'level': 2, 'time':'randint()', 'price':randint},
{'name': 'task_1', 'level': 2, 'time':'randint()', 'price':randint},
{'name': 'task_1', 'level': 2, 'time':'randint()', 'price':randint},
]

добавить в журнал цену и уровень сложности
сколько денег затрачено на оплату работников
и выводить среднюю сложность, среднюю стоимость

'''