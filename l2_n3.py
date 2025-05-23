class NumStorage:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def display_numbers(self):
        print(f"Число 1: {self.num1}, Число 2: {self.num2}")

    def change_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def sum_numbers(self):
        return self.num1 + self.num2

    def max_number(self):
        return max(self.num1, self.num2)

storage = NumStorage(5, 10)
storage.display_numbers()
print("Сумма чисел:", storage.sum_numbers())
print("Наибольшее число:", storage.max_number())


storage.change_numbers(15, 20)
storage.display_numbers()