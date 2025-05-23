# 🤖 Шаблон для разработки Telegram-ботов на Aiogram3 для новичков

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green.svg)](https://docs.aiogram.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Шаблон, имеющий правильную архитектуру и учитывающий современные паттерны разработки


## 🌟 Особенности

- ✅ Правильная система запросов к БД (CRUD)
- ✅ Готовая проверка на админа
- ✅ Правильное раздление логики между файлами
- ✅ Работа с магическим фильтром

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10+
- Telegram Bot Token (получить у [@BotFather](https://t.me/BotFather))

### Установка
```bash
# Клонировать репозиторий
git clone https://github.com/AndreySmolev/Newbie-Template-Aiogram.git
cd ваш-репозиторий

# Установить зависимости
pip install -r requirements.txt
cd src
python3 main.py
```

⚠️ Перед запуском заполните данные в .env

## Предупреждение
В качестве базы данных используется SQLite — это отличный выбор для начинающих, так как она не требует настройки сервера и идеально подходит для небольших проектов: телеграм-ботов, локальных приложений и прототипирования. Однако важно учитывать ограничения SQLite: при высокой нагрузке с множеством одновременных запросов возможны блокировки, что в критических случаях может потребовать перезапуска бота, поэтому для полноценных проектов используйте MySQL, PostgreSQL и другие "полноценные" базы данных
