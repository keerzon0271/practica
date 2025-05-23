class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Пункт назначения: {self.destination}, Номер поезда: {self.train_number}, "
              f"Время отправления: {self.departure_time}")

train = Train("Томск", "123А", "11:00")
train2 = Train("Новосибирск", "79", "17:00")
train3 = Train("Москва", "14", "8:00")
train4 = Train("Красноярск", "19Б", "19:00")
train.display_info()
train2.display_info()
train3.display_info()
train4.display_info()

train_number_input = input("Введите номер поезда для получения информации: ")
if train.train_number == train_number_input:
    train.display_info()
else:
    print("Поезд с таким номером не найден.")