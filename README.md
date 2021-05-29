# digital_calls
Проект API для списка звонков по тестовому заданию.

### Для развертывания проекта локально выполнить:
 ```
 mkdir digital_test
 cd digital_test
 git init
 git pull https://github.com/warrinot/digital_testing.git
 pip install virtualenv
 python -m venv venv
 source venv/bin/activate //на Linux или "venv\scripts\activate" на Windows
 pip install -r requirements.txt
 python manage.py migrate
 python manage.py loaddata data.json
 
 python manage.py runserver
 ```
 
 ### .env файлы не скрыты намеренно
 
 ### Для развертывания проекта через докер выполнить:
  ```
 mkdir digital_test
 cd digital_test
 git init
 git pull https://github.com/warrinot/digital_testing.git
 docker-compose up --build
  ```
 
 Для логина использовать ahhi:123
 
 Документация к API:
 - /swagger.json /swagger.yaml - api specification
 - /swagger - Swagger docs
 - /redoc - Redoc docs
 
