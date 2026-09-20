"""
ВСПОМОГАТЕЛЬНЫЙ ФАЙЛ ДЛЯ УПРАЖНЕНИЯ ПО ОТЛАДКЕ (п. 6.6 методички).

Это main.py с ОДНОЙ намеренно внесённой ошибкой в функции
get_podcast_info(): пропущено преобразование строки в число.
Файл нужен только для демонстрации отладчику — рабочая версия
находится в main.py.

Как воспроизвести упражнение:
1. Открой этот файл в IDE (PyCharm / VS Code).
2. Поставь breakpoint на строке "rating_rounded = round(rating, 1)".
3. Запусти файл в режиме отладки (Debug), а не обычного запуска.
4. Выполни программу пошагово (Step Over) до breakpoint.
5. Посмотри в панели переменных значение rating -> увидишь,
   что это строка "4.8" (str), а не число (float).
6. Выполни ещё один шаг (Step Into/Over) -> программа упадёт с
   TypeError: type str doesn't define __round__ method,
   потому что round() нельзя применить к строке.
7. Вывод: причина ошибки - в get_podcast_info() пропущена строка
   rating = float(rating_raw), поэтому в rating попадает исходная
   строка вместо числа.
8. Исправление -> см. main.py, где перед round() выполняется
   rating = float(rating_raw).

Подробное описание хода отладки - в файле DEBUG_NOTES.md.
"""

from datetime import date

podcast_name = "Разбор Полётов"
podcast_topic = "Технологии"
podcast_rating_raw = "4.8"
podcast_duration_min = 95
is_available = True

user_name = "Резар"
search_query = "технологии"
is_already_subscribed = False


def search_by_topic(topic, query):
    topic_normalized = topic.lower()
    query_normalized = query.lower()
    return query_normalized in topic_normalized


def get_podcast_info(name, topic, rating_raw, duration, available):
    rating = rating_raw                 # <-- ОШИБКА: забыли float(rating_raw)
    rating_rounded = round(rating, 1)   # здесь программа упадёт

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
