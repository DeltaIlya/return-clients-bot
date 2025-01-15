# Бот по возвращению клиентов

## Описание
Этот проект представляет собой Telegram-бота, предназначенного для взаимодействия с клиентами, сбора их отзывов и оценки предложений. Кроме того, проект включает дашборд для анализа собранных данных.

---

## Установка
Для установки нужно скачать три файла zip-архив и распокавать его.

---

## Запуск
Чтобы запустить проект, нужно сделать:
1. Создать Телеграм-бота в BotFather и скопировать токен Вашего этого бота;
2. Откройте файл `bot.py` и в 15 строке, вместо **ВАШ ТОКЕН** вставте скопированным Вами токен;
3. Запустите файл `main.py` или введите в терлинал команду ```python main.py```
4. Чтобы

---

## Команды для Телеграм-бота
Используйте следующие команды в Telegram для взаимодействия с ботом:
- `/start` для начала диалога.
- `/report` для получения отчета.
- `/help` для справочной информации.
- `/send_proposal` для отправки предложений.
- `/dash` для получения ссылки на дашборд.

---

## Дашборд
- Дашборд доступен по адресу: `http://localhost:8050/` (или `http://localhost:8000/`, в зависимости от конфигурации).
- Он предоставляет визуализацию собранной информации о клиентах.
