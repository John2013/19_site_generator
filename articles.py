from collections import namedtuple
from os import listdir

from os.path import join, isfile, isdir


def parse_filename(filename):
    if "_" in filename:
        sort, name = filename.split('_', 1)
        try:
            sort = int(sort)
        except ValueError:
            sort, name = None, filename
    else:
        sort, name = None, filename

    if "." in name:
        name, _ = name.rsplit('.', 1)

    return sort, name


def find_article(sections, section_name, article_name):
    for section in sections:
        if (section.sort, section.name) == parse_filename(section_name):
            for article in section.articles:
                if (article.sort, article.name) == parse_filename(
                    article_name):
                    return article


def get_article_link(section_name, sort, name):
    if sort is not None:
        full_name = '{}_{}'.format(sort, name)
    else:
        full_name = name
    return '/articles/{}/{}'.format(
        section_name,
        full_name
    )


def get_article(basepath, section, article_filename):
    article = namedtuple(
        "article",
        ['name', 'path', 'sort', 'text', 'link']
    )
    article.path = join(basepath, section, article_filename)
    if article_filename[0] != '.' and isfile(article.path):
        article.sort, article.name = parse_filename(article_filename)
        article.link = get_article_link(section, article.sort, article.name)
        with open(article.path, encoding='utf-8') as article_file:
            article.text = article_file.read()
        return article
    return None


def get_articles(basepath, section_dirname):
    path = join(basepath, section_dirname)
    file_list = listdir(path)
    articles = []
    for entry in file_list:
        article = get_article(basepath, section_dirname, entry)
        if article is not None:
            articles.append(article)

    return articles


def get_sections(basepath="articles"):
    dir_list = listdir(basepath)
    sections = []
    for entry in dir_list:
        section = namedtuple(
            "section",
            ['name', 'sort', 'path', 'articles']
        )
        section.path = join(basepath, entry)
        if isdir(section.path) and entry[0] != ".":
            section.sort, section.name = parse_filename(entry)
            section.articles = get_articles(basepath, entry)
            sections.append(section)
    return sections


if __name__ == "__main__":
    sections = get_sections()

    article = find_article(sections, '2_html', 'html_injection')

    print(article.name)
    print(article.text)
