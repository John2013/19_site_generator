
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
    return template_enviroment.get_template(template_filename).render(
        **context
    )


def index(config):
    topics = get_topics(config)
    return render_template("index.html", topics=topics)


def article_page(topic_dir, article_filename, config):
    article_source = '{}/{}'.format(topic_dir, article_filename)
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


if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
    config = read_config()
    results_dir = 'docs'
    create_page(index(config), '{}/index.html'.format(results_dir))
    split_count = 1
    article_name_num = 0

    for article in config['articles']:
        dirname, filename = article['source'].split('/', split_count)

        html = article_page(dirname, filename, config)
        filename = '{dir}/{article_name}.html'.format(
            article_name=filename.rsplit('.', split_count)[article_name_num],
            dir=results_dir
        )
        create_page(
            html,
            filename
        )
