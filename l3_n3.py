class Calculation:
    def __init__(self):
        self.__calculation_line = ""

    def set_calculation_line(self, line):
        self.__calculation_line = line

    def set_last_symbol_calculation_line(self, symbol):
        self.__calculation_line += symbol

    def get_calculation_line(self):
        return self.__calculation_line

    def get_last_symbol(self):
        if self.__calculation_line:
            return self.__calculation_line[-1]
        return None

    def delete_last_symbol(self):
        if self.__calculation_line:
            self.__calculation_line = self.__calculation_line[:-1]

calc = Calculation()
calc.set_calculation_line("5+3")
print("Текущая строка расчета:", calc.get_calculation_line())

calc.set_last_symbol_calculation_line("*2")
print("После добавления символа:", calc.get_calculation_line())

print("Последний символ:", calc.get_last_symbol())

calc.delete_last_symbol()
print("После удаления последнего символа:", calc.get_calculation_line())