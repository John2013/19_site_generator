from flask import Flask, render_template
from flaskext.markdown import Markdown
from werkzeug.contrib.fixers import ProxyFix

from articles import get_topics, read_config, get_article

app = Flask(__name__)
Markdown(app)


@app.route("/")
@app.route("/index")
def index():
    config = read_config()
    topics = get_topics(config)
    return render_template("index.html", topics=topics)


@app.route("/<topic_dir>/<article_filename>")
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


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run()
