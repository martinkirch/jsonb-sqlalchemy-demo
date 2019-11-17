"""index article tags

Revision ID: 235691aa0ca4
Revises: 8d8c4720b995
Create Date: 2019-11-17 18:28:15.640730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '235691aa0ca4'
down_revision = '8d8c4720b995'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(op.f('ix_articles_with_extra_extra_tags'), 'articles_with_extra', [sa.text("(extra->'tags')")], postgresql_using="GIN")


def downgrade():
    op.drop_index(op.f('ix_articles_with_extra_extra_tags'), table_name='articles_with_extra')
