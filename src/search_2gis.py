import requests
import pandas as pd
import time
from tqdm import tqdm  

# Настройки
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
API_KEY = "YOUR_API_KEY"  
CITY = "Санкт-Петербург"
REGION_ID = 1  
OUTPUT_FILE = "2gis_лодочные_магазины.xlsx"

def search_2gis(query, city=CITY, pages=10):
    results = []
    print(f"\n🔍 Поиск по запросу: '{query}' в городе {city}")
    
    for page in tqdm(range(1, pages + 1), desc=f"Обработка страниц ({query})"):
        try:
            url = f"https://catalog.api.2gis.com/3.0/items?q={query}&region_id={REGION_ID}&page={page}&page_size=20&fields=items.point,items.contact_groups&key={API_KEY}"
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            data = response.json()

            for item in data.get("result", {}).get("items", []):
                # Основная информация
                name = item.get("name", "Не указано")
                address = item.get("address_name", "Не указано")
                
                # Контакты
                phones = []
                emails = []
                websites = []
                
                for group in item.get("contact_groups", []):
                    for contact in group.get("contacts", []):
                        if contact["type"] == "phone":
                            phones.append(contact.get("value", ""))
                        elif contact["type"] == "email":
                            emails.append(contact.get("value", ""))
                        elif contact["type"] == "website":
                            websites.append(contact.get("value", ""))

                results.append({
                    "Название": name,
                    "Адрес": address,
                    "Телефон": "; ".join(filter(None, phones)),
                    "Сайт": "; ".join(filter(None, websites)),
                    "Почта": "; ".join(filter(None, emails)),
                    "Город": city,
                    "Категория": query
                })

            time.sleep(0.5)  # Задержка между запросами

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе (страница {page}): {str(e)}")
            continue
        except Exception as e:
            print(f"Неожиданная ошибка (страница {page}): {str(e)}")
            continue

    return results

def main():
    queries = [
        "лодочные моторы",
        "ПВХ лодки",
        "запчасти для лодок",
        "магазин лодок",
        "судовые магазины"
    ]

    all_results = []
    for query in queries:
        all_results.extend(search_2gis(query, city=CITY, pages=10))

    # Создаем DataFrame и удаляем дубликаты
    df = pd.DataFrame(all_results)
    df.drop_duplicates(subset=["Название", "Адрес"], inplace=True)
    
    # Сохраняем в Excel
    try:
        with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Магазины')
        print(f"\nГотово! Данные сохранены в файл: {OUTPUT_FILE}")
        print(f"Найдено уникальных записей: {len(df)}")
    except Exception as e:
        print(f"Ошибка при сохранении в Excel: {str(e)}")
        # Альтернативное сохранение в CSV
        csv_file = OUTPUT_FILE.replace('.xlsx', '.csv')
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        print(f"Данные сохранены в CSV: {csv_file}")

if __name__ == "__main__":
    main()