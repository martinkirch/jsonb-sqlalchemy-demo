"""
This module is isolated from ``sa_common`` because it's imported by all others,
and depends only on SQLAlchemy.
It defines the Base class (parent of our domain classes) and the metadata
object that helps SQLAlchemy and Alembic to find classes.
"""

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.readthedocs.org/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata, cls=DeferredReflection)
