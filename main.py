# Создайте кортеж из 7-ми именованных кортежей учащихся ВУЗов. В именованном кортеже будут присутствовать
# следующие поля: имя студента, возраст, оценка за семестр, город проживания. Функция good_students()
# будет принимать этот кортеж, вычислять среднюю оценку по всем учащимся и выводить на печать следующее
# сообщение: “Ученики {список имен студентов через запятую} в этом семестре хорошо учатся!”.
# В список студентов, которые выводятся по результатам работы функции, попадут лишь те, у которых оценка за
# семестр равна или выше средней по всем учащимся.

from collections import namedtuple

lst = ['Name', 'Age', 'Marks', 'City']
Student = namedtuple('Student', lst)
students = (
    Student('stud1', 20, 1, 'Yaros'),
    Student('stud2', 21, 2, 'Yaros'),
    Student('stud3', 22, 3, 'Yaros'),
    Student('stud4', 23, 4, 'Yaros'),
    Student('stud5', 24, 5, 'Yaros'),
    Student('stud6', 25, 5, 'Yaros'),
    Student('stud7', 36, 5, 'Yaros'))


def good_students(students):
    summarks = 0
    for student in students:
        summarks += student.Marks
    return summarks / len(students)


print(good_students(students))
