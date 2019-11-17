import logging
from datetime import datetime
from sa_common import connect
from model1 import Article

log = logging.getLogger()

def make_and_query_basic_articles(session):
    article = Article(
        date=datetime.now(),
        title="Super Python Blog #1",
        content="Hello World")
    session.add(article)

    another = Article(
        date=datetime.now(),
        title="Super Python Blog #2",
        content="It might look repetitive if you call the script again and again.")
    session.add(another)

    session.commit()

    articles = session.query(Article).order_by(Article.date.desc()).limit(5).all()
    log.info("Latest 5 articles in blog:")
    for article in articles:
        log.info("%r", article)


if __name__ == '__main__':
    make_and_query_basic_articles(connect('conf.ini'))
