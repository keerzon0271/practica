class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def get_salary(self):
        salary = self.__rate * self.__days
        print(f"Зарплата работника {self.get_name()} {self.get_surname()}: {salary}")

name = input("Имя работника: ")
surname = input("Фамилия работника: ")
rate = float(input("Ставка в день: "))
days = int(input("Отработанных дней: "))

worker = Worker(name, surname, rate, days)
worker.get_salary()