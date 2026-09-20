"""
Сервис поиска подкастов по темам.

Начальный сценарий (ПР1): поиск одного подкаста по теме, формирование
карточки подкаста и оформление подписки пользователя.

В сценарии используются только конструкции, изученные в рамках ПР1:
простые типы данных, операции, преобразование типов, ветвления, функции
и импорт стандартного модуля. Работа с коллекциями и классами будет
добавлена на ПР2-ПР3.
"""

from datetime import date

# --- Исходные данные (в дальнейшем будут приходить из базы данных) ---

podcast_name = "Разбор Полётов"
podcast_topic = "Технологии"
podcast_rating_raw = "4.8"     # рейтинг приходит строкой, например, из формы ввода
podcast_duration_min = 95      # длительность эпизода в минутах
is_available = True

user_name = "Резар"
search_query = "технологии"
is_already_subscribed = False


def search_by_topic(topic, query):
    """Проверяет, соответствует ли тема подкаста поисковому запросу."""
    topic_normalized = topic.lower()
    query_normalized = query.lower()
    return query_normalized in topic_normalized


def get_podcast_info(name, topic, rating_raw, duration, available):
    """Формирует текстовую карточку подкаста."""
    rating = float(rating_raw)         # преобразование типов: строка -> число
    rating_rounded = round(rating, 1)

    if rating_rounded >= 4.5:
        rating_label = "высокий рейтинг"
    elif rating_rounded >= 3.0:
        rating_label = "средний рейтинг"
    else:
        rating_label = "низкий рейтинг"

    hours = duration // 60
    minutes = duration % 60
    if hours > 0:
        duration_str = f"{hours} ч {minutes} мин"
    else:
        duration_str = f"{minutes} мин"

    availability_str = "доступен" if available else "недоступен"

    return (
        f"Подкаст: {name}\n"
        f"Тема: {topic}\n"
        f"Рейтинг: {rating_rounded} ({rating_label})\n"
        f"Длительность эпизода: {duration_str}\n"
        f"Статус: {availability_str}"
    )


def subscribe_user(user, podcast, already_subscribed):
    """Оформляет подписку пользователя на подкаст."""
    today = date.today()
    if already_subscribed:
        return f"{user} уже подписан(а) на «{podcast}»."
    return f"{user} подписался(лась) на «{podcast}» {today}."


def main():
    found = search_by_topic(podcast_topic, search_query)
    print(f"Поиск по теме «{search_query}»: {'найдено' if found else 'не найдено'}")
    print()

    if not found:
        print("Подкастов по заданной теме не найдено.")
        return

    print(get_podcast_info(
        podcast_name, podcast_topic, podcast_rating_raw,
        podcast_duration_min, is_available,
    ))
    print()

    print(subscribe_user(user_name, podcast_name, is_already_subscribed))


if __name__ == "__main__":
    main()
