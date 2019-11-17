"""no schema table

Revision ID: 73cfa57e360e
Revises: 138d1fa2b3d4
Create Date: 2019-11-17 20:16:38.157699

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '73cfa57e360e'
down_revision = '138d1fa2b3d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('really_no_schema',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('content', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_really_no_schema'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('really_no_schema')
    # ### end Alembic commands ###
