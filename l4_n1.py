import sqlite3


class Student:
    def __init__(self, first_name, last_name, patronymic, group, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.group = group
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            patronymic TEXT,
            group_name TEXT,
            grades TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_student(student):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (first_name, last_name, patronymic, group_name, grades)
        VALUES (?, ?, ?, ?, ?)
    ''', (student.first_name, student.last_name, student.patronymic, student.group, ','.join(map(str, student.grades))))
    conn.commit()
    conn.close()


def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students


def view_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student


def edit_student(student_id, updated_student):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET first_name=?, last_name=?, patronymic=?, group_name=?, grades=?
        WHERE id=?
    ''', (updated_student.first_name, updated_student.last_name, updated_student.patronymic, updated_student.group,
          ','.join(map(str, updated_student.grades)), student_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
    conn.commit()
    conn.close()


def average_grade_by_group(group_name):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT grades FROM students WHERE group_name=?', (group_name,))
    grades_list = cursor.fetchall()

    total_average = 0
    count = 0
    for grades in grades_list:
        individual_grades = list(map(int, grades[0].split(',')))
        total_average += sum(individual_grades) / len(individual_grades)
        count += 1

    if count == 0:
        return 0
    return total_average / count


def input_student_data():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    group = input("Введите группу: ")

    grades_input = input("Введите оценки через запятую (например, 5,4,3,2): ")
    grades = list(map(int, grades_input.split(',')))

    return Student(first_name, last_name, patronymic, group, grades)


def main():
    create_database()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить студента")
        print("2. Просмотреть всех студентов")
        print("3. Просмотреть студента по ID")
        print("4. Редактировать студента")
        print("5. Удалить студента")
        print("6. Средний балл по группе")
        print("7. Выход")
        choice = input("Ваш выбор: ")

        if choice == '1':
            student = input_student_data()
            add_student(student)
            print("Студент добавлен.")

        elif choice == '2':
            all_students = view_students()
            print("Все студенты:")
            for student in all_students:
                print(student)

        elif choice == '3':
            student_id = int(input("Введите ID студента: "))
            student_info = view_student(student_id)
            print("Информация о студенте:", student_info)

        elif choice == '4':
            student_id = int(input("Введите ID студента для редактирования: "))
            updated_student = input_student_data()
            edit_student(student_id, updated_student)
            print("Информация о студенте обновлена.")

        elif choice == '5':
            student_id = int(input("Введите ID студента для удаления: "))
            delete_student(student_id)
            print("Студент удален.")

        elif choice == '6':
            group_name = input("Введите название группы: ")
            avg_grade = average_grade_by_group(group_name)
            print(f"Средний балл группы {group_name}: {avg_grade:.2f}")

        elif choice == '7':
            break

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()