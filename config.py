import os


# Путь до папки с проектом
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TEST_DATA_DIR = os.path.join(BASE_PATH, "testData")

#Базовый урл тестируемого приложения
BASE_URL_OFL = 'http://localhost:8000/'

#Данные для подключения к БД
DB_CONCTIONS_PARAMS = {
    "dbname": "online-wallet-fake",
    "host": "localhost",
    "user": "postgres",
    "password": "postgres"
}
