"""
Created this one to see if we can have a really noSQL-like container.

It seems yes, but it doesn't work with SQLAlchemy's polymorphism (see app4)
"""


from uuid import uuid4
from enum import Enum
from sqlalchemy import Column, String, TIMESTAMP, Index, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.mutable import MutableDict
from sa_metadata import Base


class ArticleType(Enum):
    NONE = 0
    TAGGED = 1
    IMAGE = 2


class Article(Base):
    __tablename__ = 'really_no_schema'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    content = Column(MutableDict.as_mutable(JSONB), nullable=False, default={})

    __mapper_args__ = {
        'polymorphic_on': content['article_type'], # FIXME
        'polymorphic_identity': 0,
    }

    def __repr__(self):
        return f"""# {self.content['title']}
        Article#{self.uuid} written on {self.content['date']}

        {self.content['content']}"""
    

class TaggedArticle(Article):
    __mapper_args__ = {'polymorphic_identity': ArticleType.TAGGED.value}

    def __repr__(self):
        return super().__repr__() + f"\n\nTagged {self.extra['tags']}"


class ImageArticle(Article):
    __mapper_args__ = {'polymorphic_identity': ArticleType.IMAGE.value}

    def __repr__(self):
        return f"""# {self.content['title']}
        Picture#{self.uuid} published on {self.content['date']}

        <img src="{self.content['url']}">
        """
