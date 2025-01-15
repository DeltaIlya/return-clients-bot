import multiprocessing
import os

# Запуск Telegram-бота
def run_bot():
    os.system("python bot.py")

# Запуск Dash-дэшборда
def run_dashboard():
    os.system("python dashboard.py")

if __name__ == '__main__':
    # Создаем процессы для бота и дэшборда
    bot_process = multiprocessing.Process(target=run_bot)
    dash_process = multiprocessing.Process(target=run_dashboard)

    # Запускаем процессы
    bot_process.start()
    dash_process.start()

    # Ожидаем завершения обоих процессов
    bot_process.join()
    dash_process.join()
