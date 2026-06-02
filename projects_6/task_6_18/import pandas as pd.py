import pandas as pd
from sqlalchemy import create_engine

# --- Пункт 1: Подключение к PostgreSQL ---
# Данные взяты из вашего docker-compose файла:
# Пользователь: postgres_task, Пароль: student, Порт: 5435, БД: student
db_url = 'postgresql://postgres_task:student@localhost:5435/student'

try:
    engine = create_engine(db_url)
    # Используем контекстный менеджер with, чтобы соединение закрылось автоматически
    with engine.connect() as connection:
        print("Успех: Соединение с PostgreSQL установлено корректно.\n")

        # --- Пункт 2: SQL-запрос с JOIN и загрузка в DataFrame ---
        query = """
        SELECT 
            pr.price, 
            p.name AS product_name, 
            p.category 
        FROM prices pr
        JOIN products p ON pr.product_id = p.id;
        """
        
        df = pd.read_sql(query, connection)
        
        print("Фрагмент загруженных данных:")
        print(df.head(), "\n")
        print("-" * 50)

        # --- Пункт 3: Расчет базовых статистик для цены ---
        price_mean = df['price'].mean()
        price_median = df['price'].median()
        price_std = df['price'].std()
        price_min = df['price'].min()
        price_max = df['price'].max()

        print("\nБазовые показатели цен:")
        print(f"Среднее значение:       {price_mean:,.2f} руб.")
        print(f"Медиана:                {price_median:,.2f} руб.")
        print(f"Стандартное отклонение: {price_std:,.2f} руб.")
        print(f"Минимальная цена:       {price_min:,.2f} руб.")
        print(f"Максимальная цена:      {price_max:,.2f} руб.\n")
        print("-" * 50)

        # --- Пункт 4: Квартили, IQR и фильтрация ---
        Q1 = df['price'].quantile(0.25)
        Q2 = df['price'].median()
        Q3 = df['price'].quantile(0.75)
        IQR = Q3 - Q1

        print(f"\nКвартили:")
        print(f"Q1 (25-й перцентиль):   {Q1:,.2f} руб.")
        print(f"Q2 (Медиана):           {Q2:,.2f} руб.")
        print(f"Q3 (75-й перцентиль):   {Q3:,.2f} руб.")
        print(f"Межквартильный размах (IQR): {IQR:,.2f} руб.\n")

        expensive_products = df[df['price'] > Q3][['product_name', 'category']].drop_duplicates()
        print("Товары с ценой выше Q3:")
        print(expensive_products.to_string(index=False), "\n")
        print("-" * 50)

        # --- Пункт 5: Группировка по категориям ---
        category_stats = df.groupby('category')['price'].agg(
            count='count',
            mean='mean',
            median='median',
            std='std'
        ).reset_index()

        category_stats = category_stats.sort_values(by='mean', ascending=False)

        print("\nСтатистика по категориям (отсортировано по средней цене):")
        print(category_stats.to_string(index=False, float_format="%.2f"), "\n")
        print("-" * 50)

        # --- Пункт 6: Разброс цен по товарам ---
        product_spread = df.groupby('product_name')['price'].agg(['min', 'max']).reset_index()
        product_spread['price_spread'] = product_spread['max'] - product_spread['min']
        
        top_5_spread = product_spread.sort_values(by='price_spread', ascending=False).head(5)

        print("\nТоп-5 товаров с наибольшим разбросом цен:")
        print(top_5_spread.to_string(index=False, float_format="%.2f"), "\n")

except Exception as e:
    print(f"Произошла ошибка: {e}")