
from articles import get_topics, read_config, get_article
import os
from jinja2 import Environment, FileSystemLoader


def render_template(template_filename, **context):
    path = os.path.dirname(os.path.abspath(__file__))
    template_enviroment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, 'templates')),
        trim_blocks=False
    )
    return template_enviroment.get_template(template_filename).render(**context)


def index():
    config = read_config()
    topics = get_topics(config)
    return render_template("index.html", topics=topics)


def article_page(topic_dir, article_filename):
    article_source = '{}/{}'.format(topic_dir, article_filename)
    config = read_config()
    topics = get_topics(config)
    article = get_article(config, article_source)

    return render_template(
        "article.html",
        article=article,
        topics=topics
    )


def create_page(page_html, path):
    with open(path, mode='w', encoding='utf-8') as page_file:
        page_file.write(page_html)


# app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
    create_page(index(), 'index.html')

    config = read_config()
    for article in config['articles']:
        dirname, filename = article['source'].split('/', 1)
        # try:
        #     os.stat(dirname)
        # except FileNotFoundError:
        #     os.mkdir(dirname)
        html = article_page(dirname, filename)
        filename = '{}.html'.format(filename.rsplit('.', 1)[0])
        create_page(
            html,
            filename
        )
