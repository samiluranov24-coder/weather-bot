import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "ТВОЙ_ТОКЕН"
API_KEY = "ТВОЙ_API_KEY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Мой город", request_location=True)],
        [KeyboardButton(text="🔍 Другой город")]
    ],
    resize_keyboard=True
)

# Функция "что надеть"
def get_advice(temp):
    if temp < 0:
        return "🥶 Очень холодно! Надень куртку, шапку и перчатки"
    elif temp < 10:
        return "🧥 Холодно, лучше надеть куртку"
    elif temp < 20:
        return "🧣 Прохладно, подойдёт кофта"
    elif temp < 30:
        return "👕 Тепло, можно в футболке"
    else:
        return "☀️ Жара! Надень что-то лёгкое"

# /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет!\n\nЯ бот погоды 🌦\nВыбери действие 👇",
        reply_markup=menu
    )

# /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "ℹ️ Как пользоваться:\n\n"
        "📍 Мой город — погода по геолокации\n"
        "🔍 Другой город — введи город вручную\n\n"
        "👗 Бот подскажет, что надеть"
    )

# Погода по геолокации
@dp.message(lambda message: message.location is not None)
async def weather_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    try:
        city = data["name"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]

        advice = get_advice(temp)

        await message.answer(
            f"🌍 {city}\n\n"
            f"🌡 {temp}°C\n"
            f"🤔 Ощущается: {feels}°C\n"
            f"☁️ {desc}\n\n"
            f"{advice}"
        )

    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

# Кнопка "другой город"
@dp.message(lambda message: message.text == "🔍 Другой город")
async def ask_city(message: types.Message):
    await message.answer("✏️ Напиши название города:")

# Погода по городу
@dp.message()
async def weather_city(message: types.Message):
    city = message.text

    if city == "📍 Мой город":
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    try:
        city_name = data["name"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]

        advice = get_advice(temp)

        await message.answer(
            f"🌍 {city_name}\n\n"
            f"🌡 {temp}°C\n"
            f"🤔 Ощущается: {feels}°C\n"
            f"☁️ {desc}\n\n"
            f"{advice}"
        )

    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
