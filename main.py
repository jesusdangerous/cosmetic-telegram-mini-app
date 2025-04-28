from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv('YOUR_TOKEN')

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# БД
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        phone TEXT,
        full_name TEXT
    )
''')
conn.commit()

# Кнопка отправки номера телефона
def get_phone_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton("📱 Отправить номер телефона", request_contact=True))
    return keyboard

# Кнопка mini-app
def get_mini_app_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(
            text="🔍 Проверить косметику на аллергены",
            web_app=WebAppInfo(url="https://ваш-mini-app-сайт.com")  # Замените на реальный URL
        )
    )
    return keyboard

# Рега
class RegistrationStates(StatesGroup):
    waiting_for_phone = State()
    waiting_for_full_name = State()

# /start
@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    if user:
        # Рега есть
        await message.answer(
            f"👋 Привет, {message.from_user.full_name}!\n"
            "Ты уже зарегистрирован(а) в системе. "
            "Можешь проверить косметику на аллергены:",
            reply_markup=get_mini_app_keyboard()
        )
    else:
        # Рега новая
        await message.answer(
            "📝 Для доступа к сервису нам нужна ваша регистрация.\n"
            "Нажмите кнопку ниже, чтобы отправить номер телефона:",
            reply_markup=get_phone_keyboard()
        )
        await RegistrationStates.waiting_for_phone.set()  # Теперь ошибки не будет

# Обработчик номера телефона
@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegistrationStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone=phone_number)
    await message.answer("📝 Теперь введите ваше ФИО:", reply_markup=types.ReplyKeyboardRemove())
    await RegistrationStates.waiting_for_full_name.set()

# Обработчик ФИО
@dp.message_handler(state=RegistrationStates.waiting_for_full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    user_id = message.from_user.id
    data = await state.get_data()
    phone_number = data.get('phone')

    # Сохранение в бд
    cursor.execute("INSERT INTO users (user_id, phone, full_name) VALUES (?, ?, ?)", (user_id, phone_number, full_name))
    conn.commit()

    await message.answer(
        f"✅ Регистрация завершена!\n\n"
        f"Ваши данные:\n"
        f"📱 Телефон: {phone_number}\n"
        f"👤 ФИО: {full_name}\n\n"
        f"Теперь вы можете проверить косметику на аллергены:",
        reply_markup=get_mini_app_keyboard()
    )
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)