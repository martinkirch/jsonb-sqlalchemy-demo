import logging
from datetime import datetime
from sa_common import connect
from model2 import Article

log = logging.getLogger()

def article_by_slug(session):
    article = Article(
        date=datetime.now(),
        title="Super Python Blog #3",
        content="Hello World of URI slugs",
        extra={
            'slug': 'super-python-blog-3'
        })
    session.add(article)

    article.extra['something_else'] = {'whatever': ['if', 'it', 'is', 'json', 0]}

    session.commit()

    article = session.query(Article).filter(Article.extra['slug'].astext == 'super-python-blog-3').first()
    log.info("Article by slug:")
    log.info("%r", article)


def tag_my_article(session):
    article = Article(
        date=datetime.now(),
        title="Super Python Blog #4",
        content="Now with tags",
        extra={
            'tags': ["JSONB", "PostGreSQL", "Python"]
        })
    session.add(article)

    session.commit()

    by_tag = session.query(Article).filter(Article.extra.contains({'tags': ["PostGreSQL"]})).all()
    log.info("All articles tagged PostGreSQL:")
    for article in by_tag:
        log.info("%r", article)


def the_update_trap(session):
    article = session.query(Article).filter(Article.extra.contains({'tags': ["PostGreSQL"]})).first()
    article.extra['tags'][0] = "JSON"
    session.commit()

    article_uuid = article.uuid
    # let SQLAlchemy forget about this article, so we really fetch it again
    session.expunge(article)

    article = session.query(Article).get(article_uuid)
    log.info("Articles tags are %r", article.extra.get('tags'))
    if article.extra['tags'][0] == "JSON":
        log.info("The tag was updated.")
    else:
        log.error("The tag wasn't updated !")


def avoiding_the_update_trap(session):
    article = session.query(Article).filter(Article.extra.contains({'tags': ["PostGreSQL"]})).first()
    article.extra['tags'][0] = "JSON"
    article.extra.changed() ## notice SQLAlchemy that this object should be flushed
    session.commit()

    article_uuid = article.uuid
    # let SQLAlchemy forget about this article, so we really fetch it again
    session.expunge(article)

    article = session.query(Article).get(article_uuid)
    log.info("Articles tags are %r", article.extra.get('tags'))
    if article.extra['tags'][0] == "JSON":
        log.info("The tag was updated.")
    else:
        log.error("The tag wasn't updated !")


if __name__ == '__main__':
    sqlalchemy_session = connect('conf.ini')
    article_by_slug(sqlalchemy_session)
    tag_my_article(sqlalchemy_session)
    the_update_trap(sqlalchemy_session)
    avoiding_the_update_trap(sqlalchemy_session)

