import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------
# Подключение к PostgreSQL
# ---------------------------------------------
def get_connection():

    return psycopg2.connect(
        dbname="student",
        user="postgres_task",
        password="student",
        host="localhost",
        port="5435"
    )


# ---------------------------------------------
# Загрузка данных
# ---------------------------------------------
def fetch_data():

    query = """
    SELECT
        p.name AS product_name,
        p.category,
        pr.price,
        s.name AS supplier
    FROM public.products p
    JOIN public.prices pr
        ON p.id = pr.product_id
    JOIN public.suppliers s
        ON p.id = s.product_id
    """

    conn = get_connection()

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ---------------------------------------------
# Построение графиков
# ---------------------------------------------
def create_graphs(df):

    sns.set_theme(style="darkgrid")

    # =================================================
    # ГРАФИК 1 — Круговая диаграмма категорий
    # =================================================
    plt.figure(figsize=(10, 10))

    category_counts = df["category"].value_counts()

    plt.pie(
        category_counts.values,
        labels=category_counts.index,
        autopct="%1.1f%%",
        startangle=140
    )

    plt.title(
        "Доля товаров по категориям",
        fontsize=18,
        fontweight="bold"
    )

    plt.tight_layout()

    plt.show()

    # =================================================
    # ГРАФИК 2 — Распределение цен
    # =================================================
    plt.figure(figsize=(12, 6))

    sns.histplot(
        x=df["price"],
        bins=25,
        kde=True
    )

    mean_price = df["price"].mean()

    plt.axvline(
        mean_price,
        linestyle="--",
        linewidth=2,
        label=f"Средняя цена: {mean_price:.2f}"
    )

    plt.title(
        "Распределение цен товаров",
        fontsize=18,
        fontweight="bold"
    )

    plt.xlabel("Цена")

    plt.ylabel("Количество товаров")

    plt.legend()

    plt.tight_layout()

    plt.show()


# ---------------------------------------------
# Главная функция
# ---------------------------------------------
def main():

    print("Запуск аналитики...")

    data = fetch_data()

    print(data.head())

    create_graphs(data)


# ---------------------------------------------
# Запуск программы
# ---------------------------------------------
if __name__ == "__main__":
    main()