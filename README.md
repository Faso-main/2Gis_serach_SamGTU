# Парсер магазинов из 2GIS

Скрипт для сбора данных о лодочных магазинах из 2GIS API с сохранением в Excel/CSV.

## Функционал
- Поиск по нескольким запросам
- Сбор контактов (телефоны, сайты, email)
- Автоматическое удаление дубликатов
- Сохранение в Excel и CSV
- Прогресс-бар обработки

## Полная установка

### 1. Установка Visual Studio Code
1. Скачайте VSCode с [официального сайта](https://code.visualstudio.com/)
2. Запустите установщик и следуйте инструкциям
3. После установки откройте VSCode и установите расширения:
   - **Python** (от Microsoft)
   ```bash
   # Альтернативно через командную строку:
   code --install-extension ms-python.python
   code --install-extension ms-python.vscode-pylance
   ```

### 2. Установка Python
1. Скачайте Python 3.11+ с [python.org](https://www.python.org/downloads/)
2. При установке отметьте галочки:
   - ☑ Add Python to PATH
   - ☑ Install pip

3. Проверьте установку:
   ```bash
   python --version
   pip --version
   ```

### 3. Настройка проекта
1. Откройте папку проекта в VSCode:
   ```bash
   code /путь/к/папке/проекта
   ```

2. Активируйте его:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Настройка API 2GIS
1. Зарегистрируйтесь на [2GIS API](https://dev.2gis.ru/)
2. Получите ключ в разделе "Мои приложения"
3. В файле `main.py` замените:
   ```python
   API_KEY = "YOUR_API_KEY"  # ← Вставьте ваш ключ здесь
   ```

## Использование
1. Настройте параметры поиска в `main.py`:
   ```python
   queries = [
       "лодочные моторы",
       "ПВХ лодки",
       "запчасти для лодок"
   ]
   ```

2. Запустите скрипт#   2 G i s _ s e r a c h _ S a m G T U  
 