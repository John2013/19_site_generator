from flask import Flask, render_template
from flaskext.markdown import Markdown
from werkzeug.contrib.fixers import ProxyFix

import articles

app = Flask(__name__)
Markdown(app)


@app.route("/")
@app.route("/index")
def index():
    sections = articles.get_sections()
    return render_template("index.html", sections=sections)


@app.route("/articles/<section_name>/<article_name>")
def article_page(section_name, article_name):
    sections = articles.get_sections()
    article = articles.find_article(sections, section_name, article_name)
    if "_" in section_name:
        _, section_name = section_name.split("_", 1)
    else:
        section_name = section_name
    return render_template(
        "article.html",
        article=article,
        section_name=section_name,
        sections=sections
    )


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run()
