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
from pathlib import Path

# Загружаем переменные окружения
load_dotenv()
api = os.getenv('YOUR_TOKEN')

# Инициализируем бота и хранилище
bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Подключаем БД в папке bot
db_path = Path(__file__).parent / 'users.db'  # Путь к БД в папке с ботом
conn = sqlite3.connect(db_path, check_same_thread=False)
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

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_skin_problems (
        user_id INTEGER PRIMARY KEY,
        allergy INTEGER DEFAULT 0,
        acne INTEGER DEFAULT 0,
        dermatitis INTEGER DEFAULT 0,
        peeling INTEGER DEFAULT 0,
        itching INTEGER DEFAULT 0,
        burning INTEGER DEFAULT 0,
        dryness INTEGER DEFAULT 0,
        pigmentation INTEGER DEFAULT 0,
        no_problems INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_reactive_brands (
        user_id INTEGER PRIMARY KEY,
        loreal INTEGER DEFAULT 0,
        maybelline INTEGER DEFAULT 0,
        nivea INTEGER DEFAULT 0,
        garnier INTEGER DEFAULT 0,
        chanel INTEGER DEFAULT 0,
        dior INTEGER DEFAULT 0,
        esteelauder INTEGER DEFAULT 0,
        lancome INTEGER DEFAULT 0,
        lrp INTEGER DEFAULT 0,
        vichy INTEGER DEFAULT 0,
        natura INTEGER DEFAULT 0,
        blackpearl INTEGER DEFAULT 0,
        other_brand INTEGER DEFAULT 0,
        other_brand_text TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_allergens (
        user_id INTEGER PRIMARY KEY,
        parabens INTEGER DEFAULT 0,
        fragrances INTEGER DEFAULT 0,
        dyes INTEGER DEFAULT 0,
        sulfates INTEGER DEFAULT 0,
        essential_oils INTEGER DEFAULT 0,
        alcohol INTEGER DEFAULT 0,
        photosensitizers INTEGER DEFAULT 0,
        preservatives INTEGER DEFAULT 0,
        proteins INTEGER DEFAULT 0,
        bee_products INTEGER DEFAULT 0,
        other_allergen INTEGER DEFAULT 0,
        other_allergen_text TEXT,
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
            web_app=WebAppInfo(url="https://cosmetic-telegram-mini-app.onrender.com/registration")
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
                "Telegram-каналы✅" if "choice3" in selected_sources else "Telegram-каналы",
                callback_data="source_choice3"
            ),
            InlineKeyboardButton(
                "Обзоры на YouTube✅" if "choice4" in selected_sources else "Обзоры на YouTube",
                callback_data="source_choice4"
            )
        ],
        [
            InlineKeyboardButton(
                "Reddit✅" if "choice5" in selected_sources else "Reddit",
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


def get_skin_problems_keyboard(selected_problems=None):
    if selected_problems is None:
        selected_problems = []

    buttons = [
        [
            InlineKeyboardButton(
                "Аллергия✅" if "allergy" in selected_problems else "Аллергия",
                callback_data="skin_allergy"
            ),
            InlineKeyboardButton(
                "Акне✅" if "acne" in selected_problems else "Акне",
                callback_data="skin_acne"
            )
        ],
        [
            InlineKeyboardButton(
                "Дерматит✅" if "dermatitis" in selected_problems else "Дерматит",
                callback_data="skin_dermatitis"
            ),
            InlineKeyboardButton(
                "Шелушение кожи✅" if "peeling" in selected_problems else "Шелушение кожи",
                callback_data="skin_peeling"
            )
        ],
        [
            InlineKeyboardButton(
                "Зуд✅" if "itching" in selected_problems else "Зуд",
                callback_data="skin_itching"
            ),
            InlineKeyboardButton(
                "Жжение✅" if "burning" in selected_problems else "Жжение",
                callback_data="skin_burning"
            )
        ],
        [
            InlineKeyboardButton(
                "Сухость✅" if "dryness" in selected_problems else "Сухость",
                callback_data="skin_dryness"
            ),
            InlineKeyboardButton(
                "Пигментация✅" if "pigmentation" in selected_problems else "Пигментация",
                callback_data="skin_pigmentation"
            )
        ],
        [
            InlineKeyboardButton(
                "Ничего из перечисленного✅" if "no_problems" in selected_problems else "Ничего из перечисленного",
                callback_data="skin_no_problems"
            )
        ],
        [
            InlineKeyboardButton("Продолжить", callback_data="skin_continue")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_reactive_brands_keyboard(selected_brands=None, other_filled=False):
    if selected_brands is None:
        selected_brands = []

    buttons = [
        [
            InlineKeyboardButton(
                "L'Oréal Paris✅" if "loreal" in selected_brands else "L'Oréal Paris",
                callback_data="brand_loreal"
            ),
            InlineKeyboardButton(
                "Maybelline✅" if "maybelline" in selected_brands else "Maybelline",
                callback_data="brand_maybelline"
            )
        ],
        [
            InlineKeyboardButton(
                "Nivea✅" if "nivea" in selected_brands else "Nivea",
                callback_data="brand_nivea"
            ),
            InlineKeyboardButton(
                "Garnier✅" if "garnier" in selected_brands else "Garnier",
                callback_data="brand_garnier"
            )
        ],
        [
            InlineKeyboardButton(
                "Chanel✅" if "chanel" in selected_brands else "Chanel",
                callback_data="brand_chanel"
            ),
            InlineKeyboardButton(
                "Dior✅" if "dior" in selected_brands else "Dior",
                callback_data="brand_dior"
            )
        ],
        [
            InlineKeyboardButton(
                "Estée Lauder✅" if "esteelauder" in selected_brands else "Estée Lauder",
                callback_data="brand_esteelauder"
            ),
            InlineKeyboardButton(
                "Lancôme✅" if "lancome" in selected_brands else "Lancôme",
                callback_data="brand_lancome"
            )
        ],
        [
            InlineKeyboardButton(
                "La Roche-Posay✅" if "lrp" in selected_brands else "La Roche-Posay",
                callback_data="brand_lrp"
            ),
            InlineKeyboardButton(
                "Vichy✅" if "vichy" in selected_brands else "Vichy",
                callback_data="brand_vichy"
            )
        ],
        [
            InlineKeyboardButton(
                "Natura Siberica✅" if "natura" in selected_brands else "Natura Siberica",
                callback_data="brand_natura"
            ),
            InlineKeyboardButton(
                "Черный Жемчуг✅" if "blackpearl" in selected_brands else "Черный Жемчуг",
                callback_data="brand_blackpearl"
            )
        ],
        [
            InlineKeyboardButton(
                "Другое✅" if other_filled else "Другое",
                callback_data="brand_other" if not other_filled else "no_action"
            )
        ],
        [
            InlineKeyboardButton("Продолжить", callback_data="brand_continue")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_allergens_keyboard(selected_allergens=None, other_filled=False):
    if selected_allergens is None:
        selected_allergens = []

    buttons = [
        [
            InlineKeyboardButton(
                "Парабены✅" if "parabens" in selected_allergens else "Парабены",
                callback_data="allergen_parabens"
            ),
            InlineKeyboardButton(
                "Ароматизаторы✅" if "fragrances" in selected_allergens else "Ароматизаторы",
                callback_data="allergen_fragrances"
            )
        ],
        [
            InlineKeyboardButton(
                "Красители✅" if "dyes" in selected_allergens else "Красители",
                callback_data="allergen_dyes"
            ),
            InlineKeyboardButton(
                "Сульфаты✅" if "sulfates" in selected_allergens else "Сульфаты",
                callback_data="allergen_sulfates"
            )
        ],
        [
            InlineKeyboardButton(
                "Эфирные масла✅" if "essential_oils" in selected_allergens else "Эфирные масла",
                callback_data="allergen_essential_oils"
            ),
            InlineKeyboardButton(
                "Алкоголь✅" if "alcohol" in selected_allergens else "Алкоголь",
                callback_data="allergen_alcohol"
            )
        ],
        [
            InlineKeyboardButton(
                "Фотосенсибилизаторы✅" if "photosensitizers" in selected_allergens else "Фотосенсибилизаторы",
                callback_data="allergen_photosensitizers"
            ),
            InlineKeyboardButton(
                "Консерванты✅" if "preservatives" in selected_allergens else "Консерванты",
                callback_data="allergen_preservatives"
            )
        ],
        [
            InlineKeyboardButton(
                "Протеины✅" if "proteins" in selected_allergens else "Протеины",
                callback_data="allergen_proteins"
            ),
            InlineKeyboardButton(
                "Продукты пчеловодства✅" if "bee_products" in selected_allergens else "Продукты пчеловодства",
                callback_data="allergen_bee_products"
            )
        ],
        [
            InlineKeyboardButton(
                "Другое✅" if other_filled else "Другое",
                callback_data="allergen_other" if not other_filled else "no_action"
            )
        ],
        [
            InlineKeyboardButton("Продолжить", callback_data="allergen_continue")
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
    waiting_for_skin_problems = State()
    waiting_for_reactive_brands = State()
    waiting_for_other_brand_text = State()
    waiting_for_allergens = State()
    waiting_for_other_allergen_text = State()


# Обработчики
@dp.message_handler(commands=['start'])
async def starting(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        # Проверяем текущее состояние
        current_state = await state.get_state()
        if current_state:
            await state.finish()

        # Проверяем наличие пользователя в БД
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()

        if user:
            # Пользователь уже зарегистрирован
            await message.answer(
                f"👋 Привет, {message.from_user.full_name}!\n"
                "Ты уже зарегистрирован(а) в системе. "
                "Можешь проверить косметику на аллергены:",
                reply_markup=get_mini_app_keyboard()
            )

            # Проверяем, есть ли запись в таблице аллергенов
            cursor.execute("SELECT 1 FROM user_allergens WHERE user_id = ?", (user_id,))
            if not cursor.fetchone():
                cursor.execute("INSERT INTO user_allergens (user_id) VALUES (?)", (user_id,))
                conn.commit()

        else:
            # Новый пользователь
            await message.answer(
                "📝 Для доступа к сервису нам нужна ваша регистрация.\n"
                "Нажмите кнопку ниже, чтобы отправить номер телефона:",
                reply_markup=get_phone_keyboard()
            )
            await RegistrationStates.waiting_for_phone.set()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        await message.answer("⚠️ Произошла ошибка при работе с базой данных. Пожалуйста, попробуйте позже.")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        await message.answer("⚠️ Произошла непредвиденная ошибка. Пожалуйста, попробуйте еще раз.")


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegistrationStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    try:
        phone_number = message.contact.phone_number
        await state.update_data(phone=phone_number)
        await message.answer("📝 Теперь введите ваше Имя:", reply_markup=types.ReplyKeyboardRemove())
        await RegistrationStates.waiting_for_full_name.set()
    except Exception as e:
        print(f"Error in process_phone: {e}")
        await message.answer("⚠️ Произошла ошибка. Пожалуйста, попробуйте еще раз.")


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
    cursor.execute("INSERT INTO user_skin_problems (user_id) VALUES (?)", (user_id,))
    cursor.execute("INSERT INTO user_reactive_brands (user_id) VALUES (?)", (user_id,))
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

    button_names = {
        'friends': 'От знакомых',
        'ads': 'Реклама',
        'choice3': 'Telegram-каналы',
        'choice4': 'Обзоры на YouTube',
        'choice5': 'Reddit'
    }

    try:
        if source_type == "continue":
            # Проверяем, что хотя бы один источник выбран
            cursor.execute("SELECT from_friends, from_ads, choice3, choice4, choice5 FROM user_referral_sources WHERE user_id = ?", (user_id,))
            sources = cursor.fetchone()
            if not any(sources):
                await callback.answer("⚠️ Пожалуйста, выберите хотя бы один источник", show_alert=True)
                return

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

        # Получаем текущее состояние всех источников
        cursor.execute("""
            SELECT from_friends, from_ads, choice3, choice4, choice5
            FROM user_referral_sources WHERE user_id = ?
        """, (user_id,))
        sources = cursor.fetchone()

        if not sources:
            # Если почему-то нет записи, создаем новую
            cursor.execute("INSERT INTO user_referral_sources (user_id) VALUES (?)", (user_id,))
            conn.commit()
            sources = (0, 0, 0, 0, 0)

        # Определяем новый статус для выбранного источника
        current_index = list(column_mapping.keys()).index(source_type)
        current_state = sources[current_index]
        new_state = 0 if current_state else 1

        # Обновляем только нужный источник
        try:
            cursor.execute(f"""
                UPDATE user_referral_sources
                SET {db_column} = ?
                WHERE user_id = ?
            """, (new_state, user_id))
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Database error in process_referral_source: {e}")
            await callback.answer("⚠️ Ошибка базы данных. Попробуйте еще раз.", show_alert=True)
            return

        # Формируем список выбранных источников для клавиатуры
        selected = [
            key for key, idx in zip(column_mapping.keys(), range(5))
            if (sources[idx] if key != source_type else new_state)
        ]

        try:
            await callback.message.edit_reply_markup(
                reply_markup=get_referral_keyboard(selected))
        except Exception as e:
            print(f"Error editing reply markup: {e}")
            await callback.answer("⚠️ Ошибка обновления клавиатуры", show_alert=True)
            return

        action = "выбран" if new_state else "отменен"
        await callback.answer(f"Источник '{button_names.get(source_type)}' {action}")

    except Exception as e:
        print(f"Ошибка в process_referral_source: {str(e)}")
        await callback.answer("⚠️ Произошла ошибка. Пожалуйста, попробуйте еще раз.", show_alert=True)

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
            return

        if goal_type == "other":
            await callback.message.delete()
            msg = await callback.message.answer(
                "📝 Пожалуйста, укажите, с какой целью вы планируете использовать приложение:",
                reply_markup=types.ReplyKeyboardRemove()
            )
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

    async with state.proxy() as data:
        if 'goal_request_message' in data:
            try:
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=data['goal_request_message']
                )
            except:
                pass

    await message.delete()

    cursor.execute("""
        UPDATE user_goals
        SET other_goal = 1, other_goal_text = ?
        WHERE user_id = ?
    """, (other_text, user_id))
    conn.commit()

    confirm_msg = await message.answer("✅ Спасибо, Ваш ответ записан!")

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

    await message.answer(
        "🎯 С какой целью вы планируете использовать приложение?",
        reply_markup=get_goals_keyboard(selected, other_filled=True)
    )

    await asyncio.sleep(2)
    await confirm_msg.delete()

    await RegistrationStates.waiting_for_goal.set()


@dp.callback_query_handler(lambda c: c.data.startswith('skin_'), state=RegistrationStates.waiting_for_skin_problems)
async def process_skin_problems(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    action = callback.data

    if action == "skin_continue":
        await callback.message.edit_text("✅ Ваши ответы сохранены!")
        await callback.message.answer(
            "На какие бренды косметики уже была выявлена реакция?",
            reply_markup=get_reactive_brands_keyboard()
        )
        await RegistrationStates.waiting_for_reactive_brands.set()
        return

    if action == "skin_no_problems":
        cursor.execute("""
            UPDATE user_skin_problems
            SET allergy = 0, acne = 0, dermatitis = 0, peeling = 0,
                itching = 0, burning = 0, dryness = 0, pigmentation = 0,
                no_problems = 1
            WHERE user_id = ?
        """, (user_id,))
        conn.commit()
        await callback.answer("Выбрано: Ничего из перечисленного")
    else:
        problem_type = action.split('_')[1]
        column_mapping = {
            'allergy': 'allergy',
            'acne': 'acne',
            'dermatitis': 'dermatitis',
            'peeling': 'peeling',
            'itching': 'itching',
            'burning': 'burning',
            'dryness': 'dryness',
            'pigmentation': 'pigmentation'
        }

        if problem_type not in column_mapping:
            await callback.answer("Неизвестный вариант", show_alert=True)
            return

        cursor.execute("UPDATE user_skin_problems SET no_problems = 0 WHERE user_id = ?", (user_id,))
        db_column = column_mapping[problem_type]
        cursor.execute(f"SELECT {db_column} FROM user_skin_problems WHERE user_id = ?", (user_id,))
        current_state = cursor.fetchone()[0]
        new_state = 0 if current_state else 1

        cursor.execute(f"UPDATE user_skin_problems SET {db_column} = ? WHERE user_id = ?",
                       (new_state, user_id))
        conn.commit()

    cursor.execute("""
        SELECT allergy, acne, dermatitis, peeling, itching,
               burning, dryness, pigmentation, no_problems
        FROM user_skin_problems WHERE user_id = ?
    """, (user_id,))
    problems = cursor.fetchone()

    selected = []
    if problems[0]: selected.append("allergy")
    if problems[1]: selected.append("acne")
    if problems[2]: selected.append("dermatitis")
    if problems[3]: selected.append("peeling")
    if problems[4]: selected.append("itching")
    if problems[5]: selected.append("burning")
    if problems[6]: selected.append("dryness")
    if problems[7]: selected.append("pigmentation")
    if problems[8]: selected.append("no_problems")

    await callback.message.edit_reply_markup(
        reply_markup=get_skin_problems_keyboard(selected))


@dp.callback_query_handler(lambda c: c.data.startswith('brand_'), state=RegistrationStates.waiting_for_reactive_brands)
async def process_reactive_brands(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    brand_type = callback.data.split('_')[1]

    column_mapping = {
        'loreal': 'loreal',
        'maybelline': 'maybelline',
        'nivea': 'nivea',
        'garnier': 'garnier',
        'chanel': 'chanel',
        'dior': 'dior',
        'esteelauder': 'esteelauder',
        'lancome': 'lancome',
        'lrp': 'lrp',
        'vichy': 'vichy',
        'natura': 'natura',
        'blackpearl': 'blackpearl',
        'other': 'other_brand'
    }

    try:
        if brand_type == "continue":
            await callback.message.edit_text("✅ Ваши ответы сохранены!")
            cursor.execute("INSERT INTO user_allergens (user_id) VALUES (?)", (user_id,))
            conn.commit()
            await callback.message.answer(
                "На что была выявлена аллергия?",
                reply_markup=get_allergens_keyboard()
            )
            await RegistrationStates.waiting_for_allergens.set()
            return

        if brand_type == "no_action":
            await callback.answer()
            return

        if brand_type == "other":
            await callback.message.delete()
            msg = await callback.message.answer(
                "📝 Пожалуйста, укажите, на какие другие бренды у вас была реакция:",
                reply_markup=types.ReplyKeyboardRemove()
            )
            async with state.proxy() as data:
                data['brand_request_message'] = msg.message_id
            await RegistrationStates.waiting_for_other_brand_text.set()
            await callback.answer()
            return

        db_column = column_mapping.get(brand_type)
        if not db_column:
            await callback.answer("Неизвестный бренд", show_alert=True)
            return

        cursor.execute(f"SELECT {db_column} FROM user_reactive_brands WHERE user_id = ?", (user_id,))
        current_state = cursor.fetchone()[0]
        new_state = 0 if current_state else 1

        cursor.execute(f"UPDATE user_reactive_brands SET {db_column} = ? WHERE user_id = ?",
                       (new_state, user_id))
        conn.commit()

        await update_brands_keyboard(callback, user_id)

        button_names = {
            'loreal': "L'Oréal Paris",
            'maybelline': "Maybelline New York",
            'nivea': "Nivea",
            'garnier': "Garnier",
            'chanel': "Chanel",
            'dior': "Dior",
            'esteelauder': "Estée Lauder",
            'lancome': "Lancôme",
            'lrp': "La Roche-Posay",
            'vichy': "Vichy",
            'natura': "Natura Siberica",
            'blackpearl': "Черный Жемчуг"
        }
        action = "выбран" if new_state else "отменен"
        await callback.answer(f"Бренд '{button_names.get(brand_type)}' {action}")

    except Exception as e:
        print(f"Ошибка: {e}")
        await callback.answer("⚠️ Ошибка. Попробуйте еще раз.", show_alert=True)


@dp.message_handler(state=RegistrationStates.waiting_for_other_brand_text)
async def process_other_brand_text(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    other_text = message.text

    async with state.proxy() as data:
        if 'brand_request_message' in data:
            try:
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=data['brand_request_message']
                )
            except:
                pass

    await message.delete()

    cursor.execute("""
        UPDATE user_reactive_brands
        SET other_brand = 1, other_brand_text = ?
        WHERE user_id = ?
    """, (other_text, user_id))
    conn.commit()

    confirm_msg = await message.answer("✅ Спасибо, Ваш ответ записан!")

    cursor.execute("""
        SELECT loreal, maybelline, nivea, garnier, chanel, dior,
               esteelauder, lancome, lrp, vichy, natura, blackpearl,
               other_brand
        FROM user_reactive_brands WHERE user_id = ?
    """, (user_id,))
    brands = cursor.fetchone()

    selected = []
    if brands[0]: selected.append("loreal")
    if brands[1]: selected.append("maybelline")
    if brands[2]: selected.append("nivea")
    if brands[3]: selected.append("garnier")
    if brands[4]: selected.append("chanel")
    if brands[5]: selected.append("dior")
    if brands[6]: selected.append("esteelauder")
    if brands[7]: selected.append("lancome")
    if brands[8]: selected.append("lrp")
    if brands[9]: selected.append("vichy")
    if brands[10]: selected.append("natura")
    if brands[11]: selected.append("blackpearl")

    other_filled = brands[12] == 1

    await message.answer(
        "На какие бренды косметики уже была выявлена реакция?",
        reply_markup=get_reactive_brands_keyboard(selected, other_filled)
    )

    await asyncio.sleep(2)
    await confirm_msg.delete()

    await RegistrationStates.waiting_for_reactive_brands.set()


@dp.callback_query_handler(lambda c: c.data.startswith('allergen_'), state=RegistrationStates.waiting_for_allergens)
async def process_allergens(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    allergen_type = callback.data.split('_')[1]

    column_mapping = {
        'parabens': 'parabens',
        'fragrances': 'fragrances',
        'dyes': 'dyes',
        'sulfates': 'sulfates',
        'essential': 'essential_oils',
        'alcohol': 'alcohol',
        'photosensitizers': 'photosensitizers',
        'preservatives': 'preservatives',
        'proteins': 'proteins',
        'bee': 'bee_products',
        'other': 'other_allergen'
    }

    try:
        # Проверяем и создаем запись в таблице аллергенов, если ее нет
        cursor.execute("SELECT 1 FROM user_allergens WHERE user_id = ?", (user_id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO user_allergens (user_id) VALUES (?)", (user_id,))
            conn.commit()

        if allergen_type == "continue":
            # Проверяем, что хотя бы один аллерген выбран
            cursor.execute("""
                SELECT parabens, fragrances, dyes, sulfates, essential_oils,
                       alcohol, photosensitizers, preservatives, proteins,
                       bee_products, other_allergen
                FROM user_allergens WHERE user_id = ?
            """, (user_id,))
            allergens = cursor.fetchone()

            if not any(allergens):
                await callback.answer("⚠️ Пожалуйста, выберите хотя бы один аллерген", show_alert=True)
                return

            await callback.message.edit_text("✅ Ваши ответы сохранены!")
            await finalize_registration(callback, user_id)
            await state.finish()
            return

        if allergen_type == "no_action":
            await callback.answer()
            return

        if allergen_type == "other":
            await callback.message.delete()
            msg = await callback.message.answer(
                "📝 Пожалуйста, укажите, на какие другие аллергены у вас была реакция:",
                reply_markup=types.ReplyKeyboardRemove()
            )
            async with state.proxy() as data:
                data['allergen_request_message'] = msg.message_id
            await RegistrationStates.waiting_for_other_allergen_text.set()
            await callback.answer()
            return

        db_column = column_mapping.get(allergen_type)
        if not db_column:
            await callback.answer("Неизвестный аллерген", show_alert=True)
            return

        cursor.execute(f"SELECT {db_column} FROM user_allergens WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        current_state = result[0] if result else 0
        new_state = 0 if current_state else 1

        cursor.execute(f"UPDATE user_allergens SET {db_column} = ? WHERE user_id = ?",
                     (new_state, user_id))
        conn.commit()

        await update_allergens_keyboard(callback, user_id)

        button_names = {
            'parabens': 'Парабены',
            'fragrances': 'Ароматизаторы',
            'dyes': 'Красители',
            'sulfates': 'Сульфаты',
            'essential': 'Эфирные масла',
            'alcohol': 'Алкоголь',
            'photosensitizers': 'Фотосенсибилизаторы',
            'preservatives': 'Консерванты',
            'proteins': 'Протеины',
            'bee': 'Продукты пчеловодства'
        }
        action = "выбран" if new_state else "отменен"
        await callback.answer(f"Аллерген '{button_names.get(allergen_type)}' {action}")

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        await callback.answer("⚠️ Ошибка базы данных. Попробуйте еще раз.", show_alert=True)
    except Exception as e:
        print(f"Ошибка: {e}")
        await callback.answer("⚠️ Ошибка. Попробуйте еще раз.", show_alert=True)


@dp.message_handler(state=RegistrationStates.waiting_for_other_allergen_text)
async def process_other_allergen_text(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    other_text = message.text

    async with state.proxy() as data:
        if 'allergen_request_message' in data:
            try:
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=data['allergen_request_message']
                )
            except:
                pass

    await message.delete()

    cursor.execute("""
        UPDATE user_allergens
        SET other_allergen = 1, other_allergen_text = ?
        WHERE user_id = ?
    """, (other_text, user_id))
    conn.commit()

    confirm_msg = await message.answer("✅ Спасибо, Ваш ответ записан!")

    cursor.execute("""
        SELECT parabens, fragrances, dyes, sulfates, essential_oils,
               alcohol, photosensitizers, preservatives, proteins,
               bee_products, other_allergen
        FROM user_allergens WHERE user_id = ?
    """, (user_id,))
    allergens = cursor.fetchone()

    selected = []
    if allergens[0]: selected.append("parabens")
    if allergens[1]: selected.append("fragrances")
    if allergens[2]: selected.append("dyes")
    if allergens[3]: selected.append("sulfates")
    if allergens[4]: selected.append("essential_oils")
    if allergens[5]: selected.append("alcohol")
    if allergens[6]: selected.append("photosensitizers")
    if allergens[7]: selected.append("preservatives")
    if allergens[8]: selected.append("proteins")
    if allergens[9]: selected.append("bee_products")

    other_filled = allergens[10] == 1

    await message.answer(
        "На что была выявлена аллергия?",
        reply_markup=get_allergens_keyboard(selected, other_filled)
    )

    await asyncio.sleep(2)
    await confirm_msg.delete()

    await RegistrationStates.waiting_for_allergens.set()


async def update_allergens_keyboard(callback: types.CallbackQuery, user_id: int):
    cursor.execute("""
        SELECT parabens, fragrances, dyes, sulfates, essential_oils,
               alcohol, photosensitizers, preservatives, proteins,
               bee_products, other_allergen, other_allergen_text
        FROM user_allergens WHERE user_id = ?
    """, (user_id,))
    allergens = cursor.fetchone()

    selected = []
    if allergens[0]: selected.append("parabens")
    if allergens[1]: selected.append("fragrances")
    if allergens[2]: selected.append("dyes")
    if allergens[3]: selected.append("sulfates")
    if allergens[4]: selected.append("essential_oils")
    if allergens[5]: selected.append("alcohol")
    if allergens[6]: selected.append("photosensitizers")
    if allergens[7]: selected.append("preservatives")
    if allergens[8]: selected.append("proteins")
    if allergens[9]: selected.append("bee_products")

    other_filled = allergens[10] == 1 and allergens[11] is not None

    await callback.message.edit_reply_markup(
        reply_markup=get_allergens_keyboard(selected, other_filled))


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


async def update_brands_keyboard(callback: types.CallbackQuery, user_id: int):
    cursor.execute("""
        SELECT loreal, maybelline, nivea, garnier, chanel, dior,
               esteelauder, lancome, lrp, vichy, natura, blackpearl,
               other_brand, other_brand_text
        FROM user_reactive_brands WHERE user_id = ?
    """, (user_id,))
    brands = cursor.fetchone()

    selected = []
    if brands[0]: selected.append("loreal")
    if brands[1]: selected.append("maybelline")
    if brands[2]: selected.append("nivea")
    if brands[3]: selected.append("garnier")
    if brands[4]: selected.append("chanel")
    if brands[5]: selected.append("dior")
    if brands[6]: selected.append("esteelauder")
    if brands[7]: selected.append("lancome")
    if brands[8]: selected.append("lrp")
    if brands[9]: selected.append("vichy")
    if brands[10]: selected.append("natura")
    if brands[11]: selected.append("blackpearl")

    other_filled = brands[12] == 1 and brands[13] is not None

    await callback.message.edit_reply_markup(
        reply_markup=get_reactive_brands_keyboard(selected, other_filled))


async def finish_registration(callback: types.CallbackQuery, user_id: int):
    await callback.message.answer(
        "Что из перечисленного у вас уже было?",
        reply_markup=get_skin_problems_keyboard()
    )
    await RegistrationStates.waiting_for_skin_problems.set()


async def finalize_registration(callback: types.CallbackQuery, user_id: int):
    await callback.message.answer(
        "✅ Регистрация полностью завершена!\n"
        "Теперь вы можете проверить косметику на аллергены, нажав кнопку ниже:",
        reply_markup=get_mini_app_keyboard()
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)