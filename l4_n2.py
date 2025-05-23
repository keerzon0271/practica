import sqlite3


class Drink:
    def __init__(self, name, alcohol_content):
        self.name = name
        self.alcohol_content = alcohol_content


class Cocktail:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price


def create_drink_database():
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            alcohol_content REAL,
            stock INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cocktails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            ingredients TEXT,
            price REAL
        )
    ''')

    conn.commit()
    conn.close()


def add_drink(drink, stock):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO drinks (name, alcohol_content, stock)
        VALUES (?, ?, ?)
    ''', (drink.name, drink.alcohol_content, stock))

    conn.commit()
    conn.close()


def view_drinks():
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM drinks')
    drinks = cursor.fetchall()

    conn.close()
    return drinks


def replenish_stock(drink_id, amount):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE drinks SET stock = stock + ? WHERE id = ?', (amount, drink_id))

    conn.commit()
    conn.close()


def add_cocktail(cocktail):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO cocktails (name, ingredients, price)
        VALUES (?, ?, ?)
    ''', (cocktail.name, ', '.join(cocktail.ingredients), cocktail.price))

    conn.commit()
    conn.close()


def view_cocktails():
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM cocktails')
    cocktails = cursor.fetchall()

    conn.close()
    return cocktails


create_drink_database()

vodka = Drink("Водка", 40)
add_drink(vodka, 100)

whiskey = Drink("Виски", 40)
add_drink(whiskey, 50)

all_drinks = view_drinks()
print("Все напитки:", all_drinks)

replenish_stock(1, 20)

cocktail1 = Cocktail("Кровавая Мэри", ["Водка", "Томатный сок", "Лимонный сок"], 150)
add_cocktail(cocktail1)

all_cocktails = view_cocktails()
print("Все коктейли:", all_cocktails)