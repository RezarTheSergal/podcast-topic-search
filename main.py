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


def get_rating_level(rating):
    if rating >= 4.5:
        return "высокий рейтинг"
    if rating >= 3.0:
        return "средний рейтинг"
    return "низкий рейтинг"


def format_duration(duration):
    hours = duration // 60
    minutes = duration % 60
    if hours > 0:
        return f"{hours} ч {minutes} мин"
    return f"{minutes} мин"


def get_podcast_info(name, topic, rating_raw, duration, available):
    rating = float(rating_raw)
    rating_rounded = round(rating, 1)
    rating_label = get_rating_level(rating_rounded)
    availability_str = "доступен" if available else "недоступен"

    return (
        f"Подкаст: {name}\n"
        f"Тема: {topic}\n"
        f"Рейтинг: {rating_rounded} ({rating_label})\n"
        f"Длительность эпизода: {format_duration(duration)}\n"
        f"Статус: {availability_str}"
    )


def subscribe_user(user, podcast, already_subscribed):
    today = date.today()
    if already_subscribed:
        return f"{user} уже подписан(а) на «{podcast}»."
    return f"{user} подписался(лась) на «{podcast}» {today}."


def main():
    found = search_by_topic(podcast_topic, search_query)
    result = "найдено" if found else "не найдено"
    print(f"Поиск по теме «{search_query}»: {result}")
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
