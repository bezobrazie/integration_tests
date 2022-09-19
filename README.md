# integration_tests
start DB and services
```sh
docker-compose -f docker-compose.online-wallet-fake.yml up
```
Перед выполнением docker-compose необходимо локально сбилдить image мокового хранилища
```sh
docker build -t storage-mock .
```
> http://localhost:8000/swagger/index.html \
> http://localhost:8000/api-docs/index.html