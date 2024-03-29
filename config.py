from pathlib import Path

# Путь до папки с проектом
BASE_DIR = Path(__file__).resolve().parent

# Путь до папки с тестовыми данными
TEST_DATA_DIR = BASE_DIR / "testData"

#Базовый урл тестируемого приложения
BASE_URL_OFL = 'http://localhost:8000/'

#Данные для подключения к БД
DB_CONCTIONS_PARAMS = {
    "dbname": "online-wallet-fake",
    "host": "localhost",
    "user": "postgres",
    "password": "postgres"
}
