"""index article slug

Revision ID: 8d8c4720b995
Revises: 4424b7c67f9c
Create Date: 2019-11-15 18:36:28.225610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d8c4720b995'
down_revision = '4424b7c67f9c'
branch_labels = None
depends_on = None


def upgrade():
    # handmade migration !
    op.create_index(op.f('ix_articles_with_extra_extra_slug'), 'articles_with_extra', [sa.text("(extra->>'slug')")])


def downgrade():
    op.drop_index(op.f('ix_articles_with_extra_extra_slug'), table_name='articles_with_extra')
