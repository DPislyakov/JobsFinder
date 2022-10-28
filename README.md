## JOBS FINDER

### Описание сервиса

Сервис для поиска работы.

### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Запуск uvicorn
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
### Локальный запуск с установкой докер-контейнера приложения
```bash
sudo docker build -t cgispro-weather-forecast:main . & sudo docker-compose up -d
```
### Локальное удаление существующего докер-контейнера приложения
```bash
sudo docker-compose down
```
### Ссылка на описание методов API
```bash
${YOUR_URL_ADDRESS}/docs
```