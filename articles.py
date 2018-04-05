import json
from markdown import markdown

import os


def read_config(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(path, encoding="utf-8") as config_file:
        config = json.loads(config_file.read())
        zero = 0
        one = 1
        for article in config['articles']:
            article['link'] = '{}.html'.format((article['source'].rsplit('/', one)[one]).rsplit('.', one)[zero])
        return config


def get_topic_articles(config, topic_slug):
    return list(filter(lambda article: article['topic'] == topic_slug, config['articles']))


def get_topics(config=None):
    if config is None:
        config = read_config()
    topics = []
    for topic in config['topics']:
        topic['articles'] = get_topic_articles(config, topic['slug'])
        topics.append(topic)

    return topics


def get_files_md_text(path: str):
    with open(path, encoding='utf-8') as text_file:
        return markdown(text_file.read())


def get_article(config, article_source, articles_dir_path=None):
    if articles_dir_path is None:
        articles_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'articles')
    for article in config['articles']:
        if article['source'] == article_source:
            article['text'] = get_files_md_text(os.path.join(articles_dir_path, article['source']))
            return article


if __name__ == "__main__":
    config = read_config()
    print(config)
    print(get_topics(config))
    print(get_topic_articles(config, 'git'))
    print(get_article(config, '0_tutorial/14_google.md'))
