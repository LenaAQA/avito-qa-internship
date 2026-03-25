# QA internship test assignment

API-тесты для сервиса объявлений https://qa-internship.avito.com/

---
## Полезные ссылки

1. [Техническое задание](https://github.com/avito-tech/tech-internship/blob/main/Tech%20Internships/QA/QA-trainee-assignment-spring-2026/QA-trainee-assignment-spring-2026.md)
2. CI / GitHub Actions Allure отчёт https://lenaaqa.github.io/avito-qa-internship/1/index.html

---
## Структура проекта

```
avito-qa-internship/
│
├── .github/
│   └── workflows/
│       └── test.yml              # CI (GitHub Actions)
│
├── clients/                      # API-клиенты и схемы
│   ├── advertisement/
│   │   ├── advertisement_client.py
│   │   └── advertisement_schema.py
│   └── statistics/
│       ├── statistic_client.py
│       └── statistics_schema.py
│
├── fixtures/                     # фикстуры (подготовка тестовых данных)
│   ├── advertisements.py
│   ├── statistics.py
│   └── allure.py
│
├── tests/                        # автотесты
│   ├── advertisement/
│   └── statistic/
│
├── tools/                        # вспомогательные утилиты
│   ├── allure/                   # работа с Allure
│   ├── assertions/               # кастомные проверки
│   └── http/                     # http-клиент, логирование, faker
│
├── BUGS.md                       # баги API
├── BUGS_TASK_1.md                # баги по скриншоту
├── TESTCASES.md                  # тест-кейсы
├── conftest.py                   # глобальные фикстуры
├── config.py                     # конфигурация
├── pytest.ini                    # настройки pytest
├── requirements.txt              # зависимости
└── README.md                     # описание проекта

```
## Установка и запуск 

### 1. Клонировать репозиторий

```
git clone https://github.com/LenaAQA/avito-qa-internship.git
cd avito-qa-internship
```

---

### 2. Создать виртуальное окружение

**Linux / macOS:**
```
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 3. Установить зависимости

```
pip install -r requirements.txt
```

---

### 4. Запуск тестов

```
pytest --alluredir=allure-results
```
> Требуется установленный Allure CLI: https://docs.qameta.io/allure/
> 
---

## Просмотр Allure отчёта

```
allure serve allure-results
```

## Линтинг и форматирование

**Форматирование:**
```
ruff format . --line-length=100
```

**Проверка:**
```
ruff check . --fix --line-length=100
```
