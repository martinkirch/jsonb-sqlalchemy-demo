from uuid import uuid4
from sqlalchemy import Column, String, TIMESTAMP, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.mutable import MutableDict
from sa_metadata import Base

class Article(Base):
    __tablename__ = 'articles_with_extra'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date = Column(TIMESTAMP(timezone=True), nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    extra = Column(MutableDict.as_mutable(JSONB), nullable=False, default={})

    __table_args__ = (
        Index('ix_article_with_extra_extra_slug', extra['slug'].astext),
        Index('ix_article_with_extra_extra_tag',
              extra['tags'],
              postgresql_using='gin'
        ),
    )

    def __repr__(self):
        return f"""# {self.title}
        Article#{self.uuid} written on {self.date}

        {self.content}"""
