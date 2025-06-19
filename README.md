# Cosmetic Telegram Mini App

Spring Boot приложение для Telegram мини-приложения с интеграцией Vue.js фронтенда и aiogram для бота, которое позволяет пользователям анализировать состав косметических средств.

Приложение должно предоставляет подробный разбор ингредиентов, их назначение, потенциальные риски и, при необходимости, альтернативные рекомендации по выбору продукции.

## 📦 Технологии

### Backend
- Java 21
- Spring Boot 3.5.0
- Spring Web
- Spring Data JPA
- Spring Security
- Spring Mail
- PostgreSQL
- Lombok
- Jsoup

### Frontend
- Vue.js 3

### Другие компоненты
- Aiogram 2.25.2
- Docker
- Docker Compose

## Требования
- Java 21
- Maven 3.9
- Node.js 18
- Python 3.11
- Docker 20.10
- PostgreSQL 17

## 📂 Структура проекта

```
├── app/              # Java Spring Boot приложение
│   ├── src/
│   └── pom.xml
├── front/             # Vue.js приложение
│   ├── src/
│   └── vite.config.js
├── bot/                  # Aiogram бот
│   └── main.py
├── docker-compose.yml    # Docker Compose конфигурация
├── .env                  # Секреты и конфигурация
└── README.md             # Документация проекта
```
## 🚀 Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/jesusdangerous/cosmetic-telegram-mini-app.git
```

### 2. Настройка окружения

Создайте файл `.env` в корне проекта:

```env
# БД
POSTGRES_PASSWORD=your_strong_password
DB_HOST=postgres
DB_PORT=5432
DB_NAME=telegram_app
DB_USER=postgres

# Почта
MAIL_NAME=your_email@example.com
MAIL_PASSWORD=your_email_password
MAIL_ADMIN=admin@example.com

# API
DEEPSEEK_KEY=your_api_key_here
VITE_API_BASE_URL=http://localhost:8080

# Telegram
BOT_TOKEN=your_telegram_bot_token
```
> Замените значения переменных на свои собственные.

### 3. Разверните приложение на хостинге
- Используйте хостинг (Render, Vercel, Heroku)

### 4. Запуск телеграм бота

1. **Найдите BotFather** в Telegram:
- Откройте поиск в Telegram
- Введите `@BotFather`
- Выберите официального бота с синей галочкой

2. **Создайте нового бота**:
- /newbot

3. **Следуйте инструкциям**:
- Введите имя бота
- Введите username бота
- Получите токен
- Откройте настройки бота
- Выберите конфигурацию мини приложения
- Измените URL мини приложения на задеплоенное приложение

### 🐳 Запуск докера (развертывание локально)

```
docker-compose up --build
```

> Рекомендуется перед запуском отключить впн (так как почтовый сервер не сможет отправлять сообщения)

---

## 🛠 Полезные команды

```bash
# Остановить и удалить все контейнеры
docker-compose down

# Перезапустить backend с пересборкой
docker-compose up --build

# Перезапустить backend без пересборки
docker-compose up 
```