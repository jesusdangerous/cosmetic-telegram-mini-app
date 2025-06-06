from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           WebAppInfo, InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
api = os.getenv('YOUR_TOKEN')

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Подключаем БД
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Создаем таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        phone TEXT,
        full_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_referral_sources (
        user_id INTEGER PRIMARY KEY,
        from_friends INTEGER DEFAULT 0,
        from_ads INTEGER DEFAULT 0,
        choice3 INTEGER DEFAULT 0,
        choice4 INTEGER DEFAULT 0,
        choice5 INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_goals (
        user_id INTEGER PRIMARY KEY,
        analyze_compositions INTEGER DEFAULT 0,
        healthy_lifestyle INTEGER DEFAULT 0,
        expert_communication INTEGER DEFAULT 0,
        skin_improvement INTEGER DEFAULT 0,
        compare_products INTEGER DEFAULT 0,
        other_goal INTEGER DEFAULT 0,
        other_goal_text TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')
conn.commit()


# Клавиатуры
def get_phone_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton("📱 Отправить номер телефона", request_contact=True)
    )


def get_mini_app_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(
            text="🔍 Проверить косметику на аллергены",
            web_app=WebAppInfo(url="https://наш-mini-app-сайт.com")
        )
    )


def get_referral_keyboard(selected_sources=None):
    if selected_sources is None:
        selected_sources = []

    buttons = [
        [
            InlineKeyboardButton(
                "От знакомых✅" if "friends" in selected_sources else "От знакомых",
                callback_data="source_friends"
            ),
            InlineKeyboardButton(
                "Реклама✅" if "ads" in selected_sources else "Реклама",
                callback_data="source_ads"
            )
        ],
        [
            InlineKeyboardButton(
                "Выбор 3✅" if "choice3" in selected_sources else "Выбор 3",
                callback_data="source_choice3"
            ),
            InlineKeyboardButton(
                "Выбор 4✅" if "choice4" in selected_sources else "Выбор 4",
                callback_data="source_choice4"
            )
        ],
        [
            InlineKeyboardButton(
                "Выбор 5✅" if "choice5" in selected_sources else "Выбор 5",
                callback_data="source_choice5"
            )
        ],
        [
            InlineKeyboardButton("Продолжить", callback_data="source_continue")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_goals_keyboard(selected_goals=None, other_filled=False):
    if selected_goals is None:
        selected_goals = []

    buttons = [
        [
            InlineKeyboardButton(
                "Анализ составов✅" if "analyze" in selected_goals else "Анализ составов",
                callback_data="goal_analyze"
            ),
            InlineKeyboardButton(
                "ЗОЖ✅" if "healthy" in selected_goals else "ЗОЖ",
                callback_data="goal_healthy"
            )
        ],
        [
            InlineKeyboardButton(
                "Общение с экспертом✅" if "expert" in selected_goals else "Общение с экспертом",
                callback_data="goal_expert"
            ),
            InlineKeyboardButton(
                "Улучшение кожи✅" if "skin" in selected_goals else "Улучшение кожи",
                callback_data="goal_skin"
            )
        ],
        [
            InlineKeyboardButton(
                "Сравнение составов✅" if "compare" in selected_goals else "Сравнение составов",
                callback_data="goal_compare"
            ),
            InlineKeyboardButton(
                "Другое✅" if other_filled else "Другое",
                callback_data="goal_other" if not other_filled else "no_action"
            )
        ],
        [
            InlineKeyboardButton("Продолжить", callback_data="goal_continue")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


# Состояния регистрации
class RegistrationStates(StatesGroup):
    waiting_for_phone = State()
    waiting_for_full_name = State()
    waiting_for_referral_source = State()
    waiting_for_goal = State()
    waiting_for_other_goal_text = State()


# Обработчики
@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    if user:
        await message.answer(
            f"👋 Привет, {message.from_user.full_name}!\n"
            "Ты уже зарегистрирован(а) в системе. "
            "Можешь проверить косметику на аллергены:",
            reply_markup=get_mini_app_keyboard()
        )
    else:
        await message.answer(
            "📝 Для доступа к сервису нам нужна ваша регистрация.\n"
            "Нажмите кнопку ниже, чтобы отправить номер телефона:",
            reply_markup=get_phone_keyboard()
        )
        await RegistrationStates.waiting_for_phone.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegistrationStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone=phone_number)
    await message.answer("📝 Теперь введите ваше ФИО:", reply_markup=types.ReplyKeyboardRemove())
    await RegistrationStates.waiting_for_full_name.set()


@dp.message_handler(state=RegistrationStates.waiting_for_full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    user_id = message.from_user.id
    data = await state.get_data()
    phone_number = data.get('phone')

    cursor.execute("INSERT INTO users (user_id, phone, full_name) VALUES (?, ?, ?)",
                   (user_id, phone_number, full_name))
    cursor.execute("INSERT INTO user_referral_sources (user_id) VALUES (?)", (user_id,))
    cursor.execute("INSERT INTO user_goals (user_id) VALUES (?)", (user_id,))
    conn.commit()

    await message.answer(
        "📢 Откуда Вы узнали про наш сервис?",
        reply_markup=get_referral_keyboard()
    )
    await RegistrationStates.waiting_for_referral_source.set()


@dp.callback_query_handler(lambda c: c.data.startswith('source_'), state=RegistrationStates.waiting_for_referral_source)
async def process_referral_source(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    source_type = callback.data.split('_')[1]

    column_mapping = {
        'friends': 'from_friends',
        'ads': 'from_ads',
        'choice3': 'choice3',
        'choice4': 'choice4',
        'choice5': 'choice5'
    }

    try:
        if source_type == "continue":
            await callback.message.edit_text("✅ Источники сохранены!")
            await callback.message.answer(
                "🎯 С какой целью вы планируете использовать приложение?",
                reply_markup=get_goals_keyboard()
            )
            await RegistrationStates.waiting_for_goal.set()
            await callback.answer()
            return

        db_column = column_mapping.get(source_type)
        if not db_column:
            await callback.answer("Неизвестный источник", show_alert=True)
            return

        cursor.execute(f"SELECT {db_column} FROM user_referral_sources WHERE user_id = ?", (user_id,))
        current_state = cursor.fetchone()[0]
        new_state = 0 if current_state else 1

        cursor.execute(f"UPDATE user_referral_sources SET {db_column} = ? WHERE user_id = ?",
                       (new_state, user_id))
        conn.commit()

        cursor.execute("""
            SELECT from_friends, from_ads, choice3, choice4, choice5 
            FROM user_referral_sources WHERE user_id = ?
        """, (user_id,))
        sources = cursor.fetchone()
        selected = []
        if sources[0]: selected.append("friends")
        if sources[1]: selected.append("ads")
        if sources[2]: selected.append("choice3")
        if sources[3]: selected.append("choice4")
        if sources[4]: selected.append("choice5")

        await callback.message.edit_reply_markup(
            reply_markup=get_referral_keyboard(selected))

        button_names = {
            'friends': 'От знакомых',
            'ads': 'Реклама',
            'choice3': 'Выбор 3',
            'choice4': 'Выбор 4',
            'choice5': 'Выбор 5'
        }
        action = "выбран" if new_state else "отменен"
        await callback.answer(f"Источник '{button_names.get(source_type, source_type)}' {action}")

    except Exception as e:
        print(f"Ошибка: {e}")
        await callback.answer("⚠️ Ошибка. Попробуйте еще раз.", show_alert=True)


@dp.callback_query_handler(lambda c: c.data.startswith('goal_'), state=RegistrationStates.waiting_for_goal)
async def process_goals(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    goal_type = callback.data.split('_')[1]

    if goal_type == "no_action":
        await callback.answer()
        return

    column_mapping = {
        'analyze': 'analyze_compositions',
        'healthy': 'healthy_lifestyle',
        'expert': 'expert_communication',
        'skin': 'skin_improvement',
        'compare': 'compare_products',
        'other': 'other_goal'
    }

    try:
        if goal_type == "continue":
            await callback.message.edit_text("✅ Ваши цели сохранены!")
            await finish_registration(callback, user_id)
            await state.finish()
            return

        if goal_type == "other":
            # Удаляем сообщение с целями
            await callback.message.delete()

            # Отправляем запрос текста цели
            msg = await callback.message.answer(
                "📝 Пожалуйста, укажите, с какой целью вы планируете использовать приложение:",
                reply_markup=types.ReplyKeyboardRemove()
            )

            # Сохраняем message_id запроса для последующего удаления
            async with state.proxy() as data:
                data['goal_request_message'] = msg.message_id

            await RegistrationStates.waiting_for_other_goal_text.set()
            await callback.answer()
            return

        db_column = column_mapping.get(goal_type)
        if not db_column:
            await callback.answer("Неизвестная цель", show_alert=True)
            return

        cursor.execute(f"SELECT {db_column} FROM user_goals WHERE user_id = ?", (user_id,))
        current_state = cursor.fetchone()[0]
        new_state = 0 if current_state else 1

        cursor.execute(f"UPDATE user_goals SET {db_column} = ? WHERE user_id = ?",
                       (new_state, user_id))
        conn.commit()

        await update_goals_keyboard(callback, user_id)

        button_names = {
            'analyze': 'Анализ составов',
            'healthy': 'ЗОЖ',
            'expert': 'Общение с экспертом',
            'skin': 'Улучшение кожи',
            'compare': 'Сравнение составов'
        }
        action = "выбрана" if new_state else "отменена"
        await callback.answer(f"Цель '{button_names.get(goal_type)}' {action}")

    except Exception as e:
        print(f"Ошибка: {e}")
        await callback.answer("⚠️ Ошибка. Попробуйте еще раз.", show_alert=True)


@dp.message_handler(state=RegistrationStates.waiting_for_other_goal_text)
async def process_other_goal_text(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    other_text = message.text

    # Удаляем сообщение с запросом текста
    async with state.proxy() as data:
        if 'goal_request_message' in data:
            try:
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=data['goal_request_message']
                )
            except:
                pass

    # Удаляем сообщение пользователя с текстом
    await message.delete()

    # Записываем текст и отмечаем что "Другое" выбрано
    cursor.execute("""
        UPDATE user_goals 
        SET other_goal = 1, other_goal_text = ?
        WHERE user_id = ?
    """, (other_text, user_id))
    conn.commit()

    # Отправляем подтверждение
    confirm_msg = await message.answer("✅ Спасибо, Ваш ответ записан!")

    # Получаем текущие выбранные цели для обновления клавиатуры
    cursor.execute("""
        SELECT analyze_compositions, healthy_lifestyle, expert_communication,
               skin_improvement, compare_products, other_goal
        FROM user_goals WHERE user_id = ?
    """, (user_id,))
    goals = cursor.fetchone()

    selected = []
    if goals[0]: selected.append("analyze")
    if goals[1]: selected.append("healthy")
    if goals[2]: selected.append("expert")
    if goals[3]: selected.append("skin")
    if goals[4]: selected.append("compare")

    # Отправляем обновлённую клавиатуру целей
    await message.answer(
        "🎯 С какой целью вы планируете использовать приложение?",
        reply_markup=get_goals_keyboard(selected, other_filled=True)
    )

    # Удаляем подтверждение через 2 секунды
    await asyncio.sleep(2)
    await confirm_msg.delete()

    await RegistrationStates.waiting_for_goal.set()


async def update_goals_keyboard(callback: types.CallbackQuery, user_id: int):
    cursor.execute("""
        SELECT analyze_compositions, healthy_lifestyle, expert_communication,
               skin_improvement, compare_products, other_goal, other_goal_text
        FROM user_goals WHERE user_id = ?
    """, (user_id,))
    goals = cursor.fetchone()

    selected = []
    if goals[0]: selected.append("analyze")
    if goals[1]: selected.append("healthy")
    if goals[2]: selected.append("expert")
    if goals[3]: selected.append("skin")
    if goals[4]: selected.append("compare")

    other_filled = goals[5] == 1 and goals[6] is not None

    await callback.message.edit_reply_markup(
        reply_markup=get_goals_keyboard(selected, other_filled))


async def finish_registration(callback: types.CallbackQuery, user_id: int):
    await callback.message.answer(
        "✅ Регистрация завершена!\n"
        "Теперь вы можете проверить косметику на аллергены, нажав кнопку ниже:",
        reply_markup=get_mini_app_keyboard()
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)