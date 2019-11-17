from uuid import uuid4
from enum import Enum
from sqlalchemy import Column, String, TIMESTAMP, Index, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.mutable import MutableDict
from sa_metadata import Base


class ArticleType(Enum):
    TAGGED = 1
    IMAGE = 2


class Article(Base):
    __tablename__ = 'articles_polymorphic'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    article_type = Column(Integer)
    date = Column(TIMESTAMP(timezone=True), nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    extra = Column(MutableDict.as_mutable(JSONB), nullable=False, default={})

    __table_args__ = (
        Index('ix_articles_polymorphic_extra_slug', extra['slug'].astext),
        Index('ix_articles_polymorphic_extra_tag',
              extra['tags'],
              postgresql_using='gin'
        ),
    )
    __mapper_args__ = {
        'polymorphic_on': article_type,
        'polymorphic_identity': None,
    }

    def __repr__(self):
        return f"""# {self.title}
        Article#{self.uuid} written on {self.date}

        {self.content}"""
    

class TaggedArticle(Article):
    __mapper_args__ = {'polymorphic_identity': ArticleType.TAGGED.value}

    def __repr__(self):
        return super().__repr__() + f"\n\nTagged {self.extra['tags']}"


class ImageArticle(Article):
    __mapper_args__ = {'polymorphic_identity': ArticleType.IMAGE.value}

    def __repr__(self):
        return f"""# {self.title}
        Picture#{self.uuid} published on {self.date}

        <img src="{self.content}">
        """
