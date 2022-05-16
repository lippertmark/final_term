import requests
import json


def get_mails(username):
    data = {'username': username}
    users = requests.get('https://jsonplaceholder.typicode.com/users', data).json()
    id = users[0]['id']
    data_posts = {
        'userId': id
    }
    posts = requests.get('https://jsonplaceholder.typicode.com/posts', data_posts).json()
    emails = []
    for post in posts:
        post_id = post['id']
        data_comments = {'postId': post_id}
        comments = requests.get('https://jsonplaceholder.typicode.com/comments', data_comments).json()
        for comment in comments:
            emails.append(comment['email'])
    print(emails)


get_mails('Bret')
