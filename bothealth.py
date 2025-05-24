import logging
import random
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помощник для Здоровья. Используй /help для получения списка команд."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "/start - Приветствие\n"
        "/help - Показать это сообщение\n"
        "/bmi <вес> <рост> - Рассчитать индекс массы тела\n"
        "/water <вода_в_литрах> - Напоминание о количестве выпитой воды\n"
        "/exercise <тип> - Рекомендации по упражнениям (кардио, силовые, растяжка)\n"
        "/recipe <блюдо> - Получить рецепт здорового блюда\n"
        "/quote - Получить мотивационную цитату\n"
        "/image - Получить изображение с полезными советами\n"
    )
    await update.message.reply_text(help_text)


async def bmi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Используйте: /bmi <вес в кг> <рост в см>")
        return

    try:
        weight = float(context.args[0])
        height = float(context.args[1]) / 100
        bmi_value = weight / (height ** 2)
        await update.message.reply_text(f"Ваш индекс массы тела (BMI): {bmi_value:.2f}")
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите корректные числовые значения.")


async def water(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Используйте: /water <вода в литрах>")
        return

    try:
        water_intake = float(context.args[0])
        await update.message.reply_text(f"Вы выпили {water_intake} литров воды сегодня. Отлично!")
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите корректное числовое значение.")


async def exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Используйте: /exercise <тип>")
        return

    exercise_type = context.args[0].lower()
    exercises = {
        "кардио": ["Бег", "Велосипед", "Плавание"],
        "силовые": ["Жим лежа", "Приседания", "Становая тяга"],
        "растяжка": ["Наклоны", "Повороты", "Упражнения на гибкость"]
    }

    if exercise_type in exercises:
        await update.message.reply_text(
            f"Рекомендуемые упражнения для {exercise_type}: {', '.join(exercises[exercise_type])}")
    else:
        await update.message.reply_text("Типы упражнений: кардио, силовые, растяжка.")

async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Используйте: /recipe <блюдо>")
        return

    recipes = {
        "салат": "Смешайте листья салата, помидоры, огурцы и заправьте оливковым маслом.",
        "овсянка": "Сварите овсянку на воде или молоке и добавьте фрукты.",
        "курица": "Запеките куриную грудку с пряностями и овощами."
    }

    dish = context.args[0].lower()
    if dish in recipes:
        await update.message.reply_text(f"Рецепт для {dish}: {recipes[dish]}")
    else:
        await update.message.reply_text("Извините, рецепт не найден.")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "Здоровье — это богатство.",
        "Ваше тело — это ваш храм.",
        "Заботьтесь о своем теле, это единственное место, где вам жить."
    ]
    await update.message.reply_text(random.choice(quotes))

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url = 'https://avatars.mds.yandex.net/i?id=46b98a8d8740f0f0f63969d5e7eec4e0af8668cc-4146488-images-thumbs&n=13'  # Замените на URL вашего изображения
    await update.message.reply_photo(photo=image_url)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7661683102:AAGDqRYrcP4R2ECRSOwvYkFiKUaOrYD2JRM').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("bmi", bmi))
    application.add_handler(CommandHandler("water", water))
    application.add_handler(CommandHandler("exercise", exercise))
    application.add_handler(CommandHandler("recipe", recipe))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("image", send_image))

    application.run_polling()