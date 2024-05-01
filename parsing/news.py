import requests
from bs4 import BeautifulSoup
from .models import News


def clear_database():
    News.objects.all().delete()


def save_news_to_database(news_list):
    news_objects = [
        News(category=news['category'], short_description=news['short_description'],
             news_link=news['news_link'], photo_link=news['photo_link'])
        for news in news_list
    ]
    News.objects.bulk_create(news_objects)


def other_news(url="https://tsn.ua/other"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Other", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Other", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Other", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Other", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def politika_news(url='https://tsn.ua/politika'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Politika", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Politika", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Politika", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Politika", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def auto_news(url="https://tsn.ua/auto"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Cars", "short_description": article_text['text_1'], "news_link": article_href["href_1"],
                   "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Cars", "short_description": article_text['text_2'], "news_link": article_href["href_2"],
                   "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Cars", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Cars", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def health_news(url="https://tsn.ua/zdorovya"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Health", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Health", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Health", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Health", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def economy_news(url="https://tsn.ua/groshi"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Economy", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Economy", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Economy", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Economy", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def sport_news(url="https://tsn.ua/prosport"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(3) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Sport", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Sport", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Sport", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Sport", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def tourism_news(url='https://tsn.ua/tourism'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Tourism", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Tourism", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Tourism", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Tourism", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


def science_and_it_news(url="https://tsn.ua/nauka_it"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    all_articles = soup.find_all('a', class_='c-card__link')

    article_text = {}
    article_href = {}
    article_photo = {}

    if len(all_articles) > 1:
        second_articles = all_articles[8:12]

    for i, article in zip(range(1, 5), second_articles):
        text = article.get_text()[:35]
        article_href[f'href_{i}'] = article['href']
        article_text[f'text_{i}'] = text + '...' if len(article.get_text()) > 35 else text

    first_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1) > article > figure > div > img')
    second_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > article > figure > div > img')
    third_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(4) > article > figure > div > img')
    fourth_photo = soup.select_one(
        'body > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > main > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(5) > article > figure > div > img')

    for i, photo in zip(range(1, 5), (first_photo, second_photo, third_photo, fourth_photo)):
        if photo and 'data-src' in photo.attrs:
            article_photo[f'photo_{i}'] = photo['data-src']

    all_articles = []

    one_article = {"category": "Science", "short_description": article_text['text_1'],
                   "news_link": article_href["href_1"], "photo_link": article_photo["photo_1"]}
    two_article = {"category": "Science", "short_description": article_text['text_2'],
                   "news_link": article_href["href_2"], "photo_link": article_photo["photo_2"]}
    thre_article = {"category": "Science", "short_description": article_text['text_3'],
                    "news_link": article_href["href_3"], "photo_link": article_photo["photo_3"]}
    four_article = {"category": "Science", "short_description": article_text['text_4'],
                    "news_link": article_href["href_4"], "photo_link": article_photo["photo_4"]}

    all_articles.append(one_article)
    all_articles.append(two_article)
    all_articles.append(thre_article)
    all_articles.append(four_article)

    return all_articles


if __name__ == '__main__':
    other = other_news('https://tsn.ua/other')
    politika = politika_news('https://tsn.ua/politika')
    cars = auto_news('https://tsn.ua/auto')
    health = health_news('https://tsn.ua/zdorovya')
    economy = economy_news('https://tsn.ua/groshi')
    sport = sport_news('https://tsn.ua/prosport')
    tourism = tourism_news('https://tsn.ua/tourism')
    science = science_and_it_news('https://tsn.ua/nauka_it')
    save_news_to_database(other)
    save_news_to_database(politika)
    save_news_to_database(cars)
    save_news_to_database(health)
    save_news_to_database(economy)
    save_news_to_database(sport)
    save_news_to_database(tourism)
    save_news_to_database(science)
