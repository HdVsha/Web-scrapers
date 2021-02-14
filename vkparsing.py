import requests
import json
from vk_api import VkApi, AuthError


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def take_1000_posts():
    # count is 100 bc vk only allows to request 100 items at once --- that's why it is cycle
    token = ''
    offset = 0
    count = 100
    all_posts = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': 5.124,
                                    'domain': 'prepod_mipt',
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(all_posts):
    with open('prepod_mipt.txt', 'w') as file:
        for post in all_posts:
            try:
                file.writelines(post['text'])
            except:
                pass

#228894487
if __name__ == "__main__":
    print("Hello World")
    #file_writer(take_1000_posts())
    vk_session = VkApi(token='')
    # vk_session.auth()
    # vk = vk_session.get_api()
    vk = vk_session.get_api()
    while True:
        msg = input()
        vk.messages.send(user_id=228894487, message=msg, random_id=2)




