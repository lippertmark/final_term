# Есть новостной портал, в котором есть пользователи и ленты новостей(топики). Каждый пользователь может быть
# подписан на произвольное количество топиков. Требуется чтобы при добавлении новости в топик все подписанные
# на этот топик пользователи получили эту новость(напечатали в консоли сообщения “пользователь <user_id> получил
# новость <feed_id>”). Нужно реализовать методы:
# 1.create_topic(topic_name: str):  создание топика
# 2.subscribe(user_id: int, topic: str): подписка пользователя на топик
# 3.post_feed(topic: str, feed_id: int): публикация новости в топик

topics = {

}

def create_topic(topic_name: str):
    topics[topic_name] = {
        'users': [],
        'feeds': [],
    }

def subscribe(user_id: int, topic: str):
    topics[topic]['users'].append(user_id)

def post_feed(topic: str, feed_id: int):
    topics[topic]['feeds'].append(feed_id)
    for user_id in topics[topic]['users']:
        print(f'пользователь {user_id} получил новость {feed_id}')

create_topic('IT')
subscribe(123, 'IT')
subscribe(145, 'IT')
post_feed('IT', 91)