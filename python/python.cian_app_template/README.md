# Шаблон приложения для микросервисов

Чтобы создать новое приложение, установите [cookiecutter](https://github.com/audreyr/cookiecutter) и выполните что-то типа
```sh
$ cookiecutter git@bitbucket.org:cianmedia/python.cian_app_template.git
microservice_name [my-new-microservice]: my-new-microservice
short_description [My short description]: My short description
Select team:
    1 - audience
    2 - builders
    3 - commercial
    4 - countryside
    5 - happiness
    6 - homeowners
    7 - ml
    8 - online-marketing
    9 - platform
    10 - qa
    11 - spb
    12 - moderation
    13 - valuation
Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 [1]: <NUMBER>
python_package_name [my_new_microservice]: <ENTER>  # Обычно тут ни чего не надо менять
install_deps [y]: y
```
В случае если вашей команды нет в списке - обращайтесь в платформу

В результате появится папка `my-new-microservice` с вот такой структурой:
```
my-new-microservice
├── docker
│   └── etc
│       └── supervisor
│           └── conf.d
│               └── app.conf
├── src
│   └── my_new_microservice
│       ├── entities
│       │   └── __init__.py
│       ├── enums
│       │   └── __init__.py
│       ├── http
│       │   └── __init__.py
│       │   └── apis.py
│       ├── mappers
│       │   └── __init__.py
│       ├── queue
│       │   ├── __init__.py
│       │   └── producers.py
│       ├── repositories
│       │   └── __init__.py
│       ├── services
│       │   └── __init__.py
│       ├── settings
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── develop.py
│       │   └── production.py
│       ├── web
│       │   ├── __init__.py
│       │   ├── handlers.py
│       │   └── urls.py
│       ├── __init__.py
│       └── cli.py
├── tests
│   ├── web
│   │   ├── __init__.py
│   │   └── test_swagger.py
│   ├── __init__.py
│   ├── conftest.py
│   └── settings.py
├── .build.sh
├── .envrc.example
├── .gitignore
├── .pylintrc
├── app.toml
├── Dockerfile
├── MANIFEST.in
├── README.md
├── pytest.ini
├── Pipfile
├── Pipfile.lock
├── setup.cfg
├── setup.py
└── tox.ini
```

## Переменные окружения
Для дев настроек и других переменных окружения, нужных при разработке, можно использовать [direnv](https://github.com/direnv/direnv).
Пример конфига: .envrc.example

## Установка
```sh
pip install pipenv
pipenv install
pipenv install --dev

## ./[entities|enums]
Предметная область. Вся логика здесь чистая, без сайд-эффектов (общения с внешними сервисами). Такой подход облегчает моделирование, внесение изменений и написание тестов.

## ./[mappers|repositories|services]
Логика для работы с внешними хранилищами и прочими вещами, связанными с инфраструктурой. Примеры: прочитать данные из Кассандры, смапить их в объект предметной области, послать в какой-то другой микросервис по http.

## ./web
Http-сервер на основе Tornado. Хэндлеры лежат в `./web/handlers/`, мапятся на урлы в `./web/urls.py`.

## ./cli.py
Консольные команды. Запускается так:
```sh
$ my-new-microservice command_name --arg1=value1
```
