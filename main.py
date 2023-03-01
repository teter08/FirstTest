class Task:
    def __init__(self, name, description, status=False):
        self.name, self.description, self.status = name, description, status

    def display(self):
        print(f'{self.name} ' + ['Сделана', 'Не сделана'][self.status])


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, value):
        self.tasks.append(value)

    def remove_task(self, value):
        self.tasks.remove(value)


class TaskManager:
    def __init__(self, newtask: TaskList):
        self.task_list = newtask

    def mark_done(self, truetask: Task):
        truetask.status = True

    def mark_undone(self, falsetask: Task):
        falsetask.status = False

    def show_tasks(self):
        [print(a.display()) for a in self.task_list.tasks]


# Создаем список задач
todo = TaskList()
assert todo.tasks == []

# Создаем несколько задач и добавляем их в список
task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
assert task1.name == 'Стирка'
assert task1.description == 'Постирать трусы, носки, слюнявчики'
assert task1.status is False
task1.display()

todo.add_task(task1)
assert len(todo.tasks) == 1

task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
assert task2.name == 'Продукты'
assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
assert task2.status is False

todo.add_task(task2)
assert len(todo.tasks) == 2

# Создаем менеджер задач и показываем список задач
manager = TaskManager(todo)
assert isinstance(manager.task_list, TaskList)
print('-----Список дел-----')
manager.show_tasks()

# Отмечаем первую задачу выполненной и показываем список задач
manager.mark_done(task1)

# Проверяем изменился ли статус 2мя способами
assert task1.status is True
assert manager.task_list.tasks[0].status is True

print('-----Список дел-----')
manager.show_tasks()

# Удаляем вторую задачу и показываем список задач
todo.remove_task(task2)

assert len(todo.tasks) == 1
assert len(manager.task_list.tasks) == 1

print('-----Список дел-----')
manager.show_tasks()