class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        salary = self.rate * self.days
        print(f"Зарплата работника {self.name} {self.surname}: {salary}")

name = input("Имя работника: ")
surname = input("Фамилия работника: ")
rate = float(input("Ставка в день: "))
days = int(input("Отработанных дней: "))
worker = Worker(name, surname, rate, days)
worker.get_salary()