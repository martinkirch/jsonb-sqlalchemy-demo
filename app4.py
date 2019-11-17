import logging
from datetime import datetime
from sa_common import connect
from model4 import Article, ImageArticle, TaggedArticle, ArticleType

log = logging.getLogger()

def create_articles(session):
    # the app fails from here because SQLAlchemy doesn't understand our polymorphic_on
    tagged = Article(content={
        'article_type': ArticleType.TAGGED.value,
        'date': datetime.now(),
        'title': "My first tagged article",
        'content': "Bla bla bla",
        'tags': ['blog'],
    })
    session.add(tagged)

    image = ImageArticle(content={
        'date': datetime.now(),
        'title': "My first picture",
        'url': "https://example.com/favicon.ico",
    })
    session.add(image)

    tagged = TaggedArticle(content={
        'date': datetime.now(),
        'title': "Another tagged article",
        'content': "Not much more inspired",
        'tags': ['article'],
    })
    session.add(tagged)

    image = ImageArticle(content={
        'date': datetime.now(),
        'title': "Another picture",
        'url': "https://example.com/favicon.ico",
    })
    session.add(image)

    session.commit()


def show_latest_articles(session):
    """
    It's exactly the same as in app1!
    """
    articles = session.query(Article).order_by(Article.date.desc()).limit(5).all()
    log.info("Latest 5 articles in blog:")
    for article in articles:
        log.info("%r", article)


def count_by_tag(session):
    count = session.query(TaggedArticle).filter(Article.extra.contains({'tags': ["article"]})).count()
    log.info("%d articles are tagged 'article'", count)



if __name__ == '__main__':
    sqlalchemy_session = connect('conf.ini')
    create_articles(sqlalchemy_session)
    show_latest_articles(sqlalchemy_session)
    count_by_tag(sqlalchemy_session)
