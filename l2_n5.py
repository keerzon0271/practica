class CustomClass:
    def __init__(self, prop1=0, prop2=0):
        self.prop1 = prop1
        self.prop2 = prop2
        print(f"Создан объект с prop1={self.prop1} и prop2={self.prop2}")

    def __del__(self):
        print(f"Удаление объекта с prop1={self.prop1} и prop2={self.prop2}")

obj1 = CustomClass(5, 10)
obj2 = CustomClass()

del obj1
del obj2
