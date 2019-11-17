from uuid import uuid4
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sa_metadata import Base

class Article(Base):
    __tablename__ = 'articles'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date = Column(TIMESTAMP(timezone=True), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def __repr__(self):
        return f"""# {self.title}
        Article#{self.uuid} written on {self.date}

        {self.content}"""
