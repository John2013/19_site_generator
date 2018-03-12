import json
from markdown import markdown
from os.path import join, dirname, abspath


def read_config(path=None):
    if path is None:
        path = join(dirname(abspath(__file__)), 'config.json')
    with open(path, encoding="utf-8") as config_file:
        config = json.loads(config_file.read())
        for article in config['articles']:
            article['link'] = '/{}.html'.format(article['source'].rsplit('.', 1)[0])
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
        articles_dir_path = join(dirname(abspath(__file__)), 'articles')
    for article in config['articles']:
        if article['source'] == article_source:
            article['text'] = get_files_md_text(join(articles_dir_path, article['source']))
            return article


if __name__ == "__main__":
    config = read_config()
    print(config)
    print(get_topics(config))
    print(get_topic_articles(config, 'git'))
    print(get_article(config, '0_tutorial/14_google.md'))
