# config.py

# Токен для доступа к боту и URL Jenkins
TOKEN = '7117726988:AAFJFXz3rF7XyNXK23vtcy6MQG1E9x3DmRc' # Тоек телеграмма
JENKINS_URL = 'http://192.168.9.152:8085' # Адресс jenkins
JENKINS_USER = 'daniil' # Логин jenkins
JENKINS_API_TOKEN = '112a3196a365e7c8f7563a10914b344791' # API jenkins
WATCH_FOLDER = r'D:\Identificators\log'  # Папка для мониторинга, в ней будет создан файл ConfigurationComparison.xlsx
EXCEL_SCRIPT_PATH = r'D:\HelixRep\BOT\excel_in_png.py'  # Путь к скрипту (excel_in_png.py)
SPECIAL_CHAT_ID = '-1002167629740'  # Замените на ID чата

# Словарь для сопоставления кнопок с именами Jenkins задач
jenkins_jobs = {
    'Сверка идентификаторов': {
        'IDENTIFICATOR FITNESS': 'IDENTIFICATOR FITNESS',
        'IDENTIFICATOR STOMA': 'IDENTIFICATOR STOMA',
        'IDENTIFICATOR SALON': 'IDENTIFICATOR SALON'
    }
}



# Пути к директориям, которые нужно очистить
rab_directory = r"D:\Identificators\Rab"
rel_directory = r"D:\Identificators\Relis"